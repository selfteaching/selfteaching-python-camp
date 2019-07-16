text = '''
The Zen of Python, by Tim Peters Beautiful is better than ugly.
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

text = text.replace('better', 'worse')  #替换单词
word = []                               #赋予文本序列类型
words = []
for i in text.split():
        if i.find('ea') < 0:           
                word.append(i)          #删除单词中含有ea
for a in word:
    words.append(a.swapcase())          #大小写翻转
words.sort()                            #按字母升序排列
print(words)