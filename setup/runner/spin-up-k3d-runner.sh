#!/bin/bash

current_cluster=$(kubectl config current-context)

read -p "???> Do you want to spin up Release Runner on your cluster (current cluster context is $current_cluster)? (Y/n) " -n 1 -r
echo

if [[ $REPLY =~ ^[Nn]$ ]]; then
    exit 0
fi

echo
echo ":::> Waiting for Release token creation..."

MAX_WAIT_SECONDS=600
WAIT_INTERVAL=5

start_time=$(date +%s)
end_time=$((start_time + MAX_WAIT_SECONDS))

api_url="http://localhost:5516/api/v1/personal-access-tokens"
unique_id=$(date +%s%N | md5sum | awk '{print $1}')

RELEASE_RUNNER_TOKEN=""

while true; do
    current_time=$(date +%s)

    if [ $current_time -ge $end_time ]; then
        echo "!!!> Timeout reached. Exiting!"
        exit 1
    fi

    response=$(curl -s -i -X POST -u admin:admin -H "Content-Type: application/json;charset=UTF-8" -d '{"tokenNote": "'$unique_id'", "globalPermissions": ["runner#registration"]}' $api_url)

    if [ $? -ne 0 ]; then
        echo ":::> Fetching token failed - probably still initializing... retrying soon"
        sleep $WAIT_INTERVAL
        continue
    fi

    http_status=$(echo "$response" | awk 'NR==1{print $2}')
    response_body=$(echo "$response" | sed -n '/^\r\{0,1\}$/,$p')
    if [ $http_status -ge 200 ] && [ $http_status -lt 300 ]; then
        echo ":::> Successful fetched token..."
        RELEASE_RUNNER_TOKEN=$(echo "$response_body" | jq -r '.token')
        break
    else
        echo "!!!> Fetching token - response had $http_status HTTP status code."
        echo "!!!> Response body was: $response_body"
    fi

    echo ":::> Error fetching token! Waiting $WAIT_INTERVAL seconds before trying again..."
    sleep $WAIT_INTERVAL
done

if ! command -v helm &> /dev/null
then
    echo "!!!> Helm could not be found"
    read -p "???> Do you want to install Helm using brew? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]
    then
        echo ":::> Installing Helm using brew"
        brew install helm
    else
        echo "!!!> Helm is required to continue, skipping Release Runner setup"
        exit 1
    fi
fi

read -p "???> Enter version tag for Release Runner repositories to use (ENTER if default branch should be used): " RELEASE_RUNNER_VERSION_TAG
echo

if [ -z "$RELEASE_RUNNER_VERSION_TAG" ]; then
    echo ":::> RELEASE_RUNNER_VERSION_TAG is not set, using default branch"
fi

git clone git@github.com:digital-ai/release-runner.git
cd release-runner

if [ -z "$RELEASE_RUNNER_VERSION_TAG" ]; then
    echo ":::> RELEASE_RUNNER_VERSION_TAG is not set, using default branch"
else
  git checkout $RELEASE_RUNNER_VERSION_TAG
fi

echo ":::> Building Release Runner image"
. ./project.properties

docker build \
  --build-arg RELEASE_RUNNER_VERSION=0.0.42-demo \
  --tag "$REGISTRY_URL/$REGISTRY_ORG/$PROJECT_NAME:0.0.42-demo" .

echo ":::> Pushing Release Runner image to registry"
docker image push "$REGISTRY_URL/$REGISTRY_ORG/$PROJECT_NAME:0.0.42-demo"

cd ..
rm -rf release-runner

echo ":::> Release Runner image pushed to registry"

echo ":::> Spinning up Remote Runner in ${current_cluster}"


git clone git@github.com:digital-ai/release-runner-helm-chart.git
cd release-runner-helm-chart

if [ -z "$RELEASE_RUNNER_VERSION_TAG" ]; then
    echo ":::> RELEASE_RUNNER_VERSION_TAG is not set, using default branch for helm"
else
  git checkout $RELEASE_RUNNER_VERSION_TAG
fi

echo ":::> Installing Remote Runner Helm chart"
helm dependency build

helm install demo-remote-runner . -n runner --create-namespace \
    --set image.pullPolicy=Always \
    --set image.registry=$REGISTRY_URL \
    --set image.repository=$REGISTRY_ORG \
    --set image.tag=0.0.42-demo \
    --set release.registrationToken=$RELEASE_RUNNER_TOKEN \
    --set release.url="http://host.k3d.internal:5516"

echo ":::> Remote Runner Helm chart installed"

cd ..
rm -rf release-runner-helm-chart

echo ":::> Waiting for Remote Runner pod 'demo-remote-runner' to be ready"
kubectl wait --for=condition=Ready pod/demo-remote-runner-0 -n runner --timeout=300s

echo ":::> Remote Runner installed in ${current_cluster}"




