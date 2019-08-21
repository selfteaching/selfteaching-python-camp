import re

def stats_text(text):
    if type(text) != str:
        raise ValueError('非字符串类型')
    list_en = stats_text_en(text)
    list_cn = stats_text_cn(text)
    list_all = sorted((list_en+list_cn), key = lambda x:x[1], reverse=True)
    return list_all

def stats_text_en(text):
    word_list = re.findall(r'\b[a-z]+\'?[a-z]+',text.lower())
    count_dict = {}
    for word in word_list:
        count_dict[word] = word_list.count(word)
    list_en = sorted(count_dict.items(), key=lambda x:x[1], reverse=True)
    return list_en

def stats_text_cn(text):
    text_cn = re.sub(r'[\wa-zA-Z0-9]','',text)
    count_dict = {}
    for character in text_cn:
        count_dict[character] = text_cn.count(character)
    list_cn = sorted(count_dict.items(), key = lambda x:x[1], reverse=True)
    return list_cn




    if type(text)!= str:
        raise ValueError('非字符串类型')
    
# 测试非字符串参数的执行结果
# text = True
# text = '大法啊都是范德萨 大发动机 的卅饭店 adf fd fd tony apple sick 我是中国人 阿道夫fdsa 12344'
# print(stats_text(text))