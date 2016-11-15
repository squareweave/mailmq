import sys
import argparse

from ..server import sendmail


def comma_separated_str(s):
    """Comma separated list of items."""
    return str(s).split(',')


parser = argparse.ArgumentParser(description="Send an email via Celery/MQ.")
parser.add_argument('-s', dest='subject', type=str, help="subject")
parser.add_argument('-c', dest='cc_addrs', type=comma_separated_str,
                    help="comma separated list of CC addresses.")
parser.add_argument('-b', dest='bcc_addrs', type=comma_separated_str,
                    help="comma separated list of BCC addresses.")
parser.add_argument(dest='to_addr', type=str, nargs='+',
                    help="destination address(es)")

args = parser.parse_args()
body = sys.stdin.read()

sendmail.delay(to=args.to_addr,
               cc=args.cc_addrs,
               subject=args.subject,
               body=body)
