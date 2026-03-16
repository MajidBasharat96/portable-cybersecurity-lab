
#!/bin/bash
echo "Stopping Portable Cybersecurity Lab..."
docker-compose -f docker/docker-compose.yml down
echo "Lab stopped."
