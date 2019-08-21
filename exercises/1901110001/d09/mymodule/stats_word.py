from collections import Counter
text='''The Zen of Python, by Tim Peters
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
 Namespaces are one honking great idea -- let's do more ofte'''

def stats_text_en(text,count):
    if not isinstance(text, str):
        raise ValueError('参数应当为str类型')
    a=text.split()
    symbols='。，；--*'
    words=[]
    for a1 in a:
        for symbol in symbols:
            b=a1.replace(symbol,'')
            words.append(b)
    return Counter(words).most_common(count)


        

text2='''函数的执行会引入一个用于函数局部变量的新符号表。
更确切地说，函数中所有的变量赋值都将存储在局部符号表中；而变量引用会首先在局部符号表中查找，
然后是外层函数的局部符号表，最后是内置名称表。
因此，全局变量和外层函数的变量不能在函数内部直接赋值.'''
def stats_text_cn(text,count):
    if not isinstance(text, str):
        raise ValueError('参数应当为str类型')
    CN=[]
    for CN1 in text2:
        if '\u4e00'<=CN1<='\u9ffff':
            CN.append(CN1)
    return Counter(CN).most_common(count)

def stats_text(text,count):
    if not isinstance(text,str):
        raise ValueError('参数必须为str类型')
    return stats_text_cn(text,count) + stats_text_en(text,count)