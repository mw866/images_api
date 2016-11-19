#!/bin/bash

set -e
set -x

echo "Provisioning starts!"
apt-get update
apt-get install -y git python-pip python-virtualenv nginx
# apt-get install python-dev 
pip install --upgrade pip
pip install gunicorn flask
#git config --global push.default simple
#python /vagrant/hello.py

echo "Provisioning complete!"