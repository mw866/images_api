#!/bin/bash

set -e
set -x

echo "Provisioning starts!"
apt-get update
apt-get install -y git python-pip nginx libmagickwand-dev
#To delete: apt-get install python-dev 
pip install --upgrade pip
pip install -r requirements.txt
#To delete: git config --global push.default simple
export FLASK_APP=hello.py
#Add if debug locally: export FLASK_DEBUG=1
flask run #If debug locallly: flask run --host=0.0.0.0 

echo "Provisioning complete!"