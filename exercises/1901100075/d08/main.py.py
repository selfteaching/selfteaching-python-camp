from mymodule import stats_word
import traceback
import logging 

logger=logging.getLogger(__name__)#__name__是日志记录的用例名，不是文件

def text_traceback():
    try:
        stats_word.stats_text(1)
    except Exception as e:#这里的e是前面MyError类的一个instance，我们可以直接访问他的value，也就是e.value
        print(e)
        print(traceback.format_exc())


def text_logger():
    try :
        stats_word.stats_text(1)
    except Exception as e:
        logger.exception(e)

if __name__ == '__main__':
    #stats_word.stat_text
    text_traceback()
    text_logger()

        
    




