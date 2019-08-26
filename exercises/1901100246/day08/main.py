from mymodule import stats_word
import traceback
import logging

logger = logging.getLogger(__name__)

def test_traceeback():
    try:
        stats_word.stats_text(1)
    except Exception as e:
        print('test_traceback =>', e)
        print(traceback.format_exc())
        
def test_logger():
    try:
        stats_word.stats_text(1)
    except Exception as e:
        logger.exception(e)

if __name__ == '__main__':
    stats_word.stats_text(1)
    test_traceeback()
    test_logger()


