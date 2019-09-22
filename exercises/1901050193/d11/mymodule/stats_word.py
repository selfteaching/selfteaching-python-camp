from collections import Counter
import jieba
import re


#定义函数stats_text_cn 用于统计文档中中文单词出现的次数并按照频率降序排列。
def stats_text_cn(text,count):
    if type(text)!= str:
        raise ValueError('非字符串类型')
    else:
        pass
    #提前处理掉所有非中文部分
    #[^\u4e00-\u9fa5]表示所有非中文
    text = re.sub('[^\u4e00-\u9fa5]','',text) 

    #jieba 用精确模式分词
    seg_list = jieba.cut(text, cut_all=False) 
    
    #只统计长度大2的词
    seg_dic = []
    for word in seg_list:
        if len(word)>=2:
            seg_dic.append(word)

    
    counter = Counter(seg_dic).most_common(count)     #使⽤用标准库中的 Counter 来完善统计功能
    return sorted(dict(counter).items(), key = lambda x:x[1],reverse = True)


text='''
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
    print('中文单字按出现次数降序排列:\n', stats_text_cn(text,20))