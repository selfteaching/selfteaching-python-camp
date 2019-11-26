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
def stats_text_en(text):#自定义函数:统计英语单词词频
    for i in ('""*,-.!'): 
        text=text.replace(i,'') #去除文章中的符号
    list=text.split() 
    dict = {}  # 建立空字典
    for word in list:
        if word not in dict:  # 如果单词不在字典中
            dict[word] = 1    # 初始词频为1
        else:
            dict[word] += 1   # 每次单词出现，词频加1
    count_dict=sorted(dict.items(),key=lambda x:x[1],reverse=True) #字典是个无序的结构，最终返回的是一个列表，没有排序。 
    print(count_dict) #输出排序后的字典   #key=lambda x:x[1]其中X表示某一迭代出来的元素，其实是个元组，                                            #而x[1] 表示元组的第二个元素，即单词的次数(词频)，
     #若要按照单词排序则改成key=lambda x:x[0]即可。