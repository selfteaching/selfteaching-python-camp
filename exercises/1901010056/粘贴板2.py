import  re 

import  collections  
text = '''                        
Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex.
好好学习天天向上，学习学习再学习,pony6666
'''
#英文词频统计函数

def  stats_text_en(text):

    a=re.sub(r'[^A-Za-z]',' ',text)    #只取英文单词

    newlist=a.split()                      #单词划分

    return(collections.Counter(newlist))  #输出英文单词频数统计结果

print(collections.Counter(text))

#中文词频统计函数

def  stats_text_cn(text):

    p =  re.compile(r'[\u4e00-\u9fa5]')  # 中文的编码范围是：\u4e00到\u9fa5

    res = re.findall(p, text)   #取中文

    newcn=''.join(res)

    return(collections.Counter(newcn))  #输出中文词频统计结果
print(collections.Counter(text))