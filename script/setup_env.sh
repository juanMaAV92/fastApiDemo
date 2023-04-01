#!/bin/bash

if [ "$1" == 'production' ]; then
    cat .env.production
elif [ "$1" == 'development' ]; then
    cat .env.development
else
    exit 1
fi

# se debe dar permisos de ejecucion
# chmod +x setup_env.sh    