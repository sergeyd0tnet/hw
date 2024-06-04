#!/bin/bash

PORT=80
IP=127.0.0.1
FILE=/var/www/html/index.nginx-debian.html

if nc -z $IP $PORT && [ -f $FILE ]; then
    exit 0
else
    exit 1
fi