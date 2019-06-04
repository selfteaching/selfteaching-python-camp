def stats_text_en():      #创建函数          
    import d5_exercise_stats_text    #将代码封装入函数
    
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
美胜于丑。
显式优于隐式。
简单胜于复杂。
复杂总比复杂好。
平的比嵌套的好。
稀疏胜于稠密。
可读性计数。
特殊情况不足以打破规则。
尽管实用性胜过纯洁性。
错误永远不会悄悄地过去。
除非明确沉默。
面对歧义，拒绝猜测的诱惑。
应该有一种——最好只有一种——显而易见的方法来做到这一点。
不过，如果不是荷兰语的话，这种方式一开始可能并不明显。
现在总比没有好。
虽然从来没有比现在更好。
如果实现很难解释，那是个坏主意。
如果实现很容易解释，这可能是一个好主意。
名称空间是一个非常好的主意——让我们做更多的事情吧！
'''

stats_text_cn(text)             #调用检索中文频次的函数

cndic=sorted(cndic.items(),key=lambda item:item[1],reverse = True)      #为了阅读方便，检索完毕后对字典进行按值从大到小排序

print(cndic)                            #打印汉字

annotation(cndic)                       #调用注释函数