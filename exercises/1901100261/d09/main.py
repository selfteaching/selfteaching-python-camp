# 通过模块导入 stats_word,调用 stats_text 统计字符串样本中中文汉子和英文单词出现的次数
from mymodule import stats_word 
import json
import traceback  # 调用 traceback (捕获错误的模块)
import logging    #调用 logging 

with open('/Users/Asha/Documents/GitHub/selfteaching-python-camp/exercises/1901100261/d09/tang300.json',encoding='UTF-8') as f:
    read_date = f.read()
print('中文词频统计==>',stats_word.stats_text_cn(read_date,100))

logger = logging.getLogger(__name__)

def test_tracebake():
    try:
        stats_word.stats_text_cn(read_date,100)  
    except Exception as e :
        print('test_traceback==>',e)   
        print(traceback.format_exc())

def test_logger():
    try:
        stats_word.stats_text_cn(read_date,100)
    except Exception as e:
        # print('test_logger==>',e)
        logger.exception(e)

if __name__ == "__main__":
    # stats_word.stats_text(1)   # 如果加上这一行，没有检测到错误，后面就不会运行
    test_tracebake()     # 封装函数
    test_logger()

