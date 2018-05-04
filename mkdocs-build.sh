#!/usr/bin/env bash
set -o errexit -o nounset

# Get current commit revision
rev=$(git rev-parse --short HEAD)

# Configure the git inside of Travis Machine
(
  git config user.name "${GH_USER_NAME}"
  git config user.email "${GH_USER_EMAIL}"
  git remote set-url origin "https://${GH_TOKEN}@${GH_REF}"
  git fetch origin
)

# Commit and push the sphinx documentation to develop
(
  git add docs/drdown.pdf
  git commit -m "Rebuild sphinx documentation at ${rev} "
  git push origin develop
)

# Running mkdocs build to gh-pages
mkdocs build --clean
