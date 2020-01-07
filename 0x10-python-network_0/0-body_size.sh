#!/usr/bin/env bash
# Displays the size of the body of the response
sudo touch  size_body
curl -so /dev/null "$1" -w '%{size_download}' > size_body
echo "" >> size_body
cat size_body
