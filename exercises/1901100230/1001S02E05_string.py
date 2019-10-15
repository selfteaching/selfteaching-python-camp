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

text = text.replace('better', 'worse')
# 将better替换为worse

# ea = re.compile(r'\w*ea\w*')
# 定义ea为包含ea的单词
# text_ea = re.findall(ea, text)
# 找出text中所有包含ea的单词
# text.split()

text = text.split()
#将text切片
text_3 = []
for i in text:
    if 'ea' not in i:
        text_3.append(i)
#去掉包含ea的单词
text_3 = " ".join(text_3)
#将list转换为string
text_4 = text_3.swapcase()
# 将大小写字母互换
text_4 = text_4.split()
text_4 = list(text_4)
text_4.sort()
#将text_4升序排序
print(text_4)