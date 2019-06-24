import string
import re

text = '''
The Zen of Python, by Tim Peters Beautiful is better than ugly.
Explicit is better than implicit.Simple is better than complex.Complex is better than complicated.Flat is better than nested.
Sparse is better than dense.Readability counts.Special cases aren't special enough to break the rules.Although practicality beats purity.
Errors should never pass silently.Unless explicitly silenced.In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do
it.Although that way may not be obvious at first unless you're Dutch.Now is better than never.
Although never is often better than *right* now.If the implementation is hard to explain, it's a bad idea.If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
 '''
print(text)
re_text = text.replace('better','worse',text.count('better'))
print("******************把better替换为worse:*****************")
print("替换字符结果为：",re_text)
print()

print("**********************删除包含ea的单词******************")
print()
#创建一个65~122数列对应所有大小写字母
pattern = re.compile("[A-Z]*[a-z]+")
del_text = re.findall(pattern,re_text)

result_text = []
for item in del_text:
    if 'ea' not in item:
        result_text.append(item)
    else:
        continue
result_text = ' '.join(result_text)
print(result_text) 
print()

print("***************************将文本大小写翻转*********************************")
print()
swap_text = result_text.swapcase()
print(swap_text)
print()

print("****************************单词顺序不变，单词内字母升序排列********************")
print()

rank_text = swap_text

rank_text = rank_text.split(' ')

for i in range(0,len(rank_text)):
    rank_word = sorted(rank_text[i])
    rank_word = ''.join(rank_word)
    print(rank_word,end = ' ')

print(rank_text[i])




    