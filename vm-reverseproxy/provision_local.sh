#!/bin/bash
set -e
set -x

echo "Provisioning Reverse Proxy from local!"


aws ec2 run-instances --image-id ami-a9d276c9 --count 1 --instance-type t2.micro --key-name aws_time --security-group-ids sg-ac1b34d5 --subnet-id subnet-f686f5ae --monitoring Enabled=True --private-ip-address 192.168.0.100 --associate-public-ip-address #--dry-run

# i-xxxxxxxx comes from the previous command
# aws ec2 create-tags --resources i-xxxxxxxx  --tags Key=Name,Value=reverseproxy --tags Key=Project,Value=one_and_done 