#!/usr/bin/env bash
set -e; cd "$(dirname "$0")/../.."
out="../cos-ignacio-$(date +%Y%m%d).bundle"
git bundle create "$out" --all && echo "Export: $out (restaurar con: git clone $out cos-ignacio)"
