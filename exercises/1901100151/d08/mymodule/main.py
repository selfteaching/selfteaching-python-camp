from stats_word import *
import traceback
import logging

logger = logging.getLogger(__name__)
# Error:
# getlogger与getLogger的区分

def test_traceback():
    try:
        stats_text(1)
    except Exception as e:
        print("test_traceback =>", e)
        print(traceback.format_exc())

def test_logger():
    try:
        stats_text(1)
    except Exception as e:
        # print("test_traceback =>", e)
        logger.exception(e)

if __name__ == "__main__":
    stats_text(1)
    test_traceback()
    test_logger()
