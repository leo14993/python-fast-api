#!/bin/bash

# upgrade system dependency
apt-get update -y
# install any needed packages
apt-get install -y redis-server
apt-get install -y libaio1
apt-get install -y libaio-dev
apt-get install -y libgomp1
# upgrade python dependency
pip install --upgrade pip setuptools wheel
# install any needed packages specified in requirements.txt
pip install -r requirements.txt

apt-get autoremove -y