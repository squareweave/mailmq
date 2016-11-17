MailMQ
======

`sendmail` like mail-relaying via MQ.

When working with PHP and transaction email services, there's the super useful
`ssmtp`, which works great, except that `ssmtp` is synchronous and if your
mail relay is slow, it will slow your entire web request down.

Enter `mailmq`, which does the same thing, but via a producer-consumer model.
You run an AMQP service, e.g. RabbitMQ, and a Celery worker that runs
`mailmq.server` and then you can use `mailmq.client` to send email
asynchronously.

The server is designed for Docker, so all configuration happens via the
environment.

Server
------

Via Docker:

```
docker-compose up
```

Or directly:

```
CELERY_BROKER=localhost SMTP_HOST=mail celery -A mailmq.server worker
```

The following environment variables are supported:

* `CELERY_BROKER` - AMQP broker (required)
* `SMTP_HOST` - destination SMTP server host (required)
* `SMTP_PORT` - destination SMTP server port
* `SMTP_USER` - user for SMTP auth
* `SMTP_PASS` - password for SMTP auth
* `MAIL_FROM` - default sender (strongly recommended)

Client
------

Designed to have the same command line arguments as `sendmail`.

From pip:

```
pip install mailmq
```

With source:

```
python setup.py install
```

```
CELERY_BROKER=amqp mailmq -t << EOF
From: badger@badger.com
To: badger@badger.com
Subject: badger

Badger!
EOF
```

Or without installing:

```
CELERY_BROKER=localhost python -m mailmq.client badger@example.com
```

The following environment variables are supported:

* `CELERY_BROKER` - AMQP broker (required)

Add the following to your `php.ini` to use with PHP:

```
sendmail_path = "mailmq -t"
```

License
-------

MIT license.

Copyright (c) 2016, Squareweave <hello@squareweave.com.au>

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
