#!/bin/bash

set -e
set -x

echo "Provisioning starts!"
apt-get update
apt-get install -y git python-pip nginx
# apt-get install python-dev 
pip install --upgrade pip
pip install gunicorn flask
#git config --global push.default simple
export FLASK_APP=hello.py
flask run 
#If run locallly: flask run --host=0.0.0.0 


echo "Provisioning complete!"