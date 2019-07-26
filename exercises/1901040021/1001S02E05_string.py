#字符串的基本处理
#step2：将字符串样本text里的better全部替换成worse
text='''The Zen of Python, by Tim Peters
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
Namespaces are one honking great idea -- let's do more of those!'''
a_text=text.replace('better','worse') #将text中better替换成worse，并将新string保存在a_text中
print(text)
print(a_text)

#step3：从第2步的结果里，将单词中包含ea的单词剔除
a_list=a_text.split()  #convert string to list
print(a_list)

import re
b_list=a_list[:]   #copy a_list
for i in range(0,len(b_list)):  
    if re.match(r'\w*ea\w*',b_list[i]):  #首先查找出包含ea的单词
        b_list[i]=''' '''   #然后将包含ea的单词替换成空格
print(b_list)

b_text=' '.join(b_list)  #convert list to string，并将string中各值以空格连接
print(b_text)

#step4：将第 3 步的结果⾥的字⺟进⾏⼤⼩写翻转（将⼤写字⺟转成⼩写，⼩写字⺟转成⼤写）
c_text=b_text.swapcase() 
print(c_text)

#step5：将第4步的结果里所有单词按a...z升序排列，并输出结果
c_list=c_text.split()  #convert string to list
print(c_list)

d_list=sorted(c_list) #sort list
print（d_list）

d_text=' '.join(d_list) #convert list to string
print(d_text)
