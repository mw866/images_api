#!/bin/bash
set -e
set -x

echo "Provisioning Reverse Proxy on EC2!"

apt-get update
apt-get install -y nginx, lynx, git

#Config NGINX:
ln -s  "$(pwd)/one_and_done" /etc/nginx/sites-available/
ln -s "$(pwd)/one_and_done" /etc/nginx/sites-enabled/
systemctl restart nginx

echo "Provisioning complete!"