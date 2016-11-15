import os
import email
import smtplib

from celery import Celery


app = Celery(__name__, broker=os.environ['CELERY_BROKER'])


@app.task
def sendmail(to=None,
             cc=None,
             bcc=None,
             subject=None,
             body=None):
    """
    Send email.
    """

    message = email.message_from_string(body)
    message['To'] = ', '.join(to or [])
    message['From'] = os.environ.get('MAIL_FROM', 'no-reply@localhost')

    if cc is not None:
        message['Cc'] = ', '.join(cc)

    if bcc is not None:
        message['Bcc'] = ', '.join(bcc)

    if subject is not None:
        message['Subject'] = subject

    with smtplib.SMTP(host=os.environ['SMTP_HOST'],
                      port=os.environ.get('SMTP_PORT', 25)) as server:
        server.send_message(message)
