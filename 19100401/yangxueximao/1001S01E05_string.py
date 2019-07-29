text='''The Zen of python, by Tim Peters
	Beautiful is better than ugly.
	Explicit is better than implicit.
	Simple is better than complex.
	Complex is better than complicated.
	Flat is better than nested.
	Sparse is better than dense.
	Readability counts.
	Special cases arent't special enough to break the rules.
	Although practicality beats purity.
	Errors should never pass silently.
	Unless explicitly silenced
	In the face of ambxiguity,refuse the temptation to guess
	There should be one-- and preferably only one --obvious way to do it.
	Although that way may not be obvious at first unless you're Dutch
	If the implementation is hard to explain,it's a bad idea
	If the implementation is easy to explain,it's may be a good idea.
	Namespaces are one honking great idea --let's do more of those!'''

text2=(text.replace('better','worse'))
print(text2)

#找到ea，并删除对应单词
text3=text2.split()
character='ea'
text4=[]
for i in text3:
	if i.find(character)==-1:
		text4.append(i)
print(text4)

#将s中的大写写字母翻转
text_string=' '.join(text4)
text_string=text_string.swapcase()
print(text_string)

#将第四步所有单词排序
text_string = text_string.lower()
text_list_final = text_string.split()
print(sorted(text_list_final))





