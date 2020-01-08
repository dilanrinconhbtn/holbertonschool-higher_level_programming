#!/bin/bash
# URL passed as an argument, and displays only the status code of the response.
curl -sL -w "%{http_code}" -I "$1" -o /
