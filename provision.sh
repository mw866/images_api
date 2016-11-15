#!/bin/bash

set -e
set -x


echo "provisioning!"

# TODO your code here
apt-get update
apt-get install -y git python3-pip
git config --global push.default simple
pip3 install --upgrade pip
sudo apt-get -y install python3-pip python3-dev nginx
pip install gunicorn flask
python3 /vagrant/hello.py

echo "provisioning complete!"
