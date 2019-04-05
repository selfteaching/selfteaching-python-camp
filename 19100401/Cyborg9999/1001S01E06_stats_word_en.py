text = '''
The Zen of python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases arent't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced
In the face of ambxiguity,refuse the temptation to guess
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch
If the implementation is hard to explain,it's a bad idea
If the implementation is easy to explain,it's may be a good idea.
Namespaces are one honking great idea --let's do more of those!
'''
def stats_text_en(text):#封装开始
    lst=text.split()#把句子拆分为单词
    adict={}#定义词典
    for i in lst:#i值开始遍历单词文本
        adict.update({i:lst.count(i)})#adict词典开始赋值及计算词频
    tup1 = sorted(adict.items(),key = lambda x:x[1],reverse = True)#元组根据词频排序
    return tup1#返回值
    
print(stats_text_en(text))