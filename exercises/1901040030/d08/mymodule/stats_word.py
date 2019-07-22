import re
re_en = re.compile(r'[\u0061-\u007a,\u0020]') #用正常表达式获取所有的英文和空格，为了能达到单词需要保留空格
re_cn = re.compile(r'[\u4E00-\u9FA5]') #用正常表达式获取所有的汉字

def stats_text_en (text:'输入的文本') -> list:
    if not isinstance(text,str):
        raise ValueError('stats_text_en函数需要的参数是字符串')
    en_text=''.join(re_en.findall(text))  #截取英文和空格，拼接成带单词的字符串
    en_text_list=en_text.split() #截取出单词，存在列表里
    en_text_dict={} #存储英文单词的字典
    for word in en_text_list:
        if word in en_text_dict.keys():
            en_text_dict[word]=en_text_dict[word]+1
        else:
            en_text_dict[word]=1
    en_text_list=sorted(en_text_dict.items(),key=lambda item:item[1],reverse=True) #iteam()里包含key和value，后面的表达式是按value排序
    return en_text_list 


def stats_text_cn (text:'输入的文本') -> list:
    if isinstance(text,str):
        raise ValueError('stats_text_cn函数需要的参数是字符串')
    cn_text_list=re_cn.findall(text)  #截取中文部分
    cn_text_dict={} #存储中文的字典
    for word in cn_text_list:
        if word in cn_text_dict.keys():
            cn_text_dict[word]=cn_text_dict[word]+1
        else:
            cn_text_dict[word]=1
    cn_text_list=sorted(cn_text_dict.items(),key=lambda item:item[1],reverse=True) #按value排序
    return cn_text_list
     
    

def stats_text (text:'输入的文本') -> list:
    if isinstance(text,str):
        raise ValueError('stats_text函数需要的参数是字符串')
    text_list=stats_text_cn(text) #运行统计中文的函数
    text_list.extend(stats_text_en(text)) #运行统计英文的函数
    return text_list
