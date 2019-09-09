text = 123

from mymodule import stats_word
import traceback
import logging
logger = logging.getLogger(__name__)

try:
    print('中英文字频====>', stats_word.stats_text(text))
except ValueError as err:
    print("print out the error: ", err)
    print(traceback.format_exc())

def test_logger():
    try:
        stats_word.stats_text(1)
    except Exception as e:
        logger.exception(e)

if __name__ == '__main__':
    test_logger()
