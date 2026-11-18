# Uploading the course data to Source Cooperative

Target product: <https://source.coop/giuz/sds210> (S3 path `s3://giuz/sds210/`, public URLs
`https://data.source.coop/giuz/sds210/...`).

Files in this folder:

| File | Purpose |
|---|---|
| `manifest.csv` | The 59 files to publish: target path, size and SHA-256 (for files in this repository), where to get each file, which lessons use it, and which current link it replaces |
| `product-README.md` | Becomes `README.md` on the Source Cooperative page |
| `stage_data.py` | Builds the upload folder, verifies checksums, writes `SHA256SUMS`, and checks the upload afterwards |

## 1. Confirm the open sources

`product-README.md` has `TODO(confirm)` markers where the source or licence could not be read
from the lessons or file metadata (snowshoe trails, parks, hospital landing sites, nuclear power
plants, the Practical L6 weather station, the Alpine Convention perimeter, HydroSHEDS licence).
Fill them in and delete the markers; the staging step refuses to finish while any are left.

## 2. Stage the files

```bash
conda run -n sds210 python source-coop/stage_data.py --out ~/sds210-source-coop
```

This copies 51 files from this repository, downloads 5 from GitLab and 3 from Google Drive
(including the 831 MB `hydrorivers_100.gpkg`), about 1.4 GB in total. It also downloads the
second copies listed in `compare_with` and prints whether they are identical. Review these lines:

- `L07/swissBoundaries3D_cantons.gpkg` and `L07/wohnungsinventar.gpkg`: the copies in this
  repository differ from those on GitLab. The script stages the repository copy; if the GitLab
  one is the current version, change the row in `manifest.csv` to `source_type` `gitlab`.
- `L09/S2_composite_*.tif` and the five `L10` practical files: expected to be identical to the
  Google Drive copies the notebooks download today under shorter names.

Useful options: `--only L06,L07` stages selected lessons, `--no-compare` skips the comparison
downloads, `--cog` converts all GeoTIFFs to Cloud-Optimized GeoTIFFs (same pixel values, adds
overviews so Python can read parts of a raster over the web; the checksums then change, and
`SHA256SUMS` is written after the conversion).

## 3. Install the Source CLI and sign in

```bash
brew install source-cooperative/tap/source-coop
source-coop --version
source-coop login               # opens the browser (older versions: `source-coop auth login`)
```

If the product page shows no upload or credentials option under the lock icon, ask
hello@source.coop for upload access.

## 4. Configure the AWS CLI

Add a profile to `~/.aws/config`:

```ini
[profile source-coop]
credential_process = source-coop creds
region = us-west-2
s3 =
  multipart_threshold = 1
```

`multipart_threshold = 1` makes the CLI send every file as a multipart upload. With AWS CLI
2.11, single uploads (files under 8 MB) are rejected by the Source Cooperative server with
"There were headers present in the request which were not signed"; multipart uploads are
accepted.

The installed AWS CLI (2.11) is older than 2.13, which added `endpoint_url` to profiles, so the
commands below pass `--endpoint-url` explicitly. (After `brew upgrade awscli` you could add
`endpoint_url = https://data.source.coop` to the profile instead.)

## 5. Upload

Dry run first; it lists what would be uploaded without changing anything:

```bash
aws s3 sync ~/sds210-source-coop s3://giuz/sds210/ \
  --profile source-coop --endpoint-url https://data.source.coop \
  --exclude ".DS_Store" --dryrun
```

Then upload:

```bash
aws s3 sync ~/sds210-source-coop s3://giuz/sds210/ \
  --profile source-coop --endpoint-url https://data.source.coop \
  --exclude ".DS_Store"
```

`sync` only transfers new or changed files, so you can rerun it after an interruption, or upload
lesson by lesson (`aws s3 sync ~/sds210-source-coop/L07 s3://giuz/sds210/L07/ ...`).

## 6. Verify

```bash
aws s3 ls s3://giuz/sds210/ --recursive --profile source-coop --endpoint-url https://data.source.coop
conda run -n sds210 python source-coop/stage_data.py --out ~/sds210-source-coop --verify-remote
```

The second command checks every file through its public URL and compares the sizes with the
staged copies.

## 7. Afterwards

- The notebooks of L06 to L10 read their data from these URLs; Practicals L8 to L10 download
  their larger files into a local `data` folder first. (The `replaces` column of `manifest.csv`
  lists the GitLab and Google Drive links and the old file names they replaced.) When you add or
  rename a file later, update `manifest.csv`, stage and sync again, then update the notebooks.
- Remove the data files from this repository and optionally rewrite its history to shrink it.
