# 封装统计英文单词词频的函数
def stats_text_en(text:str) -> list:
    list_text=text.lower().split()
    words=[]
    #剔除特殊字符并删除空字符
    for i in range(len(list_text)):
        list_text[i]=list_text[i].strip('*--!.,\'')
        if len(list_text[i]):
            words.append(list_text[i])
    # 使用字典类型统计文本中单词数
    word_dic={}
    keys_set=set(words)
    for word in keys_set:
        word_dic[word]=words.count(word)  
    # 对字典的值降序排列
    return sorted (word_dic.items(),key=lambda item:item[1],reverse=True)
# 封装统计汉字词频的函数
def stats_text_cn(text:str) -> list:
    # 挑拣汉字出来
    words=[]
    for word in text:
        if '\u4e00' <= word <= '\u9fff':
            words.append(word)
    # 统计文本中汉字个数
    word_dic={}
    keys_set=set(words)
    for word in keys_set:
        word_dic[word]=words.count(word)
    # 对字典值降序排列
    return sorted (word_dic.items(),key=lambda item:item[1],reverse=True)

text_en='''
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
text_ch='''
Python 是一门简单易学且功能强大的编程语言。
它拥有高效的高级数据结构，并且能够用简单而又高效的方式进行面向对象编程。
Python 优雅的语法和动态类型，再结合它的解释性，使其在大多数平台的许多领域成为编写脚本或开发应用程序的理想语言。
'''
# 测试函数
if __name__=='__main__':
    print('英文单词统计结果：',stats_text_en(text_en))
    print('汉字统计结果：',stats_text_cn(text_ch))
    
