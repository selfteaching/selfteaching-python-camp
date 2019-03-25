#-*- coding:utf-8 -*-

#统计英文词频函数

#将代码封装入函数
def stats_text_en():                
    import d5_exercise_stats_text
    
#定义注释函数
def annotation(string) -> '''This is a document''':     #用文档字符串进行注释
    print("Annotation:",annotation.__annotations__) 

stats_text_en()         #运行封装英文文本

docstr=stats_text_en.__doc__    #使用文本文档属性函数

annotation(docstr)              #对文本文档进行注释


#统计中文词频函数

cndic={}                        #初始化一个空的字典

def stats_text_cn(checkstr):    #定义检索中文函数
    for i in checkstr:
        if u'\u4e00' <= i <= u'\u9fff':
            cndic[i] = checkstr.count(i)
    return cndic

#一个中英混杂的文本
text = '''                       
The Zen of Python, by Tim Peters
美丽 is better than 丑陋.
清楚 is better than 含糊.
简单 is better than 复杂.
复杂 is better than 难懂.
单一 is better than 嵌套.
稀疏 is better than 稠密.
可读性计数.
Special cases aren't special enough to 打破规则.
即使练习会使得不再纯粹.
但错误不应该用沉默来掩盖.
Unless explicitly silenced.
面对起义，拒绝猜的诱惑.
有且只有一个办法.
Although that way may not be obvious at first unless you're Dutch.
尝试总比从未试过要强.
Although never is often better than *right* now.
如果执行很难被解释，那将是一个很糟的想法.
如果执行很容易解释，这会是一个好点子.
Namespaces are one honking great idea -- 让我们继续为之努力!
'''

stats_text_cn(text)             #调用检索中文频次的函数

cndic=sorted(cndic.items(),key=lambda item:item[1],reverse = True)      #为了阅读方便，检索完毕后对字典进行按值从大到小排序

print(cndic)                            #打印汉字

annotation(cndic)                       #调用注释函数
