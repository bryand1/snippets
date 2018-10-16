#!/bin/bash

# Remove dangling images
docker rmi $(docker images -q -f'dangling=true')
