#!/bin/bash

read -p "???> Do you want to use FluxCD with a GitHub repository? (Y/n) " -n 1 -r
echo

if [[ $REPLY =~ ^[Nn]$ ]]; then
    exit 0
fi

# check if fluxcd is installed
if ! command -v flux &> /dev/null
then
    echo "!!!> FluxCD could not be found"
    read -p "???> Do you want to install FluxCD using brew? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]
    then
        echo ":::> Installing FluxCD using brew"
        brew install fluxcd/tap/flux
    else
        echo "!!!> FluxCD is required to continue, skipping FluxCD GitHub repository setup"
        exit 1
    fi
fi


echo ":::> Setting up GitHub repository for FluxCD"

#check for GITHUB_USER if there is already in envs if not prompt for one
if [ -z "$GITHUB_USER" ]; then
    echo "!!!> GITHUB_USER is not set"
    read -p "???> Enter your GitHub username: " GITHUB_USER
else
    echo ":::> GITHUB_USER is set to $GITHUB_USER"
fi
if [ -z "$GITHUB_TOKEN" ]; then
    echo "!!!> GITHUB_TOKEN
    read -p "???> Enter your GitHub token: " GITHUB_TOKEN
else
    echo ":::> GITHUB_TOKEN is set
fi
read -p "???> Enter your FluxCD GitHub repository name: " GITHUB_REPO


echo ":::> Initializing $GITHUB_REPO up FluxCD in k3d cluster"
flux bootstrap github --owner=${GITHUB_USER} --repository=${GITHUB_REPO} --branch=main --personal --path=clusters/staging
