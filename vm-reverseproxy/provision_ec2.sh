#!/bin/bash

# [Prerequisite] Run the folling before executing this shell script
# cd ./vm-reverseproxy/
# sudo -s
# cd ~
# git clone https://github.com/mw866/one-and-done.git

set -e
set -x

echo "Provisioning Reverse Proxy on EC2!"

sudo apt-get update
sudo apt-get install -y nginx lynx 

#Config NGINX:
sudo cd ~/one-and-done/vm-reverseproxy
sudo ln -s "~/one_and_done" /etc/nginx/sites-available/
sudo ln -s "~/one_and_done" /etc/nginx/sites-enabled/
sudo systemctl restart nginx


echo "Provisioning complete!"