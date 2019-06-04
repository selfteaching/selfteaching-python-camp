
text = '''
The Zen of Python, by Tim Peters.


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
text1=text.split()
zifu="ea"  # 剔除包含ea的英文单词
text2=[]
for i in text1:
    if i.find(zifu)<1:
        text2.append(i)
text3=" ".join(text2)  # 将列表改成字符串
print(text3.replace('.','.\n'))# 遇'.'换行

print(text.replace('better','worse'))  # 将better全部替换成worse

print(text.swapcase())  # 小写字母改成大写，大写字母改成小写

text2.sort()  #将列表中单词按a...z顺序排列
text4=" ".join(text2)
text4=text4.lower()
text4=text4.replace(',',' ').replace('.',' ').replace('--',' ').replace('!',' ').replace('*',' ').replace('\n',' ').replace('  ',' ')
print(text4)  