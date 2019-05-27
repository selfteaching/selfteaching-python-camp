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
#替换字符
yl01=text.replace('better','worse')
#将含EA的单词都剔除
yl02=yl01.split()
yl03=[]
for a in yl02:
    if "ea" not in a:
        yl03.append(a)
yl04=' '.join(yl03)
#将字母大写改小写，小写改大写
yl05=yl04.swapcase()
#倒序排列
yl06=yl05.replace(","," ").replace("."," ").replace("--"," ").replace("*"," ").replace("!"," ")
yl07=yl06.split()
yl08=sorted(yl07)
yl06=' '.join(yl08)

print(yl06)