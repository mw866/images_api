# CS 5356 Final Project
By Chris Wang (mw866@cornell.edu)
An API based on Flask, Gunicorn and NGINX
<domain>/api/num_colors?src=<imageurl>

## Architecture
DNS: TBD
CDN: TBD
Reverse Proxy & Load Balancer (x1 VM): NGINX
Web Server (x3 VM): Gunicorn
Web Framework: Flask

## Requirements
* https://docs.google.com/document/d/1oog1sbBdm-d6KSmLjhbHjAUD8XDtdojVWpyFNwk-Fj8/edit#heading=h.5ec0zrrtnk5v

## Reference
* Vagrant: https://www.vagrantup.com/docs/getting-started/

* ImageMagick with Python Example: https://github.com/jinpark/imageresizer

* ImageMagick Wand API Documentations: http://docs.wand-py.org/en/0.2.4/index.html

* Flask Applications with Gunicorn and Nginx on Ubuntu 16.04: https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-16-04

* Gunicorn config: http://docs.gunicorn.org/en/stable/settings.html#server-socket

* UFW config: https://help.ubuntu.com/community/UFW

# NGINX Load Balancing: https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-load-balancing

## Debugging Nginx

* Writing the NGINX Debugging Log to a File: https://www.nginx.com/resources/admin-guide/debug/#error_log_file

* Test new NGINX config: $sudo nginx -t && sudo service nginx restart

* See log in real time: $tail -f file-name.log





commit before branching to split Reverse Proxy (NGINX) and App Server (Gunicorn).