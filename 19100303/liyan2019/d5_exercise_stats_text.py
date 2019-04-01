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

print(text)
text1=text.replace(',',' ').replace('.','').replace('!','').replace('*',' ').replace('-','')
print(text1)
text2=text1.split()
# string.count(str, beg=0, end=len(string))
##i=text1.count('is',0,len(text1))
##print(''is' 在文中出现的次数是:',i)
wordnum={}
for i in text2:
    wordcount=text2.count(i)
    wordnumber={i:wordcount}  #好像不先定义空字典以及后续的update，直接print（Wordnumber）无法成功。why？
    wordnum.update(wordnumber)
print(wordnum)
print(sorted(wordnum.items(),key=lambda x:x[1],reverse=True))##但是输出的是列表格式，而非字典格式。
#sorted:wordnums.items()，得到包含键，值的元组,由于迭代对象是元组，返回值自然是元组组成的列表,这里对排序的规则进行了定义，x指元组，x[1]是按值排序，x[0]是按键排序
# sorted(wordnums)，默认是对字典的键，从小到大进行排序;sorrted（wordnum,reverse=true）,表示按键从大到小排序，等同于 sorted(wordnum.keys(),reverse=True)
# sorted(wordnums.values())，表示对字典的值，小到大排序。





