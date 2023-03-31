#!/bin/sh

export PYTHONPATH=$PWD

if [ "$1" == 'development' ]; then
    export $(cat .env.development | xargs)
    echo "We are in DEVELOPMENT mode"
elif [ "$1" == 'production' ]; then
    export $(cat .env.production | xargs)
    echo "We are in PRODUCTION mode"
else
    echo "invalid parameter"
    exit 1
fi

./script/load-env-file.sh > env.tmp
sudo docker-compose up -d


# se debe dar permisos de ejecucion
# chmod +x setup_env.sh    