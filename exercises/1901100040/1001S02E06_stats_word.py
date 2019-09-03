text='''The Zen of Python, by Tim Peters.
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated. 9 Flat is better than nested.
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
Namespaces are one honking great idea -- let's do more of those!'''
def stats_text_en(text):
    dictionary={} 
    #创建一个字典
    text_en=text.replace(',',' ').replace('.',' ').replace('--',' ').replace('!',' ').replace('*',' ')
    #将text中标点符号用空格替换
    mytext=text_en.split( ) 
    for i in mytext:                
        dictionary[i]=mytext.count(i) 
    dic=sorted(dictionary.items(),key=lambda item:item[1],reverse=True)
    #按照值从大到小的排序
    print(dic)
    #返回一个按词频降序排列的数组
stats_text_en(text)
#运行stats_text_en(text)函数

text='''学习编程很费劲,英语单词量太小,作业一多,就心急如焚,心脏病都快犯了,我真是自讨苦吃!:)'''
def stats_text_cn(text):
    dictionary={} 
    #创建一个字典
    text_cn=text.replace(',','').replace('!','').replace(':','').replace(')','')
    #将text中标点符号替换为空
    for i in text_cn:                
        dictionary[i]=text_cn.count(i) 
    dic=sorted(dictionary.items(),key=lambda item:item[1],reverse=True)
    #按照值从大到小的排序
    print(dic)
    #返回一个按字频降序排列的数组
stats_text_cn(text)
#运行stats_text_cn(text)函数