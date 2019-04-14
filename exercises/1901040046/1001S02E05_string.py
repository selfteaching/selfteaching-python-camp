#这个版本很完美。思路清晰，排版整洁，语句老练。主要学习了剔除包含关键字词语的语言方法。
#1.将字符串样本text里英文单词中包含ea的英文单词剔除
def cut_and_clean(s):
    s=s.split()
    i=0
    while i<len(s):
        s[i]=s[i].strip('*-.')
        if s[i]=='':
            s.remove('')
        else:
            i=i+1
    return s


#2.将s字符串中包含keyword的词删除
def delet_word(s,keyword):
    i=0
    while i<len(s):
        if 'ea' in s[i]:
            del s[i]  
        else:
            i=i+1
    return s

#3.将better替换成worse
def change_word(s,keyword1,keyword2):
    for i in  range(len(s)):
        if s[i]==keyword1:
            s[i]=keyword2
    return s

#4.大写转小写，小写转大写
def case_change(s):
    for i in range(len(s)):
        s[i]=s[i].swapcase()
    return s

#字符样本
text = '''
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
text=cut_and_clean(text)
text=delet_word(text,'ea')
text=change_word(text,'better','worse')
text=case_change(text)
text.sort()
print(text)