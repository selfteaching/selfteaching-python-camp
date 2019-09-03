import re

#统计文件中的英文单词出现的次数

def stats_text_en(text,count_n):

    result = {}
     #替换特殊字符
    for sb in '!"@#$%^&*()+,-./:;<=>?@[\\]_`~{|}':
        text.replace(sb, ' ')
    
    text = text.replace(' ',',')
    en_pattern = re.compile(r'[a-zA-Z]+[\'\-]?[a-zA-Z]+')
    text = re.findall(en_pattern, text)
    textList = list(text)
 
    for i in text:
        result[i]=textList.count(i)
    print(result)
    
    return result

#中文统计
def stats_text_cn(text):

    if type(text) != str:
        raise ValueError('不是字符串类型')
        
    result = {}
     #替换特殊字符
    for sb in '!"@#$%^&*()+,-./:;<=>?@[\\]_`~{|};':
        text.replace(sb, ' ')
    cn_pattern = re.compile(r'[\u4e00-\u9fa5]')
    re.findall(cn_pattern, text)
    text = re.sub('[\\n]','',text)
    textList = list(text)

    for i in text:
        if(i != ' '):
             result[i]=textList.count(i)
    print(result)
    return result

#合并输出结果
def stats_text(text):
    stats_text_cn(text)
    #stats_text_en(text)