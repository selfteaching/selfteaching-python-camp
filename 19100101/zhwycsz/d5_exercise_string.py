A= """
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
"""

A=A.replace('better', 'worse') # better 替换成 worse
print(A)

A=A.swapcase()  #大小写字母转换
print(A)

A=A.replace(',',' ').replace('.',' ').replace('--',' ').replace('!',' ').replace('*',' ')
#将非英文字符替换为空格
A=A.split()#以空格拆分为独立的单词
temp1="ea"  # 剔除包含ea的英文单词
temp2=[]
for i in A:
    if i.find(temp1)<1:
        temp2.append(i)
print(temp2)

print(end='\n')
temp2.sort()    #将所有单词按a，...z升序排列
print(temp2)