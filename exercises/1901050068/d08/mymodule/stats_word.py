test='''
The Zen of Python,by Tim Peters


Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases arent special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one -- obvious way to do it.
Although never is often better the *right* now.
Now is better than never.
If the implementation is hard to explain, its a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- lets do more of those!
惟有饮者留其名，古来圣贤皆寂寞。
陈王昔时宴平乐，斗酒十恣欢谑。
主人何为言少钱，径须沽取对君酌。
五花马，千金裘，呼儿将出换美酒，与尔同来万古愁。
'''

import re #调用正则表达式模块
          # re.sub(pattern, repl, string, count=0, flags=0)
def stats_text_en(test_en):  #定义函数
    if type(test)!=str:
        raise ValueError('input date is not string')
    m = test_en.replace(',','').replace('.','').replace(':','').replace(';','').replace('"','').replace('!','').replace('?','').replace('、','').replace('，','').replace('。','').replace('”','').replace('：','').replace('；','').replace('\n','').replace('！','').replace('？','').replace('/','').replace('*',' ').replace('--',' ')
    m = m.lower() #全英文单词小写
    m = re.sub("[^A-Za-z]", " ", m)   # 借用了这个正则表达式，这里保留了英文单词，^代表取出大小写a-z以外所有的字符串剔除
    m = m.split()
    n = {}
    for i in m:
        count = m.count(i)
        r1 = {i:count}
        n.update(r1)
    c = sorted(n.items(),key=lambda x:x[1],reverse=True)
    print('英文单词统计频率如下： \n',c)  #这里print()函数缩进就是封装进我定义的函数里面去了
    return c   
   

def stats_text_cn(test_cn):
    if type(test)!=str:
        raise ValueError('input date is not string')
        o = test_cn.replace(',','').replace('.','').replace(':','').replace(';','').replace('"','').replace('!','').replace('?','').replace('、','').replace('，','').replace('。','').replace('”','').replace('：','').replace('；','').replace('\n','').replace('！','').replace('？','').replace('/','').replace('*',' ').replace('--',' ').replace(' ','')
        o = re.sub("[A-Za-z0-9]", "",o) #借用了这个正则表达式，这里删除了英文单词，因为没有加上^
        p = {}
    for j in o:
           count = o.count(j)
           r2 = {j:count}
           p.update(r2)
    q = sorted(p.items(),key=lambda x:x[1],reverse=True)
    print('中文字统计频率如下： \n',q)
    return q 

 
#分别调用stats_text_en和stats_text_cn，输出合并词频统计结果

def stats_text(en_cn):
    '''中英文词频统计'''
    if type(test)!=str:
        raise ValueError('input date is not string')
    return(stats_text_cn(en_cn)),(stats_text_en(en_cn))
#stats_text(test)

