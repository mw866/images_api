#!/bin/bash

set -e
set -x

echo "Provisioning starts!"

apt-get update
apt-get install -y git python-pip nginx python-dev imagemagick libmagickwand-dev
pip install --upgrade pip
pip install -r /vagrant/requirements.txt

#For debugging locallly:
# export FLASK_APP=one_and_done.py
# export FLASK_DEBUG=1
# flask run --host=0.0.0.0 

#Config Gunicorn:
sudo cp /vagrant/one_and_done.service /etc/systemd/system/ #ln -s will not work
sudo systemctl start one_and_done.service
sudo systemctl enable one_and_done.service

#Config NGINX:
sudo ln -s /vagrant/one_and_done /etc/nginx/sites-available/
sudo ln -s /vagrant/one_and_done /etc/nginx/sites-enabled/
sudo systemctl restart nginx

echo "Provisioning complete!"