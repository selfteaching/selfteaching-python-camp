
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
print('这是第1个小要求,把better换成worse\n')
text_replace = text.replace('better','worse')
print(text_replace)

text_new = text_replace.split(' ') #把字符串分割成列表


'''import re  正则表达式方法 把单词为单位分隔开 
text_string = re.findall(r"\w+",text_replace)
print(text_string)'''

list_text = []
for strea in text_new:
    if 'ea' in strea:
        strea = strea.replace(strea,'')
    else:
        pass
    list_text.append(strea)
#删掉列表中包含ea的值  print(list_text)

print('这是第2个小要求，删除掉包含ea的字符\n')
string_text = " ".join(list_text) #再把列表转成字符串
print(string_text)

print('这是第3个小要求，转换大小写\n')
text_trans = string_text.swapcase()#这是大小写转换
print(text_trans)

print('这是第4个小要求，将所有单词按照a...z的升序排列\n')
list_new = text_trans.split(' ')
list_new.sort()
list_sorted = "".join(list_new)
print(list_sorted)