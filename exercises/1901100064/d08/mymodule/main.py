import stats_word
import traceback
import logging

# 启动日志记录器
logger=logging.getLogger('__name__')

# 定义test_traceback()测试函数
def test_traceback():
    try:
        stats_word.stats_text(1)
    except Exception as e:
        print('test_traceback =>',e)
        print(traceback.format_exc())


def test_logger():
    try:
        stats_word.stats_text(2)
    except Exception as e:
        print('test_logger =>',e)
        logger.exception(e)



if __name__ =='__main__':
    test_traceback()
    test_logger()



