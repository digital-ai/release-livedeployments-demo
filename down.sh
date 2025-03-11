docker compose -f docker-compose.yaml down

echo "Select where Release Runner was run:"
echo "1) Docker"
echo "2) Local K3d Cluster"
read -p "???> Enter your choice (1 or 2): " -n 1 -r
echo

if [[ $REPLY =~ ^[1]$ ]]; then
    docker compose -f docker-compose-runner.yaml down
    exit 0
else
    ./k3d/cluster/spin-down-cluster.sh
fi
