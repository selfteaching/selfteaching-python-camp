text= '''
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
text1=text.replace(',',' ').replace('--',' ').replace('*',' ').replace('!',' ')  #将字符串中的标点符号替换成‘ ’
text2=text1.split() #拆分字符串text1，返回一个列表，赋值给text2
dict1={}       #创建一个空字典
for i in text2:   
    j=text2.count(i) #统计每个单词在text2中出现次数
    dict2={i:j}      #建立一个新词典，key值为每个单词，value值为每个单词出现的次数
    dict1.update(dict2)  #因为上一步操作处于循环中，所以dict2只会有一个元素，不把他的值取出来保存到一个新变量的话，它的值很快就会在下一轮循环中被更新
dict2=sorted(dict1.items(),key=lambda x:x[1],reverse=True) #对dict1.items() 为待排序的对象；key=lambda x: x[1] 为对前面的对象中的第二维数据（即value）的值进行排序
print(dict2)  
  
