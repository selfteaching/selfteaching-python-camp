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
dictionary={} #创建一个字典

text=text.replace(',',' ').replace('.',' ').replace('--',' ').replace('!',' ').replace('*',' ')
#将text中标点符号用空格替换
mytext=text.split( ) #将text分隔成单词

for i in mytext:                #遍历文本
    dictionary[i]=text.count(i) #向字典中写入数据
dic=sorted(dictionary.items(),key=lambda item:item[1]) #按照值排序，从小到大
dic.reverse()                       #将从小到大的排序反转
print(dic)                          #得到最终结果，从大到小排序单词
    