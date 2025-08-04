#!/bin/sh
xl apply --verbose --detach --file /data/setup.yaml

# need these releases to happen sequentially or else connections will not be created in time
xl apply --verbose --file /data/setup-live-deployment.yaml