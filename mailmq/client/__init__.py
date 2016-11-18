"""
mailmq sendmail shim
"""


import sys
import argparse
import email

from ..server import sendmail


def main():
    """Main entrypoint."""
    parser = argparse.ArgumentParser(description="Send an email via Celery/MQ.")
    parser.add_argument('-r', dest='sender', type=str,
                        help="Set the envelope sender address.")
    parser.add_argument('-t', dest='extract_recipients', action='store_true',
                        help="Extract recipients.")
    parser.add_argument(dest='to_addr', type=str, nargs='*',
                        help="destination address(es)")

    args = parser.parse_args()
    body = sys.stdin.read()

    message = email.message_from_string(body)
    _, mail_from = email.utils.parseaddr(message.get('from'))

    rcpt_to = args.to_addr

    if args.extract_recipients:
        rcpt_to += [
            address
            for _, address in email.utils.getaddresses(
                message.get_all('to', []) +
                message.get_all('cc', []) +
                message.get_all('resent-to', []) +
                message.get_all('resent-cc', []))
        ]

    assert rcpt_to, "Need some recipients!"

    sendmail.delay(sender=args.sender or mail_from,
                   to=rcpt_to,
                   body=body)
