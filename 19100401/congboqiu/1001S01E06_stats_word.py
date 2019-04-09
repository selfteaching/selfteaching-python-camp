'输入任何一段英文文档，得到降序排列的词频数组'
':'
def stats_text_en(text):
    """统计参数中每个英文单词出现的次数，最后返还一个按词频降序排列的数组"""
    textlist1 = text.split()#形成单词列表
    textlist2 = []
    for i in textlist1:
        if i.isalpha():
            textlist2.append(i)#去除非单词

    list1 = textlist2.count(0)
    print(list1)

    dict1 = {}
    dict1 = dict1.fromkeys(textlist2)#将textlist2的元素作为dict1的键值key
    word_1 = list(dict1.keys())
    for i in word_1:
        dict1[i] = textlist2.count(i)#统计单词出现的次数
    dict2 = {}
    dict2 = sorted(dict1.items(),key=lambda d:d[1],reverse=True)#按values进行排序
    dict2 = dict(dict2)#转化为字典
    return dict2
    print(dict2)


stats_text_en( "The Zen of Python, by Tim Peters Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested. Sparse is better than dense. Readability counts. Special cases aren't special enough to break the rules. Although practicality beats purity. Errors should never pass silently. Unless explicitly silenced. In the face of ambxiguity, refuse the temptation to guess. There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch. Now is better than never. Although never is often better than *right* now. If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea -- let's do more of those! ")

def stats_text_cn(a):
    #统计参数中每个中文汉字出现的次数，最后返回一个按字频降序排列的数组
    dict1 = {}
    for i in a:
        if u'\u4e00' <= i <= u'\u9fff': #判断一个unicode是否是汉字
            dict1[i] = a.count(i)
        
    dict1 = sorted(dict1.items(),key=lambda item:item[1],reverse=True)  #创建以键值对为元素的元组
    dict1 = dict(dict1)#转化为字典
    return dict1                      
<<<<<<< HEAD
    print(dict1)               
a='morining我的个to省啊mingh妈the妈啊，你usa的良心komi大大的花了啊,很ah好,我爱ao you are my borther你time，你是我的nkkal爱人啊'
=======
    print(dict1)            
    
a = input('morining我的个to省啊mingh妈the妈啊，你usa的良心komi大大的花了啊,很ah好，我爱ao you are my borther你time，你是我的nkkal爱人啊')
>>>>>>> parent of 87738a28... 111
stats_text_cn(a)