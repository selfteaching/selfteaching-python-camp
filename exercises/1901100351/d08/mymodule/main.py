# this is d8 exercise for erros and exceptions
# date: 2019.09.15;renew in 09.18
# author by: rtgong

import stats_word
import traceback
import logging

logger = logging.getLogger(__name__)

def test_traceback():
    try:
        stats_word.stats_text(1)
    except Exception as e:
        print('test_traceback =>',e)
        print(traceback.format_exc())

def test_logger():
    try:
        stats_word.stats_text(1)
    except Exception as e:
        logger.exception(e)

if __name__=="__main__":
    test_traceback()
    test_logger()


