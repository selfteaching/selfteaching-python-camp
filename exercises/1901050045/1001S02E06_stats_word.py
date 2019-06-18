

def stats_text_en(text):#定义函数，其中text是可变的量
    text = text.replace(',',' ').replace('.',' ').replace('\'','').replace('-',' ').replace('!',' ').replace('*',' ')
        #去标点符号也可用这样的语句
#h=text.split()
#for i in text: 
#   if i.isalpha():
#       h.append(i)
    text=text.split()   #列表化字符串
    seta=set(text)      #取集合
    b=[]                #定义b列表
    for i in seta:
        count=text.count(i)                             #统计i在列表text中出现的次数
        a=(i,count)
        b.append(a)                                     #将a添加到列表b             
    b=sorted(b,key=lambda kv:kv[1], reverse=True)       #按照数字大小降序排列
    b=dict(b)                                           #将b设置成为词典
    print(b)

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
'''#给text设定一个值
stats_text_en(text)#运行函数

#=================================================================任务2================================================================

def stats_text_cn(text):
        text = text.replace(',',' ').replace('.',' ').replace('\'','').replace('-',' ').replace('!',' ').replace('*',' ')#去标点符号
        setb=set(text)                                 #设定集合
        x=[]                                            #设定x列表
        for o in setb:                                  #o从集合setb中取
                if o >= u'\u4e00' and o <= u'\u9fa5':#如果o是在u4e00 到u9fa5之间（汉字）
                        count=text.count(o)#统计每个汉字的数量
                        y=(o,count)
                        x.append(y)#将y加到x列表中
        x=sorted(x,key=lambda kv:kv[1],reverse=True)#按重复次数，由大到小排列
        print(x)


text='''The Zen of Python, by Tim Peters
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
青葡萄，紫葡萄，青葡萄没紫葡萄紫，吃葡萄不吐葡萄皮，不吃葡萄倒吐葡萄皮
'''
stats_text_cn(text)




