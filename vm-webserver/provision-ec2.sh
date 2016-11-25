#!/bin/bash

# Run the folling before executing this shell script
# cd ~
# git clone https://github.com/mw866/one-and-done.git

set -e
set -x

echo "Provisioning starts!"

sudo -s
apt-get update
apt-get install -y python-pip  python-dev imagemagick libmagickwand-dev lynx
pip install --upgrade pip

cd ~
git clone https://github.com/mw866/one-and-done.git
cd ./one-and-done/vm-reverseproxy
pip install -r requirements.txt

#For debugging locallly:
# export FLASK_APP=one_and_done.py
# export FLASK_DEBUG=1
# flask run --host=0.0.0.0 --port=80

#Config Gunicorn:
sudo cp ./one_and_done.service /etc/systemd/system/ #ln -s will not work
sudo systemctl start one_and_done.service
sudo systemctl enable one_and_done.service



echo "Provisioning complete!"