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
做个自驱动的人，而非被外部驱动的被动的人。
'''

dict1 = {}
dict2 = {}
dict3 = {}
dict4 = {}
  
def stats_text_en(text):                           # 定义一个名为stats_text_en的函数
    import re 
    text = re.sub("[^A-Za-z]", " ", text.strip())  # 使用正则表达式"[a-zA-Z]+"，将非英文字母替换成空字符
    list1 = re.split(r"\W+",text)                  # 将字符串text转换为列表list1,只保留单词为list1中的元素
    while '' in list1:                             # 删除list1中为空的列表元素
        list1.remove('')
    for i in list1:                                # i属于list1中的元素，开始循环
        dict1.setdefault(i,list1.count(i))         # 将列表中的单词及单词的出现次数，分别赋值给dict1的键和值
    # 将dict1按照value值倒序排列，并将结果赋给元组tup1
    tup1 = sorted(dict1.items(),key = lambda items:items[1],reverse = True)   
    for tup1 in tup1:   
            dict2[tup1[0]] = dict1[tup1[0]]  
    return dict2

#打印统计英文词频的结果
print("统计英文词频的结果为:")
print(stats_text_en(text))
str = ''

def feng_zhuang(s, old_d):                            # 封装函数
    d = old_d
    print(s,d)
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d
    

def stats_text_cn(text):                             # 定义一个名为stats_text_cn的函数
    import re
    text = re.sub("[A-Za-z0-9]", "", text)           # 使用正则表达式"[A-Za-z0-9]"，将非英文字母替换成空字符
    list1 = re.split(r"\W+",text)                    # 将字符串text转换为列表list1,只保留单词为list1中的元素
    while '' in list1:                               
        list1.remove('')                             # 删除list1中为空的列表元素
    dict3 = dict()                                   # 把dict3的行拆成字典
    for i in range(len(list1)):
        dict3 = feng_zhuang(list1[i], dict3)

    # 将dict3按照value值倒序排列，并将结果赋给元组tup1
    tup1 = sorted(dict3.items(),key = lambda items:items[1],reverse = True)  
    for tup1 in tup1:   
            dict4[tup1[0]] = dict3[tup1[0]]  
    return dict4

#打印统计中文词频的结果
print("统计中文词频的结果为:")
print(stats_text_cn(text))
