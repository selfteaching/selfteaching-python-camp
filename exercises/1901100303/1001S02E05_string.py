str_text='''The Zen of Python, by Tim Peters
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
Namespaces are one honking great idea -- let's do more of those!'''
#str_text.replace('better','worse')
#print(str_text.replace('better','worse'))    #2.将字符串串样本 text ⾥里里的 better 全部替换成 worse
#print(str_text.replace('ea',''))             #3.从第 2 步的结果⾥里里，将单词中包含 ea 的单词剔除
#print(str_text.swapcase())                   #将第 3 步的结果⾥里里的字⺟母进⾏行行⼤大⼩小写翻转（将⼤大写字⺟母转成⼩小写，⼩小写字⺟母转成⼤大写）
str_text=str_text.replace('*','')
str_text=str_text.replace('-','')
str_text=str_text.replace('.','')
s_list = str_text.split()
s_list.sort()
print(s_list)
