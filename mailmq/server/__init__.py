import os
import logging
import smtplib

from celery import Celery


logging.basicConfig(level=logging.INFO)

LOGGER = logging.getLogger(__name__)
app = Celery(broker=os.environ['CELERY_BROKER'])


@app.task(autoretry_for=(smtplib.SMTPException,))
def sendmail(sender=None,
             to=None,
             body=None):
    """
    Send email.
    """

    assert isinstance(to, list)
    assert to

    sender = sender or os.environ['MAIL_FROM']

    with smtplib.SMTP(host=os.environ['SMTP_HOST'],
                      port=os.environ.get('SMTP_PORT', 25)) as server:
        LOGGER.info("Sending email from %s -> %s", sender, to)
        server.sendmail(sender, to, body)
        LOGGER.info("Done")
