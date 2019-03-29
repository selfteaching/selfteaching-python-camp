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
'''

d = {}
def stats_text_en(text):
    for x in text:
        if not x in d:
            d[x]=1
        else:
            d[x]=d[x]+1
    print(d)
    return(sorted(d,reverse=True))
stats_text_en(text);

_all_=['e']
class e:
    def stats_text_en(self):
        '''
        统计单词次数
        返回降序
        '''
        pass



import re
def stats_text_cn(text):
    
    
    Chc_sum = 0
    
    for line in text:
        Chc_sum+=len(re.findall(r'\\x..','%r'%line))/3
    
    print('文中含有%d个汉字'%Chc_sum)
    
    a = [Chc_sum]
    return a
stats_text_cn(text);

_all_=['f']
class f:
    def stats_text_cn(self):
        '''
        统计中文汉字字数
        '''
        pass