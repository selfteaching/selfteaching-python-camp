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
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
红酥手，黄藤酒，满城春色宫墙柳。等闲识得东风面，万紫千红总是春。
'''


#使用字典统计
def stats_text_en(text):
    text=text.replace(',',' ').replace('.',' ').replace('--','').replace('!','').replace('*',' ')#将非英文字符替换为空格
    text=text.lower()#将所有英文字符改为小写
    text=text.split()#以空格拆分为独立的单词
    zidian={}
    for i in text:  #将字符转换为字典
        count=text.count(i)
        r1={i:count}
        zidian.update(r1)
        #print(i,'',count)
    print(zidian)
        
    zidian1=sorted(zidian.items(),key=lambda x:x[1],reverse=True) #按照单词出现次数，从小到大排序
    print(zidian1)


import re
#统计中文单词
def stats_text_cn(text):      
    result1 = re.findall(u'[\u4e00-\u9fff]+', text)
    newString = ''.join(result1)
    b ={}
    for i in result1:
        b.update({i:newString.count(i)})
    b1 = sorted(b.items(),key = lambda x:x[1],reverse= True)
    print('the result of counting chinese words ', b1, '\n')


stats_text_en(text1)
stats_text_cn(text1)        







