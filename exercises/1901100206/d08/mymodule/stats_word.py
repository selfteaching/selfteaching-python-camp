#英文字符排序
def stats_text_en(text):    
    import re
    if isinstance(text, str) is True:
        en = re.sub(r'[^A-Za-z]',' ', text) #仅挑出英文字符，略过中文
        text_1 = en.lower().split() #组成列表
        dic = {}
        for key in text_1:   
            dic[key] = text_1.count(key)  #给text_2的键逐个计数，并储存它的值。
        dic_1 = sorted(dic.items(), key=lambda x: x[1], reverse=True) #reverse=True代表降序
        return dic_1 
    else:
        raise TypeError ('输入有误, 请输入字符串')

 #中文字符排序
def stats_text_cn(text):
    import re
    if isinstance(text, str) is True:
        cn = re.findall(r'[\u4E00-\u9FFF]', text) #\u4E00-\u9FFF代表取出中文字符
        dic = {}
        for char in cn:   #作用同上面英文排序
            dic[char] = cn.count(char)
        dic_1 = sorted(dic.items(), key=lambda x: x[1], reverse=True) 
        return dic_1
    else:
        raise TypeError ('输入有误, 请输入字符串')

 #封装函数
def stats_text(text): #定义函数，实现统计汉字和英文单词出现次数
    if isinstance(text, str) is True:
        print(stats_text_en(text))
        print(stats_text_cn(text))
    else:
        raise TypeError ('输入有误, 请输入字符串')