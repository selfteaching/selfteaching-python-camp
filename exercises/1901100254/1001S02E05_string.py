
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


string = text
string.replace("better", "worse")   #替换函数str.replace()
print('\n替换better后的结果：',string.replace("better","worse"))


#从第2步的结果⾥，将单词中包含 ea 的单词剔除
text1 = text.replace('better','worse')
text2  =text1.replace('ea', '__')  
print ('\n删除含ea的单词的结果：\n',text2)


#将第3步的结果里的字⺟进⾏大小写翻转(将大写字母转成小写，⼩写字母转成大写)
text3 = ' '.join(text2)   #列表转换成字符串
text4 = text3.swapcase()   #逐个字符更替大小写
print('\n大小写翻转后新字符串text4为：\n',text4)

#将第4步的结里所有单词按a...z升序排列，并输出结果
text5 = text4.split()   # 排序需要通过列表，上一步结果字符串转换成列表
text5.sort()
print('\n排列结果如下：\n',text5)
