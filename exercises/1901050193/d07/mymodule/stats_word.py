#定义函数1：统计参数中每个英⽂文单词出现的次数，最后返回⼀个按词频降序排列列的数组。
def stats_text_en(text):
    words = text.split()
    wordlist = []
    symbols = ',.*-!'
    for word in words:
        for symbol in symbols:
            word = word.replace(symbol,'')
        if len(word) and word.isascii():
            wordlist.append(word)
    counter = {}
    wordset = set(wordlist)
    
    for singleword in wordset:
        counter[singleword] = wordlist.count(singleword)
    return sorted(counter.items(), key=lambda x: x[1], reverse=True)  #返回函数结果


#定义函数2：统计文档中中文单词出现的次数并按照频率降序排列。
def stats_text_cn(text):
    cnsymbols=[]
    for cnsymbol in text:
        if '\u4e00'<= cnsymbol<='\u9fff':  #判断是否属于中文单字，可以直接过滤掉符号等等了。
            cnsymbols.append(cnsymbol)
    counter={}
    cnsymbols_set=set(cnsymbols)
    for cnsymbol in cnsymbols_set:
        counter[cnsymbol]=cnsymbols.count(cnsymbol)
    return sorted(counter.items(), key = lambda x: x[1], reverse=True) #同上返回函数结果


def stats_text(text): 
#合并 英文词频 和中文词频 的结果
    return stats_text_en(text) + stats_text_cn(text)


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

if __name__=='__main__':
    # if _name_=='_main_'："的作用在于：如果直接执行含有该语句的模块，则执行该语句后续部分；
    # 若在另一个模块中调用含有该语句的模块时，该语句的后续部分不执行。
    
    en_result = stats_text_en(en_text)  #给函数的返回结果一个值 
    cn_result = stats_text_cn(cn_text)  #中文同上
    print('英文单词按出现次数降序排列:\n', en_result)
    print('中文单字按出现次数降序排列:\n', cn_result)



