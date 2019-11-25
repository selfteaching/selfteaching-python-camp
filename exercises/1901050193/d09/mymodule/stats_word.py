import re
from collections import Counter

#定义函数1：统计参数中每个英⽂文单词出现的次数，最后返回⼀个按词频降序排列列的数组。
def stats_text_en(text,count):
    if type(text)!= str:
        raise ValueError('非字符串类型') #遇到非字符串类型时，抛出错误
    else:
        pass
    
    
    words = text.split()
    wordlist = []
    symbols = ',.*-!'  #过滤符号


    for word in words:
        for symbol in symbols:
            word = word.replace(symbol,'')
        if len(word) and word.isascii():
            wordlist.append(word)
    
    
    counter = Counter(wordlist).most_common(count)    #使⽤用标准库中的 Counter 来完善统计功能
    return sorted(dict(counter).items(), key = lambda x:x[1],reverse = True)




#定义函数2：统计文档中中文单词出现的次数并按照频率降序排列。
def stats_text_cn(text,count):
    if type(text)!= str:
        raise ValueError('非字符串类型')
    else:
        pass
    
    
    cnsymbols=[]
    for cnsymbol in text:
        if '\u4e00'<= cnsymbol<='\u9fff':  #判断是否属于中文单字，可以直接过滤掉符号等等了。
            cnsymbols.append(cnsymbol)
    
    
    counter = Counter(cnsymbols).most_common(count)     #使⽤用标准库中的 Counter 来完善统计功能
    return sorted(dict(counter).items(), key = lambda x:x[1],reverse = True)

def stats_text(text,count): 
#合并 英文词频 和中文词频 的结果
    if type(text)!= str:
        raise ValueError('非字符串类型')
    else:
        pass
    print("文本中的中文汉字词频为：\n", stats_text_cn(text, count))
    print("文本中的英文单词词频为：\n", stats_text_en(text, count))


en_text='''
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
There should be one-- and preferably only one --obvious way to do
it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"
'''
cn_text='''
优美优于丑陋，

明了优于隐晦；

简单优于复杂，

复杂优于凌乱，

扁平优于嵌套，

可读性很重要！

即使实用比纯粹更优，

特例亦不可违背原则。

错误绝不能悄悄忽略，

除非它明确需要如此。

面对不确定性，

拒绝妄加猜测。

任何问题应有一种，

且最好只有一种，

显而易见的解决方法。

尽管这方法一开始并非如此直观，

除非你是荷兰人。

做优于不做，

然而不假思索还不如不做。

很难解释的，必然是坏方法。

很好解释的，可能是好方法。

命名空间是个绝妙的主意，

我们应好好利用它。 

'''
