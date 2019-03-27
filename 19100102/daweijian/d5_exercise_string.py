def cut_clean(s):
    #切分字符串
    s=s.split()
    #清洗标点符号
    i=0
    while i<len(s):
        s[i]=s[i].strip('*-.')
        if s[i]=='': #清洗完成之后若为空元素‘’，则删除元素
            s.remove('')
        else:
            i=i+1
    return s

def del_word(s,w):
    i=0
    while i<len(s):
        if w in s[i]:
            del s[i]
        else:
            i=i+1
    return s

def change_word(s,w1,w2):
    for i in range(len(s)):
        if s[i]==w1:
            s[i]=w2
    return s

def case_switch(s):
    for i in range(len(s)):
        s[i]=s[i].swapcase()
    return s



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
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
text=cut_clean(text) #切分字符串并清洗标点符号
text=del_word(text,'ea') #将字符串样本text里英文单词中包含ea的英文单词剔除
text=change_word(text,'better','worse') #将better全部替换成worse
text=case_switch(text) #大写字母转成小写，小写字母转成大写
text.sort() #将所有单词按a...z升序排列
print(text) #打印结果