# 统计英文词频函数

# 将代码封装入函数
def stats_text_en():                
    import d5_exercise_stats_text
    
# 定义注释函数
def annotation(string) -> '''This is a document''':     # 用文档字符串进行注释
    print("Annotation:",annotation.__annotations__) 

stats_text_en()         # 运行封装英文文本

docstr=stats_text_en.__doc__    # 使用文本文档属性函数

annotation(docstr)              # 对文本文档进行注释


# 统计中文词频函数

cndic={}                        # 初始化一个空的字典

def stats_text_cn(checkstr):    # 定义检索中文函数
    for i in checkstr:
        if u'\u4e00' <= i <= u'\u9fff':
            cndic[i] = checkstr.count(i)
    return cndic

# 一个中英混杂的文本
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

Python是一种计算机程序设计语言。是一种动态的、面向对象的脚本语言，最初被设计用于编写自动化脚本(shell)，随着版本的不断更新和语言新功能的添加，越来越多被用于独立的、大型项目的开发。
'''
stats_text_cn(text)             # 调用检索中文频次的函数

cndic=sorted(cndic.items(),key=lambda item:item[1],reverse = True)      # 为了阅读方便，检索完毕后对字典进行按值从大到小排序

print(cndic)                            # 打印汉字

annotation(cndic)                       # 调用注释函数
