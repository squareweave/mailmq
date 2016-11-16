import sys
import argparse

from ..server import sendmail


parser = argparse.ArgumentParser(description="Send an email via Celery/MQ.")
parser.add_argument('-r', dest='sender', type=str,
                    help="Set the envelope sender address.")
parser.add_argument(dest='to_addr', type=str, nargs='+',
                    help="destination address(es)")

args = parser.parse_args()
body = sys.stdin.read()

sendmail.delay(sender=args.sender,
               to=args.to_addr,
               body=body)
