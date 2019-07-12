#text文本文件
text = False

from mymodule import stats_word

try : 
    print('合并词频统计结果： ', stats_word.stats_text(text))
except ValueError as modify :
    print(modify)