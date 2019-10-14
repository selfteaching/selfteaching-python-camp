import jieba
import json
from collections import Counter
######################   2.输出中文函数
def stats_text_cn(text):

    seg_list =[]
    #seg_list = ",".join(jieba.cut(text,cut_all = False))  #精确模式
    words = jieba.cut(text,cut_all=False)

        
    for word in words:
        seg_list.append(word)

   
    symbols = ',  :{}，.。：*\!'    ##########汉字拼写下的“，”与拼音状态下的“,”不同
    for symbol in symbols:
        if symbol in seg_list:
            seg_list.remove(symbol)

    for word in seg_list:
        if len(word) <= 1:
            seg_list.remove(word)

    
   
    cnt = Counter()
    for word in seg_list:
        cnt[word] += 1
    
    print(cnt.most_common(20))
##############   4.读取tang300

with open('c:/Users/sddl/Documents/GitHub/selfteaching-python-camp/exercises/1901100303/d09/mymodule/tang300.json',encoding='utf-8') as ff:
    read_data = json.loads(ff.read())


poems = ''
for item in read_data:
    poems += item.get('contents','')


print(stats_text_cn(poems))
