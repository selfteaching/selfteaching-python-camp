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
string.replace("better", "worse")
print('\n替换better后的结果：',string.replace("better","worse"))


#从第2步的结果⾥，将单词中包含 ea 的单词剔除
text1 = text.replace('better','worse')
text2  =text1.split()   #用str.split()方法把字符串变成由若干个元素组成的列表
i = 0
while 'ea' in text2[i] and i <= len(text2):
    del text2[i]   #删除含ea的单词
print ('\n删除含ea的单词的结果：\n',text2)


#将第3步的结果里的字⺟进⾏大小写翻转(将大写字母转成小写，⼩写字母转成大写)
text3 = ' '.join(text2)   #列表转换成字符串
text4 = text3.swapcase()   #字符串有转换大小写函数
print('\n大小写翻转后新字符串text4为：\n',text4)

#将第4步的结里所有单词按a...z升序排列，并输出结果
text5 = text4.split()   # 排序需要通过列表，上一步结果字符串转换成列表
text5.sort()
print('\n单词首字母按a-z升序后新列表text5如下：\n',text5)

#输出结果中某些单词开头有特殊符号，予以删除后再进行排序,并输出结果
text6 = ''  #创建空字符串
for i in range(len(text4)):
        if text4[i] != '*' and text4[i] != '-':
                text6 += text4[i]   #将去掉特殊字符的字符串重新赋值
text7 = text6.split()
text7.sort()
print('\n删除特殊字符后重新排序的列表text7为：\n',text7)
