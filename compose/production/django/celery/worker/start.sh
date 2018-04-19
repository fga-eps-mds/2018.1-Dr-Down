#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset


celery -A drdown.taskapp worker -l INFO
