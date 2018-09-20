#!/bin/bash

# https://stackoverflow.com/questions/41897077/connect-to-mysql-on-localhost-from-docker-container

# Exposed ports are ignored when using the host network
docker run --name container --net host container