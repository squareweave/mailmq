import os
import smtplib

from celery import Celery
from celery.utils.log import get_task_logger


LOGGER = get_task_logger(__name__)
app = Celery(broker=os.environ['CELERY_BROKER'])


@app.task(autoretry_for=(smtplib.SMTPException,))
def sendmail(sender=None,
             to=None,
             body=None):
    """
    Send email.
    """

    try:
        assert isinstance(to, list)
        assert to

        sender = sender or os.environ['MAIL_FROM']

        with smtplib.SMTP(host=os.environ['SMTP_HOST'],
                        port=os.environ.get('SMTP_PORT', 25)) as server:
            if 'SMTP_USER' in os.environ:
                server.login(os.environ['SMTP_USER'], os.environ['SMTP_PASS'])

            LOGGER.info("Sending email from %s -> %s", sender, to)
            server.sendmail(sender, to, body)
            LOGGER.info("Done")
    except:
        LOGGER.exception("Failed to send email!")
        raise
