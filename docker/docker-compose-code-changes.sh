#!/bin/bash

# https://stackoverflow.com/questions/31466428/how-to-restart-a-single-container-with-docker-compose
# This will apply changes to the docker-compose.yaml and any container changes
docker-compose pull
docker-compose up -d --build

# or to rebuild one worker
docker-compose up -d --build worker


# Lifecycle
docker-compose stop worker
docker-compose rm worker 
docker-compose create worker
docker-compose start worker
