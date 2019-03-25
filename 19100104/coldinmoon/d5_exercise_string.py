#1.将字符串样本text里英文单词中包含ea的英文单词剔除
#2.将better全部替换成worse
#3.大写字母转为小写，小写字母转为大写
#4.将所有单词按a...z升序排列
#5.输出结果
#Date:3/22/2019

#剔除ea单词
def del_ea(text):
    word=[]
    for i in text.split():
        if i.find('ea')<0:
            word.append(i)
    return word

#将better全部置换成worse
def change_word(text,word1,word2):
    for i in range(len(text)):
        if text[i] == 'word1':
            text[i] = 'word2'
    return text

#大小写互换
def intial_change(text):
    for i in range(len(text)):
        text[i]=text[i].swapcase()
    return text

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
text=del_ea(text)
text=change_word(text,'better','worse')
text=intial_change(text)
text.sort()
print(text)
