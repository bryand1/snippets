#!/bin/bash

# start container if it does not already exist
container_name=my-rabbit
if [[ "1" == $(sudo docker ps -a --filter status=running | grep -c "${container_name}") ]]; then
  echo "${container_name} is running"
  exit 0
fi

if [[ "1" == $(sudo docker ps -a --filter status=exited | grep -c "${container_name}") ]]; then
  echo "${container_name} exited"
  sudo docker rm "${container_name}"
fi

cd "$(dirname "${BASH_SOURCE[0]}")"

sudo docker run -d --name "${container_name}" \
  --net rabbitmq-net \
  -p 5672:5672 \
  -p 15672:15672 \
  -e RABBITMQ_ERLANG_COOKIE='ERLANG_COOKIE' \
  -e RABBITMQ_DEFAULT_USER='RMQUSER' \
  -e RABBITMQ_DEFAULT_PASS='RMQPASS' \
  -e RABBITMQ_DEFAULT_VHOST='/myvhost' \
  rabbitmq:3.7-management
