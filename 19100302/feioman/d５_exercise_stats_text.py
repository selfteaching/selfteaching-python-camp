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
#1.1将字符串样本中better全部替换成worse
text = text.replace('better', 'worse') 
print(text)

#1.2将字符串样本中es替换为‘’
text = text.replace('ea','')
print(text)

#1.3将字符串样本中的大小写互转
text = text.swapcase()
print(text)

#1.4将字符串样本中A....z排序
text = str(sorted(text)).replace(',','\n').replace('[','').replace(']','')
print (text)