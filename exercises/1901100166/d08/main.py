from mymodule import stats_word  #从m文件中导入st模块

import traceback
import logging  #这是两种方法

logger=logging.getLogger(__name__)

def T():
    try:
        stats_word.stats_text(1)
    except Exception as e:
        print('T=>',e)
        print(traceback.format_exc())

def L():
    try:
        stats_word.stats_text(1)
    except Exception as e:
        # print('L=>',e)  
        logger.exception(e)

if __name__ == "__main__":
    stats_word.stats_text(1)
    T()
    L()
      