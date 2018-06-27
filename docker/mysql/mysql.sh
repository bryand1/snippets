#!/bin/bash

# Start MySQL service
docker-compose up -d

# Connect to MySQL using container
docker run -it --rm --net backend mysql:5.7 sh -c 'exec mysql -h"mysql" -P3306 -uroot -p"MYSQL_ROOT_PASSWORD"'

# Database files will be stored on local filesystem, per the bind mount in docker-compose.yml
