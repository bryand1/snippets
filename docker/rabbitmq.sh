#!/bin/bash

# Start RabbitMQ with management plugin
docker run -d --hostname my-rabbit \
  --name my-rabbit \
  --net rabbitmq-net \
  -p 5672:5672 \
  -p 15672:15672 \
  -e RABBITMQ_ERLANG_COOKIE='YOUR_SECRET' \
  -e RABBITMQ_DEFAULT_USER='YOUR_USER' \
  -e RABBITMQ_DEFAULT_PASS='YOUR_PASSWORD' \
  -e RABBITMQ_DEFAULT_VHOST='YOUR_VHOST' \
  rabbitmq:3.7-management

# Access the management interface on localhost:15762 in browser

# Use rabbitmqctl
docker run -it --rm --net rmqnet -e RABBITMQ_ERLANG_COOKIE='YOUR_SECRET' rabbitmq:3.7 bash

# root@0e181c083f1b:/# rabbitmqctl -n rabbit@my-rabbit list_users

# > Listing users ...
# > newsworthy   [administrator]
