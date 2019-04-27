from mymodule import stats_word #从mymodule中导入stats_word
from collections import Counter
import re #调取re函数
import os #调取os函数
import jieba
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tang300.json'), encoding = 'UTF-8') as f:
    #绝对路径调取唐诗三百首
    read_date = f.read()
    t1=re.findall(r'[\u4e00-\u9fa5]',read_date)#提取中文字符
    seg_list1 = jieba.cut(''.join(t1), cut_all=False)#将t1转换字符串再进行jieba
    cn1 = []#定义一个空列表
    for i in seg_list1:#遍历老列表
        if len(i)>=2:#将字符串长度大于等于2的字符筛选出来
            cn1.append(i)#生成新列表
    mydict = Counter(cn1).most_common(20)#统计出现频次前100的字符
print (mydict)
try:
    stats_word.stats_text(read_date)
except ValueError:
    print('Input is not str. try again')
