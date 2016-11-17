#!/bin/sh -xe

# Bring up MailDev and the Celery worker
docker-compose up -d

export CELERY_BROKER=localhost

php -d 'sendmail_path="python -m mailmq.client -t"' \
    -d allow_url_fopen=On \
    -d detect_unicode=Off \
    phpunit-5.6.2.phar \
    tests
