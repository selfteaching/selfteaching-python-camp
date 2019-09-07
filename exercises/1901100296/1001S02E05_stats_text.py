'''
统计字符串样本中英文单词出现的次数
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
list_text=text.lower().split()

#去除特殊字符
for i in range(len(list_text)):
    list_text[i]=list_text[i].strip('*--!., ')
#去除空字符
i=0               
while i<len(list_text):
        if ''==list_text[i]:
                del list_text[i]
                i=0
        else:
                i=i+1   
# print(list_text)
# 使用字典类型统计文本中单词数
word_dic={}
for word in list_text:
    if word in word_dic.keys():
        word_dic[word]=word_dic[word]+1  
    else:
        word_dic[word]=1

list_sorted=sorted (word_dic.items(),key=lambda item:item[1],reverse=True)
# 打印统计结果  
#  
print (list_sorted)
for i in list_sorted:
        a,b=i
        print(a,':',b)  
