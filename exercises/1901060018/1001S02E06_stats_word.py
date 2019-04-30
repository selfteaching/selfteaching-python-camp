text='''
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

乡愁      余光中
小时候，
乡愁是一枚小小的邮票，
我在这头，
母亲在那头。
长大后，
乡愁是一张窄窄的船票，
我在这头，
新娘在那头。
后来啊，
乡愁是一方矮矮的坟墓，
我在外头，
母亲在里头。
而现在，
乡愁是一湾浅浅的海峡，
我在这头，
大陆在那头。
'''

import re
fuhao=",.!-*&，。" #去除字符串中所有单词和汉字的符号
for str in fuhao:
    text=text.replace(str,'')
print(text)

#创建一个名为stats_text_en的函数
#使用字典（dicict）统计字符串样本text中各个单词出现的次数

def stats_text_en(text):
#    统计单词次数.
#    使用字典（dict）统计text中每个英文单词出现的次数.
    result=re.sub("[^A-Za-z]"," ",text.strip())
    dic={}
    for x in result.split():
        if not x in dic:
            dic[x]=1
        else:
            dic[x]=dic[x]+1
    return dic
frequency = stats_text_en(text)
print('**********************************************')
print("按照出现次数从大到小输出所有的单词及出现的次数")
print('**********************************************')
print(sorted(frequency.items(),key=lambda frequency:frequency[1],reverse=True))
#创建一个名为stats_text_cn的函数
def stats_text_cn(text):
    #统计汉字次数
    #使用字典（dict)统计text中每个汉字出现的次数
    dictionary={} #引用一个空字典
    for i in text:
        if u'\u4e00' <= i <= u'\u9fa5': #提取中文汉字 \u是unincode编码，u4e00是十进制表达式
            dictionary[i]=text.count(i)
    return dictionary
frequency = stats_text_cn(text)
print('**********************************************')
print("按照出现次数从大到小输出所有的汉字及出现的次数")
print('**********************************************')
print(sorted(frequency.items(), key=lambda frequency: frequency[1],reverse=True))

