text = '''
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
Python是一种计算机程序设计语言。是一种动态的、面向对象的脚本语言，最初被设计用于编写自动化脚本(shell)，随着版本的不断更新和语言新功能的添加，越来越多被用于独立的、大型项目的开发。
'''

import collections
from collections import Counter
count = int()
def stats_text_en(text,count):
    import re
    text_en = re.sub("[^A-Za-z]", " ", text.strip())
    list_en = text_en.split()
    return collections.Counter(list_en).most_common(count)
def stats_text_cn(text,count):
    import re
    import jieba
    text_cn = re.findall(u'[\u4e00-\u9fff]+', text.strip())
    str_cn = ''.join(text_cn)
    seg_list=jieba.cut(str_cn)
    jielist=[]
    for i in seg_list:
        if len(i)>=2:
            jielist.append(i)
        else:
            
           return collections.Counter(jielist).most_common(count)
def stats_text(text,count):
    return collections.Counter(stats_text_en(text,count)+stats_text_cn(text,count)).most_common(count)





    



