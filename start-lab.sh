#!/bin/bash

echo "Initializing Portable Cybersecurity Lab..."

docker-compose -f configs/docker-compose.yml up -d

echo "Lab running."

echo "DVWA -> http://localhost:8081"
echo "Juice Shop -> http://localhost:3000"
echo "Kibana Dashboard -> http://localhost:5601"
