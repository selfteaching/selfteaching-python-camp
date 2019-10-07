#1.封装统计英文单词词频的函数
text1= '''
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

import string #用import导入string模块

def stats_text_en(text):
    for x in string.punctuation:#用string模块中的punctuation功能检查标点符号并用空格代替
	    text1=text.replace(x,"")
    text2=text1.split() #以空格拆分为独立单词

    for i in text2:
        if u'\u4e00' <= i <= u'\u9fff':#判断是不是中文
            text2.remove(i) #将列表中中文删除

    dic={}
    for i in text2:  #将字符串转换为字典
        count=text2.count(i)
        r1={i:count}
        dic.update(r1)
    dic1=sorted(dic.items(),key=lambda x:x[1],reverse=True) #按照单词出现次数，从大到小排序
    return(dic1)
print(stats_text_en(text1))  #调用函数并打印结果


#2.封装统计中文汉字字频的函数 
text_1 = '''                       
"Her eyes beginning to water, she went on,
"So I would like you all to make me a promise:
from now on, on your way to school，
or on your way home, find something beautiful
to notice. It doesn' t have to be something you
see -it could be a scent perhaps of freshly
baked bread wafting out of someone 's house,
or it could be the sound of the breeze
slightly rustling the leaves in the trees,
or the way the morning light catches one
autumn leaf as it falls gently to the ground.
Please, look for these things, and remember them."
　　她的眼睛开始湿润了，她接着说因此我想让你们每个人答应我:
从今以后，在你上学或者放学的路上，要发现一些美丽的事物。
它不一定是你看到的某个东西——它可能是一种香味——
也许是新鲜烤面包的味道从某一座房里飘出来，也许是微风轻拂树叶的声音，
或者是晨光照射在轻轻飘落的秋叶上的方式。请你们寻找这些东西并且记住它们吧。 
'''

def stats_text_cn(text):    #定义检索中文函数
    cndic={} 
    for i in text:
        if u'\u4e00' <= i <= u'\u9fff':#判断是不是中文
            count = text.count(i)
            cndic2 = {i:count}
            cndic.update(cndic2)
    cndic=sorted(cndic.items(),key=lambda item:item[1],reverse = True) 
    return cndic
print(stats_text_cn(text_1)) #调用函数并打印结果


def stats_word(text): #定义函数，实现统计汉字和英文单词出现次数
    print(stats_text_en(text))
    print(stats_text_cn(text))
stats_word(text_1)