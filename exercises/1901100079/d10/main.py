from mymodule import stats_word
import logging
from os import path
filepath=path.join(path.dirname(path.abspath(__file__)),'tang300.json')
'''print(filepath)'''
with open(filepath,'r',encoding='utf-8') as t:
    p=t.read()

logger=logging.getLogger(__name__)

def test_logger():
    try:
        a=stats_word.stats_text_cn(p,20)
        print(a)
    except Exception as i:
        logger.exception(i)
    
if __name__=='__main__':
    test_logger()           