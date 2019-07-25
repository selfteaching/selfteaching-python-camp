text = list(range(10))

'''
from mymodule import stats_word
import traceback
def test_traceback():
    try:
        stats_word.stats_text(text)
    except Exception as i:
        print('错误类型',i)
        print(traceback.format_exc())
    else:
        a=stats_word.stats_text(text)
        print('统计的结果是：',a)
       
if __name__=='__main__':
    test_traceback()   
'''

from mymodule import stats_word
import logging
logger=logging.getLogger(__name__)

def test_logger():
    try:
        stats_word.stats_text(text)
    except Exception as i:
        logger.exception(i)
    else:
        a=stats_word.stats_text(text)
        print('统计的结果是：',a)

if __name__=='__main__':
    test_logger()           