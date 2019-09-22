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

#封装统计英文单词词频的函数
#定义一个名为 stats_text_en 的函数，函数接受一个字符串 text 作为参数
#统计参数中每个英文单词出现的次数，最后返回个按词频降序排列的数组
#为 stats_text_en 添加注释说明
def stats_text_en(text):
    for i in ('""*,-.!'): 
        text=text.replace(i,'')
    list=text.split() 
    dict = {}
    for word in list:
        if word not in dict:
            dict[word] = 1
        else:
            dict[word] += 1
    count_dict=sorted(dict.items(),key=lambda x:x[1],reverse=True) 
    print(count_dict)
stats_text_en(text) 

#封装统计中⽂文汉字字频的函数
#定义一个名为 stats_text_cn 的函数，函数接受⼀个字符串 text 作为参数
#实现该函数的功能:统计参数中每个中文汉字出现的次数，最后返回⼀个按字频降序排列的数组
#为 stats_text_cn 添加注释说明
text1='''
But man is not made for defeat.
A man can be destroyed but not defeated.
但人不是为失败而生的.
一个人可以被毁灭，但不能被打败.
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