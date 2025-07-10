#!/bin/bash

# Check if the .env file exists.
if [ ! -f .env ]; then
  echo "CRITICAL: Environment file .env not found. Creating a template."
  touch .env
  exit 1
fi
if [ ! -f frontend/.env ]; then
  echo "INFO: Creating .env file for frontend."
fi

# Check if any Docker containers are running. If they are, stop them.
if [ `docker compose ps | egrep "^IMAGE" | wc -l | tr -d ' '` -gt 0 ]; then
  echo "WARNING: Found containers running. Stopping them."
  docker compose down
fi


# Build the Docker images.
echo
echo "INFO: Building docker images and starting services."
docker compose down
docker compose build --no-cache
docker compose down
docker compose up -d
docker compose logs -f
