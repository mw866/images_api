#!/bin/bash

# [Prerequisite] Run the folling before executing this shell script
# cd ./vm-reverseproxy/
# sudo -s
# cd ~
# git clone https://github.com/mw866/one-and-done.git

set -e
set -x

echo "Provisioning Reverse Proxy on EC2!"

apt-get update
apt-get install -y nginx lynx 

#Config NGINX:
cd ./one-and-done/vm-reverseproxy
ln -s  "$(pwd)/one_and_done" /etc/nginx/sites-available/
ln -s "$(pwd)/one_and_done" /etc/nginx/sites-enabled/
systemctl restart nginx


echo "Provisioning complete!"