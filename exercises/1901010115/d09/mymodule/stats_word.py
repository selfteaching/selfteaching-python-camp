import re
from collections import Counter
import json #测试用

text1 = '''
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
There should be one-- and preferably only one --obvious way to do
it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

def stats_text_en(t,count): #定义函数，参数为t
    if not isinstance(t,str): #如果t不是字符串
        raise ValueError('wrong operand type') #则报错
    else: #如果t是字符串
        t = t.lower() #文本转小写
        t_list = t.split() #文本转列表
        x = Counter() #设定一个空计数器
        for i in t_list: #指定i遍历上述列表
            ii = i.strip(' ,.*!-') #清洗i中元素
            x[ii] += 1 #计数清洗完的单词
        return x.most_common(count)#得单词计数结果（已自动排序）

text2 = '''
/“/请/！/”/“/请/！/”/两名/剑士/各自/倒转/剑尖/，/右手/握/剑柄/，
/左手/搭于/右手/手背/，/躬身行礼/。/两/人/身子/尚未/站/直/，
/突然/间/白光闪/动/，/跟着/铮的/一/声响/，
/双剑相/交/，/两/人/各/退一步/。
/旁/观众/人/都/是/“/咦/”/的/一声/轻呼/。/青衣/剑士/连/劈/三/剑/
'''

text3 = '''
二 结构化思维，几乎是最值得刻意训练的能力！
然而在现实中，很多人往往忽略结构化思维的培养，因为他们认为，这是天生的。他们要么觉得自己足够聪明所以不需要培养，要么觉得我天生不聪明，学不来，干脆放弃。
我曾经在文章中提到过能力的重要性。有人问，能力有那么多，到底培养哪一个才好呢？如果我用一个两维矩阵来分析的话，可以看到，结构化思维能力，是既能够被培养同时价值度又高的能力。
'''

def stats_text_cn(t,count): #定义函数，参数为t
    if not isinstance(t,str): #如果t不是字符串
        raise ValueError('wrong operand type') #则报错
    else: #如果t是字符串
        t_list = [] #新建一个空列表
        exclude_str = '\n ，。！？/”“「」:\',[]' #新建一个字符串,备用（将要消除的中文符号）
        y = Counter()
        for char in t: #遍历文本中的字节
            t_list.append(char) #把拆解的所有字节（包括单个汉字和符号）放入新建的列表中
        for char in t_list: #遍历列表中的元素
            if char not in exclude_str: #如果该字节为汉字，不是符号
                y[char.strip()] += 1
        return y.most_common(count)

with open('tang300.json',mode='r',encoding='utf-8') as f: #测试用
    read_data = f.read() #测试用

def stats_text(t,count):
    if not isinstance(t,str): #如果t不是字符串
        raise ValueError('wrong operand type') #则报错
    else: #如果t是字符串
        a = re.sub(r'[^A-Za-z]',' ',t)
        stats_text_en(a,count)
        b = [i for i in t if '\u4e00' <= i <= '\u9fa5']
        b = str(b) #这里再次把列表转化为字符串
        stats_text_cn(b,count)
        return (print(stats_text_en(a,count) + stats_text_cn(b,count)))


