#!/usr/bin/env bash

ARGS="--config /work/commitlint.config.js"

if [ "$1" == ".git/COMMIT_EDITMSG" ]; then
  # Running from pre-commit hook.
  ARGS="$ARGS --edit $1"
else
  # Use whatever args we where passed.
  ARGS="$ARGS $*"
fi

# shellcheck disable=SC2086
exec /work/node_modules/.bin/commitlint $ARGS
