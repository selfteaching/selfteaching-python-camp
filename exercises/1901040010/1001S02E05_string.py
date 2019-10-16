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
#将文本中的“better”用“worse”代替
new_text = text.replace('better', 'worse')
print (new_text)

#将单词中包含 ea 的单词剔除#
delete_word = new_text.split()
for i in delete_word:
    if 'ea' in i:
            delete_word.remove(i)
l = [] 
for j in delete_word:
        l.append(j+'  ')
s = ''.join(l)
print(s)

#将字⺟进行⼤小写翻转#
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

#所有单词按a...z升序排列列#
t1 = t.replace(',', ' ').replace('.', ' ').replace(  '--', ' ').replace('!', ' ').replace('*', ' ')
t2 = t1.split()
t2.sort()
print(t2)
