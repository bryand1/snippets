#!/bin/bash
# https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-16-04

sudo apt-get update
sudo apt-get install mysql-server

mysql_secure_installation

# Regardless of how you installed it, MySQL should have started running automatically. To test this, check its status.

# systemctl status mysql.service