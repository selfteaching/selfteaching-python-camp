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
我是乱入的中文,哈哈哈
'''
import re                     #引入正则表达式
def stats_text_en(en):        #定义一个函数
    #\u4e00-\u9fa5 	汉字的unicode范围
    #\u0030-\u0039 	数字的unicode范围
    #\u0041-\u005a 	大写字母unicode范围
    #\u0061-\u007a 	小写字母unicode范围
    #sub(pattern,repl,string) 	把字符串中的所有匹配表达式pattern中的地方替换成repl
    t1= re.sub(u"([^\u0041-\u005a\u0061-\u007a])"," ",en) #将en中非英文字符转换成“ ”
    text1 = t1.split() #将字符串分割
    d = {} #创建一个空字典
    for i in text1: #循环遍历
        if i in d:
            d[i] += 1 #如果字典中没有就显示1，有的话就在原来的基础上+1
        else:
            d[i] = 1

    a = sorted(d.items(),key=lambda x:x[1],reverse = True) #利用lambda函数进行values值的排序
    return a
print(stats_text_en(text))

def stats_text_cn(cn): #定义一个统计中文汉字字频的函数
    t = re.sub(u"([^\u4e00-\u9fa5])","",cn) #将cn中非中文字符转换成“”
    d = {}
    for i in t:     #中文不需要分割，可以直接遍历！！！！！
        if i in d:
            d[i] +=1
        else:
            d[i] =1
    a = sorted(d.items(),key=lambda x:x[1],reverse = True)
    return a
print(stats_text_cn(text))
