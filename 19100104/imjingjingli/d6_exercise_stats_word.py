text = '''
来自百度的Python问题，Python是一种计算机程序设计语言。
Unless explicitly silenced.
面对起义，拒绝猜的诱惑.
'''
dict1 = {}
dict2 = {}
dict3 = {}
dict4 = {}


def stats_text_en(text):   #创建一个名为stats_text_en的函数
    import re
    text = re.sub("[^A-Za-z]", " ", text.strip())   #只保留英文
    list1 = re.split(r"\W+",text)   #将字符串text转换为列表list1,只保留单词为list1中的元素
    while '' in list1:   #删除list1中为空的列表元素
        list1.remove('')
    for i in list1:   
        dict1.setdefault(i,list1.count(i))  #将列表中的单词及单词的出现次数，分别赋值给dict1的键和值
    tup1 = sorted(dict1.items(),key = lambda items:items[1],reverse = True)   #将dict1按照value值从大到小排列，并将结果赋给元组tup1
    for tup1 in tup1:   
            dict2[tup1[0]] = dict1[tup1[0]]  
    return dict2
print(stats_text_en(text))
str = ''



#封装一个统计中文字频的函数

cndic={}                        #创建一个空的字典

def stats_text_cn(checkstr):    #定义检索中文函数
    for i in checkstr:          # 如果字典里有该单词则加1，否则添加入字典
        if u'\u4e00' <= i <= u'\u9fff':   #判断一个unicode是否是汉字
            cndic[i] = checkstr.count(i)   
    return cndic

#一个中英混杂的文本
text = '''                       
来自百度的Python问题，Python是一种计算机程序设计语言。
Unless explicitly silenced.
面对起义，拒绝猜的诱惑.
'''

stats_text_cn(text)             #调用检索中文频次的函数

cndic=sorted(cndic.items(),key=lambda item:item[1],reverse = True)      #检索完毕后对字典进行按值从大到小排序

print(cndic)                            
