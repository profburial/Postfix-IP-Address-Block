#!/usr/bin/env bash

touch /etc/postfix/reject_client
python block.py 
sudo service postfix restart