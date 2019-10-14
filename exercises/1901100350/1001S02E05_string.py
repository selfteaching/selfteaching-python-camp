sample_text = '''
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
Although that way may not be obvious at first unless you're Dutch. Now is better than never. 
Although never is often better than *right* now. 
If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

1#将字符串样本text里的所有 better 替换为 worse.

text = sample_text.replace("better","worse")
print("str",text)

2#将单词中含有ea剔除
#先将字符串根据空白字符分割成list，要调用str
words = text.split()
#定义一个list类型的变量存放过滤完的单词
filtered = []
#用for...in循环来检查是否含有ea
for word in words:
    if word .find ('ea') < 0:
        filtered.append(word)
print("str",filtered)

3#
swapcased = [i.swapcased() for i in filtered]
print("进行大小写翻转 ==>",swapcased)



