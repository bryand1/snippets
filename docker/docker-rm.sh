#!/bin/bash

# Remove exited containers
docker rm $(docker ps -a -q -f'status=exited')
