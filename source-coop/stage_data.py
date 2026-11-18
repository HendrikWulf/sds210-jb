"""Assemble the SDS210 course data for upload to Source Cooperative (giuz/sds210).

Reads manifest.csv (next to this script) and builds a folder with exactly the
layout of the Source Cooperative product:

    <out>/README.md            (copied from product-README.md)
    <out>/SHA256SUMS
    <out>/L06/... <out>/L10/...

Files come from this repository, from GitLab or from Google Drive, as listed in
the manifest. Every file with a known checksum is verified. Files with a
`compare_with` entry are also downloaded from that second location and
compared, so you can see whether the two copies are identical.

Run it with the course environment (needs requests and gdown; rasterio for --cog):

    conda run -n sds210 python source-coop/stage_data.py --out ~/sds210-source-coop

After uploading, check that every file is online:

    conda run -n sds210 python source-coop/stage_data.py --out ~/sds210-source-coop --verify-remote
"""

import argparse
import csv
import hashlib
import shutil
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
MANIFEST = HERE / "manifest.csv"
PUBLIC_BASE = "https://data.source.coop/giuz/sds210/"


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def download_http(url, dest):
    import requests

    with requests.get(url, stream=True, timeout=120) as r:
        r.raise_for_status()
        with open(dest, "wb") as f:
            for chunk in r.iter_content(1 << 20):
                f.write(chunk)


def download_gdrive(file_id, dest):
    import gdown

    result = gdown.download(id=file_id, output=str(dest), quiet=False)
    if result is None or not Path(dest).exists():
        raise RuntimeError(f"Google Drive download failed for id {file_id}")


def fetch(source_type, source, dest):
    """Put one file at dest, from the repository, a URL or Google Drive."""
    dest.parent.mkdir(parents=True, exist_ok=True)
    if source_type == "repo":
        shutil.copy2(REPO / source, dest)
    elif source_type in ("gitlab", "http"):
        download_http(source, dest)
    elif source_type == "gdrive":
        download_gdrive(source, dest)
    else:
        raise ValueError(f"unknown source type {source_type!r}")


def parse_alt(alt):
    if alt.startswith("gdrive:"):
        return "gdrive", alt.split(":", 1)[1]
    return "http", alt


def to_cog(path):
    """Rewrite a GeoTIFF as a Cloud-Optimized GeoTIFF (same pixel values)."""
    import rasterio
    from rasterio.shutil import copy as rio_copy

    with rasterio.open(path) as src:
        integer = src.dtypes[0].startswith(("int", "uint"))
    tmp = path.with_suffix(".cog.tif")
    rio_copy(path, tmp, driver="COG", COMPRESS="DEFLATE", PREDICTOR="YES",
             RESAMPLING="NEAREST" if integer else "AVERAGE", BIGTIFF="IF_SAFER")
    tmp.replace(path)


def stage(out, compare, cog, only=None):
    rows = list(csv.DictReader(MANIFEST.open(encoding="utf-8")))
    if only:
        rows = [r for r in rows if r["target_path"].split("/")[0] in only]
    problems, comparisons = [], []
    for i, row in enumerate(rows, 1):
        target = out / row["target_path"]
        expected = row["sha256"]
        label = f"[{i:2d}/{len(rows)}] {row['target_path']}"
        if target.exists() and (not expected or sha256(target) == expected):
            print(f"{label}: already staged")
        else:
            print(f"{label}: fetching from {row['source_type']}")
            try:
                fetch(row["source_type"], row["source"], target)
            except Exception as exc:  # keep going, report at the end
                problems.append(f"{row['target_path']}: download failed ({exc})")
                continue
        actual = sha256(target)
        if expected and actual != expected:
            problems.append(f"{row['target_path']}: checksum mismatch (manifest {expected[:12]}, got {actual[:12]})")
        if compare and row["compare_with"]:
            alt_type, alt_source = parse_alt(row["compare_with"])
            with tempfile.TemporaryDirectory() as tmp:
                alt_path = Path(tmp) / target.name
                try:
                    fetch(alt_type, alt_source, alt_path)
                    same = sha256(alt_path) == actual
                    comparisons.append(f"{'identical' if same else 'DIFFERENT'}: {row['target_path']}  vs  {row['compare_with']}")
                except Exception as exc:
                    comparisons.append(f"not compared: {row['target_path']} ({exc})")

    if cog:
        for tif in sorted(out.glob("L*/*.tif")):
            print(f"converting to COG: {tif.relative_to(out)}")
            to_cog(tif)

    readme = (HERE / "product-README.md").read_text(encoding="utf-8")
    open_todos = readme.count("TODO(confirm)")
    if open_todos:
        problems.append(f"product-README.md still has {open_todos} TODO(confirm) markers: confirm those sources, then rerun")
    shutil.copy2(HERE / "product-README.md", out / "README.md")
    files = sorted(p for p in out.rglob("*") if p.is_file() and p.name not in ("SHA256SUMS", ".DS_Store"))
    with open(out / "SHA256SUMS", "w", encoding="utf-8") as f:
        for p in files:
            f.write(f"{sha256(p)}  {p.relative_to(out).as_posix()}\n")

    total = sum(p.stat().st_size for p in files)
    print(f"\nStaged {len(files)} files ({total / 1e6:,.0f} MB) in {out}")
    if comparisons:
        print("\nComparison with second copies:")
        for line in comparisons:
            print("  " + line)
    if problems:
        print("\nPROBLEMS (fix these before uploading):")
        for line in problems:
            print("  " + line)
        return 1
    print("\nAll checksums OK. Next: upload with `aws s3 sync` (see UPLOAD.md).")
    return 0


def verify_remote(out):
    import requests

    sums = out / "SHA256SUMS"
    if not sums.exists():
        sys.exit(f"{sums} not found: run the staging step first")
    missing = 0
    entries = [line.split("  ", 1)[1].strip() for line in sums.read_text(encoding="utf-8").splitlines()]
    for rel in entries + ["SHA256SUMS"]:
        url = PUBLIC_BASE + rel
        r = requests.head(url, timeout=60, allow_redirects=True)
        local_size = (out / rel).stat().st_size
        remote_size = int(r.headers.get("Content-Length", -1))
        ok = r.status_code == 200 and remote_size == local_size
        missing += not ok
        print(f"{'OK  ' if ok else 'FAIL'} {r.status_code} {rel}" + ("" if ok else f" (local {local_size} B, remote {remote_size} B)"))
    print(f"\n{len(entries) + 1 - missing} of {len(entries) + 1} files online and complete.")
    return 1 if missing else 0


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out", type=Path, required=True, help="staging folder (created if needed)")
    parser.add_argument("--no-compare", action="store_true", help="skip downloading the second copies for comparison")
    parser.add_argument("--cog", action="store_true", help="convert all GeoTIFFs to Cloud-Optimized GeoTIFFs")
    parser.add_argument("--only", help="comma-separated lesson folders to stage, e.g. L06,L07")
    parser.add_argument("--verify-remote", action="store_true", help="check the uploaded files on data.source.coop")
    args = parser.parse_args()
    out = args.out.expanduser().resolve()
    if args.verify_remote:
        sys.exit(verify_remote(out))
    out.mkdir(parents=True, exist_ok=True)
    only = set(args.only.split(",")) if args.only else None
    sys.exit(stage(out, compare=not args.no_compare, cog=args.cog, only=only))


if __name__ == "__main__":
    main()
