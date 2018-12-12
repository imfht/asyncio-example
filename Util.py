import logging
import re
import sys

import cchardet

TITLE_REGEXP = '<title>(.*?)</title>'


def get_title(html):
    try:
        return re.findall(re.compile(TITLE_REGEXP, re.IGNORECASE | re.MULTILINE), html)[0]
    except:
        return ""


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Here we define our formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    logHandler = logging.StreamHandler(sys.stdout)
    logHandler.setLevel(logging.DEBUG)
    # Here we set our logHandler's formatter
    logHandler.setFormatter(formatter)
    logger.addHandler(logHandler)
    return logger


def auto_decode(content):
    """
    auto decode from byte to str
    :param content: raw html response
    :return: str
    """
    things = cchardet.detect(content)
    return content.decode(things['encoding'])
