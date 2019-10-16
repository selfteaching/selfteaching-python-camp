text='''
The Zen of Python,by Tim Peters


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
In the face of ambxiquity,refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Altough that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain,it's a bad idea.
If the implementation is easy to explain,it's a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

# 替换str.replace(old, new[, count])
#print("text.lower().replace('better', 'worse'):\n")
s=text.lower().replace('better', 'worse')
print(s)
print()
#删除含ea的单词
k=s.split()
new_list=[]
for word in k:
    if word.find("ea")<0:
        new_list.append(word)
print(new_list)
print()

#大小写转换.swapcase(),或.upper()、.lower()
swapcased=[i.swapcase() for i in new_list ]
print(swapcased)
print()
#升序

print(sorted(swapcased))

