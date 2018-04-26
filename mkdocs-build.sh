#!/usr/bin/env bash
set -o errexit -o nounset

# Get curent commit revision
rev=$(git rev-parse --short HEAD)

# Initialize gh-pages checkout
(
    cd docs/
    git config user.name "${GH_USER_NAME}"
    git config user.email "${GH_USER_EMAIL}"
    git remote add upstream "https://${GH_TOKEN}@${GH_REF}"
    git fetch upstream
    git reset upstream/gh-pages
)

# Commit and push the documentation to gh-pages
(
    touch .
    git add -A .
    git commit -m "Deployed ${rev} with MkDocs version: 0.17.3"
    git push -q upstream HEAD:gh-pages
)

mkdocs build --clean
