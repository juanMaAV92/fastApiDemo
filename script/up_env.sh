#!/bin/sh
while read line; do export $line; done < .env

# printenv <name>
# chmod +x up_env.sh    