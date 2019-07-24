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

#1.将字符串样本text里英文单词中包含ea的英文单词剔除
#2.将better全部替换成worse
#3.大写字母转成小写，小写字母转成大写
#4.将所有单词按a...z升序排列
#5.最后输出结果

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

text=text.replace('better', 'worse') # 将 better 替换成 worse
text=text.swapcase() #转换大小写

text=text.replace(',',' ').replace('.',' ').replace('--',' ').replace('!',' ').replace('*',' ')
text=text.split() 
s1="ea"
s2=[]
for i in text:
    if i.find(s1)<1:
        s2.append(i)
s2.sort()
print(s2)


