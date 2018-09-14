#!/bin/bash

# Install Python3.7 on Debian/Ubuntu
# https://stackoverflow.com/questions/27022373/python3-importerror-no-module-named-ctypes-when-using-value-from-module-mul

sudo apt-get update
sudo apt-get upgrade
sudo apt-get dist-upgrade
sudo apt-get install build-essential python-dev python-setuptools python-pip python-smbus
sudo apt-get install libncursesw5-dev libgdbm-dev libc6-dev
sudo apt-get install zlib1g-dev libsqlite3-dev tk-dev
sudo apt-get install libssl-dev openssl
sudo apt-get install libffi-dev

wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tar.xz
xz -d Python-3.7.0.tar.xz
tar -xvf Python-3.7.0.tar
cd Python-3.7.0

./configure --prefix=/usr/local
make
sudo make altinstall

