import re

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
There should be one-- and preferably only one --obvious way to do
it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

#将text ⾥的 better 全部替换成 worse，将单词中包含 ea 的单词剔除,对字⺟进⾏⼤⼩写翻转
text_1 = text.replace('better','worse').replace('ea','').swapcase()

#将第上步的结果⾥所有单词按 a…z 升序排列
text_2 = re.sub(r'[\-\*\.\-!,]', '', text_1).split()  #去除标点，只留单词,并将字符串分拆成单词列表

text_2.sort()  #对单词列表排序 

result = ' '.join(text_2) #将排序结果生成字符串

print(result)
