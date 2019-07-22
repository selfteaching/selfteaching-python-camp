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

new_text = text.replace('better', 'worse')  #将字符串text 里的 better 替换成 worse
print(new_text)

# text1 = text.replace(',', ' ').replace('.', ' ').replace(  '--', ' ').replace('!', ' ').replace('*', ' ')
# print(text1)


#将单词中包含“ea”的单词剔除
test_text = new_text.split()
# print(test_text)

for i in test_text:
        if 'ea' in i:              
                test_text.remove(i)    

# i_ea = ''.join([test_text])
# print(test_text) 
l = [] 
for j in test_text:
        l.append(j+'  ')
s = ''.join(l)
print(s)

#将第三步结果里的字母大小写反转
# l = []



def fn( x ):
    if x.islower():
        return x.upper()
    elif x.isupper():
        return x.lower()
    else:
        return x

                                                # result = ''.join  ([fn(r) for r in test_text])
t = ''.join([fn(r) for r in s])
print (t)


t1 = t.replace(',', ' ').replace('.', ' ').replace(  '--', ' ').replace('!', ' ').replace('*', ' ')
t2 = t1.split()
t2.sort()
print(t2)



# text.swapcase()
# print(text)