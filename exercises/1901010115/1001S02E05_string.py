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

text2 = text.replace("better","worse") #设置text2为替换worse后的新文本
print(text2)

text_list3 = text2.split() #以空格为分割点，将文本分割为列表
str1 ='ea' #设置检索单元
for i in text_list3: #设定i在列表中进行循环罗列
    if i.find(str1) > -1: #如果存在”ea“，则提取”ea“的位置编号
        text_list3.remove(i) #去掉列表中编号为i的项
text3 = ' '.join(text_list3) #将空格插入到text_list3中，以重新呈现为文本形式
print(text3)
print('\n')

text4 = text3.swapcase() #用swapcase对”字符串“类型的文本进行大小写翻转
print(text4)
print('\n')

text_list5 = text4.split() #再次将字符串提取为列表
text_list5.sort() #排序列表（这里只是对text_list执行排序指令，并不输出值，所以不能赋值一个新的list5）
print(text_list5)