#!/usr/bin/env bash
# Remove all practical sample solutions from the history of the public repository.
#
# After the takedown (1 July), the released solutions are gone from the book and from the
# current files, but they remain in old commits: anyone who clones the repository can still
# find them. Run this once a year after the takedown and before the next semester, if the
# practicals will be reused. See ANNUAL-CHECKLIST.md and .github/RELEASING-SOLUTIONS.md.
#
#   bash .github/scripts/purge_solution_history.sh
#
# What it does:
#   1. clones the repository from GitHub into a temporary folder (your working folder is not touched)
#   2. saves a backup of the full history to ~/sds210-jb-history-backup-<date>.bundle
#   3. rewrites every commit without the solution files (git filter-repo)
#   4. asks for confirmation, then force-pushes main and the other branches to GitHub
#
# Afterwards every existing clone (yours on other computers too) must be reset; the script prints
# how. Needs git-filter-repo:  pip install git-filter-repo   (or: brew install git-filter-repo)

set -euo pipefail

REPO_URL="${REPO_URL:-https://github.com/HendrikWulf/sds210-jb.git}"
# The same file names the .gitignore rule covers: <nr>_practical[-_]L<nr>[-_]solution(s).ipynb/.md
SOLUTIONS_RE='(^|/)[0-9]+_practical[-_]?(L[0-9]+)?[-_]solutions?\.(ipynb|md)$'

command -v git-filter-repo >/dev/null || {
  echo "git-filter-repo is not installed: pip install git-filter-repo"; exit 1; }

work="$(mktemp -d)"
trap 'rm -rf "$work"' EXIT
echo "Cloning $REPO_URL ..."
git clone --quiet --mirror "$REPO_URL" "$work/repo.git"
cd "$work/repo.git"

# Count solution paths in the history of the branches. (GitHub's pull-request snapshots,
# refs/pull/*, are read-only and cannot be rewritten; they are dropped below.)
count_solutions() { git log --branches --tags --name-only --format= | sort -u | grep -cE "$SOLUTIONS_RE" || true; }

current=$(git ls-tree -r --name-only main | grep -cE "$SOLUTIONS_RE" || true)
if [ "$current" -ne 0 ]; then
  echo "Solutions are currently released on main (the course is running or the takedown has"
  echo "not happened yet). Run this only after the takedown."
  exit 1
fi

found=$(count_solutions)
if [ "$found" -eq 0 ]; then
  echo "No solution files in the history of the branches: nothing to do."
  exit 0
fi
echo "Solution files found in the history: $found paths."

backup="$HOME/sds210-jb-history-backup-$(date +%Y-%m-%d-%H%M%S).bundle"
[ ! -e "$backup" ] || { echo "$backup already exists; try again in a second."; exit 1; }
git bundle create --quiet "$backup" --all
echo "Backup of the full history: $backup"

git for-each-ref --format='delete %(refname)' refs/pull | git update-ref --stdin
git ls-tree -r main > "$work/before.txt"
git filter-repo --force --invert-paths --path-regex "$SOLUTIONS_RE"
git ls-tree -r main > "$work/after.txt"
cmp -s "$work/before.txt" "$work/after.txt" || {
  echo "Unexpected: the current files on main would change. Stopping without pushing."; exit 1; }
left=$(count_solutions)
echo "Rewritten. Solution files left in the history: $left. Current files on main: unchanged."

read -r -p "Force-push the rewritten history to GitHub now? Type yes: " answer
[ "$answer" = yes ] || { echo "Not pushed. Nothing changed on GitHub."; exit 0; }
git remote add origin "$REPO_URL" 2>/dev/null || git remote set-url origin "$REPO_URL"
git push --force origin 'refs/heads/*:refs/heads/*'
# Tags point to old commits too; push their rewritten versions (if there are any).
if [ -n "$(git tag)" ]; then git push --force origin 'refs/tags/*:refs/tags/*'; fi

cat <<'EOF'

Done. On every computer with a clone of sds210-jb:
  1. copy the book/*/data folders somewhere safe if they exist there
  2. git fetch origin && git reset --hard origin/main    (commit or stash your work first)
  3. copy the data folders back
GitHub may keep old pull-request snapshots; ask GitHub Support to remove them if needed
(docs: "Removing sensitive data from a repository").
EOF
