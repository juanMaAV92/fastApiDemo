#!/bin/bash
if [ "$ENV" = "production" ]
then
  cat .env.production
else
  cat .env.development
fi
