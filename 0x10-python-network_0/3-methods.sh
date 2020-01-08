#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept.
curl -si "$1" | grep Allow: | cut -d ":" -f 2 | sed -e 's/^.//'
