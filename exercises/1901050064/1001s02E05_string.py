#1001s02E05_string.py
text = '''
The Zen of Python, by Tim Peters


Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sqarse is better than dense.
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
#1.将字符串样本text里的better替换成worse
new_text = text.replace('better','worse')
print('将字符串样本text里的better替换成worse==.',new_text)

#2.将包含ea的单词剔除
words = new_text.split()  #将new_text分割成list
filtered = []             #定义一个变量为空的列表，用来放过滤的单词
for word in words:        #用for...in..循环遍历一遍已分隔的单词
    if word.find('ea') < 0:
        filtered.append(word)
print('将单词中包含ea的单词剔除==>',filtered)

#3.将字母进行大小写翻转
swapcased = [i.swapcase() for i in filtered]
print('字母进行大小写翻转==>',swapcased)

#将单词按a...z升序排列
print('单词按a-z升序排列==>',sorted(swapcased))