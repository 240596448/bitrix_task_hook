import logging
import sys
from const import LOGGING_LEVEL

def get():

    return logging.getLogger(logname())

def logname():
    return 'BITRIX'

logger = logging.getLogger(logname())

handler = logging.StreamHandler(stream=sys.stdout)
handler.setFormatter(logging.Formatter(fmt='[%(name)s-%(levelname)s:%(asctime)s] %(message)s'))
logger.addHandler(handler)

try:
    logger.setLevel(eval('logging.' + LOGGING_LEVEL))
except:
    logger.error("Error set log level = {LOGGING_LEVEL}")
