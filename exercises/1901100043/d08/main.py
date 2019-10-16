
from mymodule import stats_word
import traceback
import logging
# logger 报错

def text_traceback():
    try:
        stats_word.stats_tex(666)
    except Exception as e:
        print('text_traceback =>',e)
        print(traceback.format_exc())

if __name__ == "__main__":
    stats_word.stats_tex(999)
    text_traceback()

'''
练习感受：
1）学会用  
raise  ValueError  抛出异常
try:    except  Exception:  捕获异常

2）中英文过滤
isascii  来判断是英文
'\u4e00' <= character <= '\u9fff'  来判断是中文

3）logger.exception(e) 报错

4）最近重读了一边《自学是门手艺》
   把基础概念重新练习了一边
   感受：耐心，反复练习，反复归纳总结。
'''
