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

#定义一个名字为stats_text_en的函数，功能为统计出现单词的个数
def stats_text_en(strText):
    #创建一个空字典用来统计单词个数
    dic={}
    #将文本中的非单词因素去掉
    text2=strText.replace("\n","").replace("."," ").replace("!","").replace("--","").replace("  "," ")
    #将文本按照一个空格切割
    list1=text2.split(" ")

    #遍历切割的列表
    for l1 in list1:
        #如果单词不在dic字典中，则设置为0
        count=dic.get(l1,0)
        count+=1
        dic[l1]=count
    #将dic转为dic.items()，根据单词出现个数排序，降序
    list2=sorted(dic.items(),key=lambda item:item[1],reverse=True)
    return list2

#封装统计中文汉字字频的函数
def stats_text_cn(textC):
    dic={}
    for ch in textC:
        #判断该字符是否是中文
        if ch>="\u4e00" and ch<="\u9fff":
            count=dic.get(ch,0)
            dic[ch]=count+1
    
    list3=sorted(dic.items(),key=lambda item:item[1],reverse=True)        
    print(list3)

stats_text_en(text)
stats_text_cn("我爱你 哦  啊 ha  哈哈哈")



