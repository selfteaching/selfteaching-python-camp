'''
一、字符串的基本处理
'''
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
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

'''
1、将文本中的所有better替换成worse
'''
text1=text.replace('better','worse')
print('1、将文本中的所有better替换成worse:',text1)

'''
2、剔除包含ea的单词
'''
text2=' '
list_text2=text1.split()

i=0               
while i<len(list_text2):
        if 'ea'in list_text2[i]:
                del list_text2[i]
                i=0
        else:
                i=i+1

text2=text2.join(list_text2)                    
print('2、剔除包含ea的单词：',text2)


'''
3、将文本中的字母大小写翻转
'''
text3=text2.swapcase()
print('3、将文本中的字母大小写翻转:',text3)

'''
4、所有单词按a...z升序排列列
'''
text4=' '
list_text4=text3.split()
#去除单词前后的特殊字符
for j in range(len(list_text4)):
        list_text4[j]=list_text4[j].strip('*--. ')

list_text4.sort()
text4=text4.join(list_text4)
print ('4、所有单词按a...z升序排列列:',text4)
