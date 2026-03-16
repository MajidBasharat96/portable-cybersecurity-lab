#!/bin/bash

echo "Stopping Cybersecurity Lab..."

docker-compose -f configs/docker-compose.yml down
