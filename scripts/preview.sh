#!/bin/sh

set -eu

repo_root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
port=${PORT:-8000}

exec python3 -m http.server "$port" --directory "$repo_root/site" --bind 0.0.0.0
