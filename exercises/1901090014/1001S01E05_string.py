text='''
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
There should be one -- and preferably only one -- obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
#  better替换 worse

#print(text.replace('better','worse'))

#  去除ea

symbol = ",.!-*"
for str in symbol:
    text= text.replace(str,'')
print(text)

#split切片
text2=text.split()
text3=[]#新建一个空的列表
for i in text2:
    if i.find('ea')<0:
        text3.append(i)
print(text3)
 # 小写字母转换成大写字母
b = []
for n in text:
   if "a"<= n <= "z":
      b.append(n.upper())
   elif"A" <= n <= "Z" :
      b.append(n.lower())
   else:
      b.append(n)
#print("".join(b))
#升序排列
s=list(text)
s.sort()
#print (s)




