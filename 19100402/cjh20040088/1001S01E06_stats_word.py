text0='''
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
There should be one -- and preferably only one -- obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

text0=text0.replace(',','').replace('.','').replace('--','').replace('!','').replace('*','')
text=text0.split(" ")
def stats_text_en(text):   #英文词频统计
    b={}
    for i in text:
        b[i]=text.count(i)
    return b

result=sorted(stats_text_en(text).items(),key=lambda x:x[1],reverse=True)
print(result)


text1='''中国位于东亚，
是以华夏文明为主体，
中华文化为基础，
以汉族为主要民族的统一多民族国家，
通用汉语，
中国人一般称呼自己为龙的传人、
炎黄子孙或中华民族。
'''

text1=text1.replace('，','').replace('、','').replace('。','')
def stats_text_cn(text):     #中文词频统计
    c={}
    for i in text1:
        u'\u4e00'<=i<=u'\u9fff'
        c[i]=text1.count(i)
    return c

result1=sorted(stats_text_cn(text).items(),key=lambda x:x[1],reverse=True)
print(result1)