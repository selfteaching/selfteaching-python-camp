#text = ''' The Zen of Python, by Tim Peters
#Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested. Sparse is better than dense. Readability counts. Special cases aren't special enough to break the rules. Although practicality beats purity. Errors should never pass silently. Unless explicitly silenced. In the face of ambxiguity, refuse the temptation to guess. There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch. Now is better than never. Although never is often better than *right* now. If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea -- let's do more of those! '''

# 使用“字典”统计以上文本中出现的单词次数，并把结果从大到小输出
def stats_text_en(text):   #定义函数，其中text是可变的量
    text = text.replace(',',' ').replace('.',' ').replace('--',' ').replace('*',' ').replace('!',' ') # 去标点
    text = text.lower() # 全部换成小写
    text = text.split() # 拆成字符串
    d = {} #定义字典
    for i in text:    #遍历文本text
        count = text.count(i) # 数单词i个数
        r1 = {i:count} # 定义字典r1，单词在前，词频在后
        d.update(r1) #上传r1到d中去
    d = sorted(d.items(),key=lambda x:x[1],reverse=True)    #最终字典d里面元素排序
    return d
    # sorted(iterable,*,key=None,reverse=False) lambda是个特殊的定义函数，后面的是定义的表现形式，留待以后研究，reverse=True是颠倒的意思
    #print('\n按照出现次数降序输出所有单词:\n')
    #print(d)
#stats_text_en(text)   #运行所定义的函数

####################################################################################################################

#text='''学号：1901050095
#姓名：陆永超
#学习内容：day6掌握函数的用法（封装+调用）
#1、封装day5的函数，封装其实很简单，就是定义（def）之后，直接运行（函数名+参数）。
#2、知道了汉字字符在u4e00 到u9fa5之间，
#学习用时：2天
#收获总结：又反复看了数据容器的内容，把day5的第2个作业又思考了多次。
#遇到的难点与问题（是否解决）：
#1、关于文件的读取，还是没看明白，这次作业还是把样本文档放在程序文件中。希望后面会单独存放文本文件，并进行处理
#2、辅导员发的视频很好。
#'''

#该函数用于统计字符串中每个汉字出现的个数。输出的结果按照降序排列，格式为以中文汉字及其字频为元组的一个字典
def stats_text_cn(text):    #定义函数，参数text可变
    setb=set(text)   #设定集合set，并把集合元素赋值给setb
    d = []   #设定列表
    for char in setb:        #char从集合setb中取值
	    if char >= u'\u4e00' and char <= u'\u9fa5':       #如果c是在u4e00 到u9fa5之间（汉字）
	        count=text.count(char)     #统计每个汉字的数量
	        n=(char,count)
	        d.append(n)         #将y加到x列表中
    x=sorted(d,key=lambda kv:kv[1],reverse=True)    #按重复次数，由大到小排列
    return x
    #print('\n按照出现次数降序输出所有汉字:\n')
    #print(x)
 
######################################################################################################

def stats_text(text):   #将两个函数合并成一个函数。
                    #都有点怀疑python是不是太简单了，封装函数只是定义函数名+参数就行
    print('\n按照出现次数降序输出所有单词:\n')
    print(stats_text_en(text),'\n')
    print('\n按照出现次数降序输出所有汉字:\n')
    print(stats_text_cn(text),'\n')     
#该函数用于统计字符串中英文单词和汉字出现的个数。输出的结果按照降序排列，格式为以单词、汉字及其字频为元组的一个字典