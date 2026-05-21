#!/usr/bin/env bash
# Read the commit message on the host and pipe it into the commitlint
# container on stdin. Reading on the host avoids bind-mount issues when
# the repo is a git worktree (where .git is a file pointing outside the
# working tree).
set -euo pipefail
exec docker run --rm -i extenda/commitlint < "$1"
