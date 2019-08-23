import re  #使用正则表达式，自己想了很久没法在中英文中进行英文排序
def stats_text_en(text):  
    #此函数的功能是统计参数中的英文单词的频次，并且按照词频从高到低排序输出
    text = text.lower()
    text = re.sub("[^A-Za-z]", " ", text) #这个正则表达式表示只保留英文单词，其他字符串剔除
    text = text.split()
    d = {}   
    for i in text:    
        a = text.count(i)
        d[i] = a  
    d1 = sorted(d.items(), key = lambda item : item[1], reverse = True)
    return d1

def stats_text_cn(text):
    #此函数的功能是统计参数中的中文单词的频次，并且按照词频从高到低排序输出
    text1 = []  
    for cn in text:     
        if '\u4e00' <= cn <= '\u9fa5':  
            text1.append(cn)
    d = {}  
    for zh in text1:
        d[zh] = text1.count(zh)  
    d1 = sorted(d.items(), key = lambda item : item[1], reverse = True) 
    return d1

def stats_text(text):
    print("文本中的中文汉字词频为：\n",stats_text_cn(text))
    print("文本中的英文单词词频为：\n",stats_text_en(text))
    return