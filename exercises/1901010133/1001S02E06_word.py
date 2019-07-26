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
    dict = {}  # 建立字典
    for word in list:
        if word not in dict:  # 如果单词不在字典中
            dict[word] = 1    # 初始词频为1
        else:
            dict[word] += 1   # 每次单词出现，词频加1
    count_dict=sorted(dict.items(),key=lambda x:x[1],reverse=True) #字典是个无序的结构，最终返回的是一个没有排序的列表。 
    print(count_dict) #输出排序后的字典                             #key=lambda x:x[1] 其中X表示某一迭代出来的元素，其实是个元组，
stats_text_en(text)                                                #而x[1] 表示元组的第二个元素，即单词的次数(词频)，
      #若要按照单词排序则改成key=lambda x:x[0]即可。
  
text1='''
one is always on a strange road, watching strange scenery
and listening to strange music.then one day ,you will find
that the things you try hard to forget are already gone 
一个人总要走陌生的路，看陌生的风景，听陌生的歌，然后在某个不经意的瞬间，
你会发现，原本你想费尽心机想要忘记的事情，真的就没了。
'''
def stats_text_cn(text): #自定义函数:统计汉字词频
    dict1={}
    for i in text:
        if u'\u4e00'<=i<= u'\u9fff': #提取中文
        #计算机中所有的字符都是用数字来表示的。汉字也是用数字表示的，
        #Unicdoe4E00~9FFF表示中文
        #if u'a' <= ch <= u'z' or u'A' <= ch <= u'Z':提取英文
            count=text.count(i)
            dict2={i:count}
            dict1.update(dict2)
    dict1=sorted(dict1.items(),key=lambda item:item[1],reverse=True) #先引用吧，慢慢再弄懂它，现在不懂
    return dict1
print(stats_text_cn(text1)) 



