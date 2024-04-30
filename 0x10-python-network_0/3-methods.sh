#!/bin/bash
# Displays all HTTP methods the server will accept.
curl -s -I "$1" | grep -i "Allow" | cut -d ' ' -f 2- | tr -d ','
