from mymodule import stats_word
from os import path
import json
import re
import logging

logging.basicConfig(format = 'file:%(filename)s|line:%(lineno)d|message:%(message)s',level = logging.DEBUG)

def load_file():
    
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
        print('test_traceback =>' , e)
        logger.exception(e)

if __name__ == "__main__":
    stats_word.stats_text(1)
    test_traceback()
    test_logger