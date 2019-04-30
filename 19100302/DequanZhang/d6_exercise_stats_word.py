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
'''
   #将代码封装入函数     *source code copied from @zdy958  in class 19100103
def stats_text_en():                
    import d5_exercise_stats_text
#定义注释函数
def annotation(string) -> '''This is a document''':     #用文档字符串进行注释
    print("Annotation:",annotation.__annotations__) 

stats_text_en()         #运行封装英文文本
docstr=stats_text_en.__doc__    #使用文本文档属性函数

annotation(docstr)              #对文本文档进行注释


#统计中文词频函数
dic={}                        #初始化一个空的字典

def stats_text_cn(checkchinese):    #定义检索中文函数
    for i in checkchinese:
        if u'\u4e00' <= i <= u'\u9fff':
            dic[i] = checkchinese.count(i)
    return dic

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

dic=sorted(dic.items(),key=lambda item:item[1],reverse = True)      #为了阅读方便，检索完毕后对字典进行按值从大到小排序

print(dic)                            #打印汉字

annotation(dic)                       #调用注释函数


