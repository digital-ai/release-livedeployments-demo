#!/bin/bash

echo "Populating registry with plugins"

repositories=(
  "git@github.com:digital-ai/release-fluxcd-integration.git"
  "git@github.com:digital-ai/release-argocd-integration.git"
  "git@github.com:digital-ai/release-xld-integration.git"
  "git@github.com:digital-ai/release-k8s-integration.git"
 )

echo ":::> Select repositories to use:"
echo "0) ALL"
for i in "${!repositories[@]}"; do
  echo "$((i+1))) ${repositories[$i]}"
done
echo "42) NONE"

read -p "???> Enter your choice (e.g., 0 for ALL, - for none of the plugins, 1 2 for specific repos, use space as delimiter): " -a choices
echo

if [ ${#choices[@]} -eq 0 ]; then
  echo "!!!> No selection made, exiting."
  exit 1
fi

selected_repos=()
if [ "${choices[0]}" -eq 0 ]; then
  selected_repos=("${repositories[@]}")
elif [ "${choices[0]}" -eq 42 ]; then
  echo ":::> No plugins selected, skipping plugin generation."
  exit 0
else
  for choice in "${choices[@]}"; do
    selected_repos+=("${repositories[$((choice-1))]}")
  done
fi

echo ":::> Selected repositories: ${selected_repos[@]}"

read -p "???> Do you want to upload plugin artefacts to Release instance? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]
then
  RELEASE_DEMO_PLUGIN_UPLOAD=true
fi
read -p "???> Enter version tag for plugin repositories to use (ENTER if default branch should be used): " RELEASE_DEMO_PLUGIN_VERSION_TAG
echo

for repo in "${selected_repos[@]}"
do
  git clone $repo
  cd $(basename $repo .git)

  if [ -z "$RELEASE_DEMO_PLUGIN_VERSION_TAG" ]; then
    echo ":::> RELEASE_DEMO_PLUGIN_VERSION_TAG is not set, skipping checkout, building from master"
  else
    git checkout $RELEASE_DEMO_PLUGIN_VERSION_TAG
  fi

  if [ -z "$RELEASE_DEMO_PLUGIN_UPLOAD" ]; then
    sh build.sh
  else
    sh build.sh --upload
  fi

  if [ $? -ne 0 ]; then
    echo "!!!> Failed to run build.sh for $repo"
    exit 1
  fi
  cd ..
  rm -rf $(basename $repo .git)
done
