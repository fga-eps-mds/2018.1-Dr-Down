#!/usr/bin/env bash
set -o errexit -o nounset

# Configure the git inside of Travis Machine

git config user.name "${GH_USER_NAME}"
git config user.email "${GH_USER_EMAIL}"
git remote add upstream "https://${GH_TOKEN}@${GH_REF}"
git fetch upstream

mkdocs build --clean
