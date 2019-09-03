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
K01=text.replace('better','worse')
#将含EA的单词都剔除
K02=K01.split()
K03=[]
for a in K02:
    if "ea" not in a:
        K03.append(a)
K04=' '.join(K03)
#将字母大写改小写，小写改大写
K05=K04.swapcase()
#倒序排列
K06=K05.replace(","," ").replace("."," ").replace("--"," ").replace("*"," ").replace("!"," ")
K07=K06.split()
K08=sorted(K07)
K09=' '.join(K08)

print(K09)