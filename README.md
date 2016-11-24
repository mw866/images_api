# CS 5356 Final Project
By Chris Wang (mw866@cornell.edu)

Description: An API based on Flask, Gunicorn and NGINX

Usage: <domain>/api/num_colors?src=<imageurl>

## Architecture
* DNS: TBD

* CDN: TBD

* Reverse Proxy & Load Balancer (x1 VM, 192.168.0.2): NGINX

* Web Server (x3 VM,  192.168.0.4-5): Gunicorn

* Web Framework: Flask

## Requirements
* https://docs.google.com/document/d/1oog1sbBdm-d6KSmLjhbHjAUD8XDtdojVWpyFNwk-Fj8/edit#heading=h.5ec0zrrtnk5v

## Reference
* Vagrant: https://www.vagrantup.com/docs/getting-started/

* ImageMagick with Python Example: https://github.com/jinpark/imageresizer

* ImageMagick Wand API Documentations: http://docs.wand-py.org/en/0.2.4/index.html

* Flask Applications with Gunicorn and Nginx on Ubuntu 16.04: https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-16-04

* Gunicorn config: http://docs.gunicorn.org/en/stable/settings.html#server-socket

 *Gunicorn accept Nginx forwarding: http://docs.gunicorn.org/en/stable/deploy.html

* UFW config: https://help.ubuntu.com/community/UFW

* NGINX Load Balancing config: https://www.nginx.com/resources/admin-guide/load-balancer/

* Vagrant Network config: 
https://www.safaribooksonline.com/library/view/vagrant-up-and/9781449336103/ch04.html
https://www.vagrantup.com/docs/virtualbox/networking.html

* VirtualBox Internal Network: https://www.virtualbox.org/manual/ch06.html#network_internal

* Flask Logging: http://flask.pocoo.org/docs/0.11/errorhandling/

## Troubleshooting Nginx

* Writing the NGINX Debugging Log to a File: https://www.nginx.com/resources/admin-guide/debug/#error_log_file

* Test new NGINX config: $sudo nginx -t && sudo service nginx restart

* See log in real time: $tail -f file-name.log

## Troubleshooting Gunicorn

* ImportError: No module named wsgi: Run within /vagrant/

* Does not receive from NGINX: --bind 0.0.0.0:8000 

## Troubleshooting Vagrant/Linux
* Network testing: Vagrant by default creates multiple interfaces, hence use ping -I <specific hostonly/private interface> to avoid confusion.

* Network interface config: /etc/network/interfaces

* .1 address cannot be used because of conflicts with host machine's vboxnet1 interface

# Parameters can be tuned
Gunicorn: --worker 3
Python Requests: requests.get(timeout = 0.01)

## Test Results
$siege --time=1M --concurrent=3 -b -i --user-agent="Magic Browser" http://192.168.0.2/api/num_colors?src=https://www.wikipedia.org/portal/wikipedia.org/assets/img/Wikipedia-logo-v2@2x.png 

###Local: 1xWebserver Gunicorn --workers 3 
Transactions:		         406 hits
Availability:		      100.00 %
Elapsed time:		       59.34 secs
Data transferred:	        0.00 MB
Response time:		        0.44 secs
Transaction rate:	        6.84 trans/sec
Throughput:		        0.00 MB/sec
Concurrency:		        2.99
Successful transactions:         406
Failed transactions:	           0
Longest transaction:	        0.74
Shortest transaction:	        0.30
 
###Local: 1xWebserver Gunicorn --workers 4 
Transactions:		         417 hits
Availability:		      100.00 %
Elapsed time:		       59.30 secs
Data transferred:	        0.00 MB
Response time:		        0.42 secs
Transaction rate:	        7.03 trans/sec
Throughput:		        0.00 MB/sec
Concurrency:		        2.99
Successful transactions:         417
Failed transactions:	           0
Longest transaction:	        0.69
Shortest transaction:	        0.30

###Local: 1xWebserver Gunicorn --workers 3 after turned on caching
Transactions:		        1169 hits
Availability:		      100.00 %
Elapsed time:		       59.79 secs
Data transferred:	        0.00 MB
Response time:		        0.15 secs
Transaction rate:	       19.55 trans/sec
Throughput:		        0.00 MB/sec
Concurrency:		        2.99
Successful transactions:        1169
Failed transactions:	           0
Longest transaction:	        0.33
Shortest transaction:	        0.11

## Reference Results
### EC2 instance $siege --time 10s https://s3.amazonaws.com/startup-systems-final-images/6461517483.jpg
Transactions:		          82 hits
Availability:		      100.00 %
Elapsed time:		        9.32 secs
Data transferred:	        9.49 MB
Response time:		        0.91 secs
Transaction rate:	        8.80 trans/sec
Throughput:		        1.02 MB/sec
Concurrency:		        8.03
Successful transactions:          82
Failed transactions:	           0
Longest transaction:	        1.28
Shortest transaction:	        0.69

