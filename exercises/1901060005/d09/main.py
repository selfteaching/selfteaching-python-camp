from mymodule import stats_word #从mymodule中导入stats_word
from collections import Counter
import re #调取re函数
import os #调取os函数
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tang300.json'), encoding = 'UTF-8') as f:
    #绝对路径调取唐诗三百首
    read_date = f.read()
    t1=re.findall(r'[\u4e00-\u9fa5]',read_date)#提取中文字符
    mydict = Counter(t1).most_common(100)#统计出现频次前100的字符
print (mydict)
try:
    stats_word.stats_text(read_date)
except ValueError:
    print('Input is not str. try again')
