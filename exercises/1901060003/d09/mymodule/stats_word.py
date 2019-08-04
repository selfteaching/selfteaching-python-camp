#统计参数中每个英文单词出现的次数，
#疑惑在于没有判断文本是否为英文，除非直接要判断的文本就是英文
from collections import Counter
def stats_text_en(text):
    if not isinstance(text,str):
        raise ValueError('参数必须是str类型，输入类型%s'%type(text))
    elements=text.split()
    words=[]
#先针对sample text挑选出需要剔除的非单词符号
    symbols=',.*-!'
    for element in elements:
    #遍历一遍要剔除的符号
        for symbol in symbols:
        #逐个替换字符号，用''是为了同时删除符号所占的位置
            element=element.replace(symbol,'')
        #剔除了字符后如果element的长度不为0，则算是正常单词
        if len(element) and element.isascii():
            words.append(element)
#Day9 用collections的counter 来计数，下面的暂时不用
    count=100
    return Counter(words).most_common(count)

#初始化一个dict 类型的变量，用来存放单词出现的次数
    #counter={}
#set(集合)类型 可以去除列表里的重复元素，可以在for...in里减少循环次数
    #word_set=set(words)

    #for word in word_set:
        #counter[word]=words.count(word)
    #print('英文单词出现的次数==>',counter)，作为函数，直接用ruturn
#2. 按照出现次数从大到小输出所有的单词及出现的次数
#内置函数sorted的参数key表示按元素的那一项的值进行排序
#dict 类型 counter的items方法会返回一个包含相应项（key,value）的元组列表
#print('counter.items()==>',counter.items())
#  #print('从大到小输出所有出现的单词及出现的次数==>',sorted(counter.items(),key=lambda x:x[1],reverse=True))
    
    # return sorted(counter.items(),key=lambda x:x[1],reverse=True)


# 统计:参数中每个中文汉字出现的次数
def stats_text_cn(text):
    if not isinstance(text,str):
        raise ValueError('参数必须是str类型，输入类型%s'%type(text))
    cn_characters=[]
    for character in text:
    #unicode中中文字符的范围
        if'\u4e00'<=character<='\u9fff':
            cn_characters.append(character)
    #Day9 用collections的counter 来计数，下面的暂时不用
    count=100
    return Counter(cn_characters).most_common(count)
    # counter={}
    # cn_character_set=set(cn_characters)
    # for character in cn_character_set:
    #     counter[character]=cn_characters.count(character)
    # return sorted(counter.items(),key=lambda x:x[1],reverse=True)

#定义stats_text函数，统计样本文件中出现的中英文的次数。
def stats_text(text):
    if not isinstance(text,str):
        raise ValueError('参数必须是str类型，输入类型%s'%type(text))
    '''
    合并英文词频和中文词频的结果
    '''
    return stats_text_cn(text) + stats_text_en(text)
    
en_text='''
The Zen of Python, by Tim Peters


Beautiful is better than ugly. 
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated. 
Flat is better than nested. 
Sparse is better than dense.
Readability counts
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

cn_text='''
Python之禅 by Tim Peters

优美胜于丑陋
明了胜于晦涩
简洁甚于复杂
复杂甚于凌乱
扁平甚于嵌套
间隔甚于紧凑
可读性很重要
即便假借特例的实用性知名，也不可违背这些原则
不要包容所有错误，除非你确定需要这样做
当存在多种可能，不要尝试去猜测
而是尽量找一种，最好是唯一一种明显的解决方案
虽然这并不容易，因为你不是Python之父
做也许好过不做，但不假思索就动手还不如不做
。。。
'''

#搜索 _name_==_main_
#一般情况下在文件内测试代码的时候以下面的形式进行
if __name__ == "__main__":

   print('hello')
   en_result=stats_text_en(en_text)
   cn_result=stats_text_cn(cn_text)
   merge_result=stats_text(en_text+cn_text)
   print('统计参数中出现次数前100的英文单词==>\n',en_result)
   print('统计参数中出现次数前100的中文汉字==>\n',cn_result)
   print('词频最高的前100个字==>\n',merge_result)
   

