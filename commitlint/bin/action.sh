#!/usr/bin/env bash

# Alternative entrypoint for GitHub Action
# We embed this in our image to avoid rebuilding it at action runtime

usage() {
  echo "Usage: $0 [-c <sha>] [-m <string>]" 1>&2
  exit 1
}

while getopts ":c:m:" opt; do
  case "${opt}" in
    c)
      commit="$OPTARG"
      ;;
    m)
      message="$OPTARG"
      ;;
    *)
      usage
      ;;
  esac
done

if [ -n "$message" ]; then
  echo "$message" | exec /usr/local/bin/commitlint
elif [ -n "$commit" ]; then
  exec /usr/local/bin/commitlint --from "$commit"
fi
