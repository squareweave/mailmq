#!/bin/sh -xe

# Bring up MailDev and the Celery worker
docker-compose up -d

export CELERY_BROKER=localhost
export PHPRC=$(dirname $0)/php.ini

phpunit tests
