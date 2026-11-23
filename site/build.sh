#!/usr/bin/env sh
# Build the Mycelium marketing pages from Soil.
#
# The shared core is vendored in site/vendor so this repository does not need a
# second checkout. Provide a compatible soil-lang binary:
#
#   SOIL_LANG=/path/to/soil-lang site/build.sh
set -eu
cd "$(dirname "$0")/.."

BIN=${SOIL_LANG:-}
if [ -z "$BIN" ] && command -v soil-lang >/dev/null 2>&1; then
  BIN=$(command -v soil-lang)
fi
if [ -z "$BIN" ] || [ ! -x "$BIN" ]; then
  echo "set SOIL_LANG to a compatible soil-lang binary" >&2
  exit 1
fi

run_soil() {
  output=$(mktemp)
  "$BIN" \
    site/vendor/prelude.soil \
    site/vendor/ui.soil \
    site/site.soil \
    "$1" > "$output"
  python3 - "$output" <<'PY'
import sys
text = open(sys.argv[1]).read()
if text.endswith("nil\n"):
    text = text[:-4]
sys.stdout.write(text.rstrip("\n") + "\n")
PY
  rm -f "$output"
}

find site/pages -name '*.soil' -type f | sort | while IFS= read -r page; do
  rel=${page#site/pages/}
  out="public/${rel%.soil}.html"
  mkdir -p "$(dirname "$out")"
  run_soil "$page" > "$out"
  echo "wrote $out"
done
