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


#第一步替换better和worse
text2=text.replace('better','worse') 


#第二步删除包含ea的单词
text3=text2.replace('.',' ').replace('*',' ').replace('!',' ').replace('--',' ') #删掉标点  
text3_list=text3.split() #将str转换成列表
for i in text3_list:
    if 'ea' in i:  #找到包含ea的项，删除
        text3_list.remove(i)
text4=' '.join(text3_list) #将列表重新转换成str。新的str不换行啊。

#第三步大小写互换
text5=text4.swapcase()

#第四步排序
text5_list=text5.split()
text5_list.sort()
for i in text5_list:
    print(i)
