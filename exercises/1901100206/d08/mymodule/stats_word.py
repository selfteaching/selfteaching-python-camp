import re
#英文字符排序
def stats_text_en(text):
    #如果不是字符串，抛异常，异常会终止代码执行
    if not isinstance(text, str):
        raise TypeError ('输入有误, 请输入字符串')
    #如果没有抛出异常，代表是字符串
    en = re.sub(r'[^A-Za-z]',' ', text) #仅挑出英文字符，略过中文
    text_1 = en.lower().split() #组成列表
    dic = {}
    for key in text_1:   
        dic[key] = text_1.count(key)  #给text_2的键逐个计数，并储存它的值。
    dic_1 = sorted(dic.items(), key=lambda x: x[1], reverse=True) #reverse=True代表降序
    return dic_1       

 #中文字符排序
def stats_text_cn(text):
    if not isinstance(text, str):
        raise TypeError ('输入有误, 请输入字符串')
    cn = re.findall(r'[\u4E00-\u9FFF]', text) #\u4E00-\u9FFF代表取出中文字符
    dic = {}
    for char in cn:   #作用同上面英文排序
        dic[char] = cn.count(char)
    dic_1 = sorted(dic.items(), key=lambda x: x[1], reverse=True) 
    return dic_1

 #封装函数
def stats_text(text): #定义函数，实现统计汉字和英文单词出现次数
    if not isinstance(text, str):
        raise TypeError ('输入有误, 请输入字符串')
    return stats_text_en(text) + stats_text_cn(text)
