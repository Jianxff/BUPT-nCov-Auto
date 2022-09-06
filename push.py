import os
from pypushdeer import PushDeer
from base import logging

def push(msg):

    key = os.environ.get('PUSHDEER','').strip()        # get key for pushdeer

    if len(key) == 0:
        logging.info('Invalid KEY')
        return

    try:
        pushdeer = PushDeer(pushkey=key)
        pushdeer.send_text('[BUPT-nCov] ' + msg)

    except Exception as e:
        logging.info(e)
            