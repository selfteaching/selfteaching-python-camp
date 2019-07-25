text = list(range(10))

'''from mymodule import stats_word
a=stats_word.stats_text(text)
print('统计的结果是：',a)

from mymodule import stats_word
a=stats_word.stats_text_en(text)
b=stats_word.stats_text_cn(text)
print('英文单词和词频是:',a)
print('中文字和出现次数是:',b)'''

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