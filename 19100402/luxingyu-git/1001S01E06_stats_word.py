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
'''
text_0=text.replace('--','').replace(',','').replace('.','').replace('*','').replace('!','')
def stats_text_en(text_0):   #英文词频统计
    counten={}
    for x in text_0:
        if x in text_0:
           counten[x]=text_0.count(x)+1   
        else:
           counten[x]=text_0.count(x)     #如果字典里有这个单词+1，如果没有这个词就算第1个
    return counten
print(sorted(stats_text_en(text_0.split()).items(),key=lambda i:i[1],reverse=True))

print()
text_1= '黑化黑灰化肥灰会挥发发灰黑讳为黑灰花会回飞，灰化灰黑化肥灰会挥发发黑灰为讳飞花回化为灰。'

text_2=text_1.replace('，','').replace('。','')
def stats_text_cn(text_2):   #中文词频统计
    countcn={}
    for i in text_2:
        if u'\u4e00'<=i<=u'\u9fff':
            countcn[i]=text_2.count(i)+1
        else:
            countcn[i]=text_2.count(i)
    return countcn
print(sorted(stats_text_cn(text_2).items(),key=lambda i:i[1],reverse=True))
