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

```
CELERY_BROKER=localhost SMTP_HOST=mail celery -A mailmq.server worker
```

Client
------

Designed to have the same command line arguments as `mail`.

```
CELERY_BROKER=localhost python -m mailmq.client badger@example.com << EOF
badger
EOF
```

ToDo
----

* Authentication
* Tests (incl tests of PHP's `mail()`)

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
