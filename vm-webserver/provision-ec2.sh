#!/bin/bash

# [Prerequisite] Run the folling before executing this shell script
# cd ./vm-webserver/
# sudo -s
# cd ~
# git clone https://github.com/mw866/one-and-done.git
# 

set -e
set -x

echo "Provisioning starts!"

sudo echo "webserver" > /etc/hostname
sudo apt-get update
sudo apt-get install -y python-pip  python-dev imagemagick lynx
sudo pip install --upgrade pip
sudo pip install -r requirements.txt

#For debugging locallly:
# export FLASK_APP=one_and_done.py
# export FLASK_DEBUG=1
# flask run --host=0.0.0.0 --port=80

#Config Gunicorn:
sudo cp ./one_and_done.service /etc/systemd/system/ #ln -s will not work
sudo systemctl start one_and_done.service
sudo systemctl enable one_and_done.service

sudo mkdir /var/log/gunicorn

echo "Provisioning complete!"
