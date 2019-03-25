# 1.将字符串样本text里英文单词中包含ea的英文单词剔除
# 2.将better全部替换成worse
# 3.大写字母转成小写，小写字母转成大写
# 4.将所有单词按a...z升序排列
# 5.最后输出结果
# Date: 19/03/22

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

#将字符串s按照None的分隔切分为一个字符串组，并清洗字符串元素的标点符号
def cut_and_clean(s):
    #切分字符串
    s=s.split()
    #清洗标点符号
    i=0
    while i<len(s):
        s[i]=s[i].strip('*-.!')
        if s[i]=='': #清洗完成之后若为空元素‘’，则删除元素
            s.remove('')
        else:
            i=i+1
    return s 

#将s字符串组中包含keywords的字符串元素删除
def delet_word(s,keyword):
    i=0
    while i<len(s):
        if keyword in s[i]:
            del s[i] #由于删除了一个元素，此时i不能执行i=i+1，s[i]正好是下一个元素，否则index就跳过了一个元素
        else:
            i=i+1
    return s

#将s字符串组中的全部keyword1字符串元素替换成keyword2字符串元素
def change_word(s,keyword1,keyword2):
    for i in range(len(s)):
        if s[i]==keyword1:
            s[i]=keyword2
    return s

#将s字符串组中的字符串元素的每个大写字母转成小写，小写字母转成大写
def case_change(s):
    for i in range(len(s)):
        s[i]=s[i].swapcase()
    return s



#即将要处理的文本
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
text=cut_and_clean(text) #切分字符串并清洗标点符号
text=delet_word(text,'ea') #将字符串样本text里英文单词中包含ea的英文单词剔除
text=change_word(text,'better','worse') #将better全部替换成worse
text=case_change(text) #大写字母转成小写，小写字母转成大写
text.sort() #将所有单词按a...z升序排列
print(text) #打印结果