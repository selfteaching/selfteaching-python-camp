from mymodule import stats_word
import traceback
import logging

logger=logging.getLogger(__name__)

def test1():
    try:
        stats_word.stats_text(1)
    except Exception as e:
        print('test1:',e)
        print(traceback.format_exc())

def test2():
    try:
        stats_word.stats_text(1)
    except Exception as e:
        print('test2:',e)
        logger.exception(e)

if __name__=='__main__':
    stats_word.stats_text(1)
    test1()
    test2()