#用函数做词频统计
#text = '''xx xxx xx xxx aa a aa a a a a a a xx xxx..;.;.;难难难男女就难就难仅仅难就难你a-zA-Z]+[\'\-]?[a-zA-Z'''


#英文词频排序
def stats_text_en(text1):
    #创建一个字典
    count = {}

# 把字符串去掉转行、大写换小写、去掉单词两边字符
    text = text1.replace(',','').replace('.','').replace(':','').replace(';','').replace('"','').replace('!','').replace('?','').replace('、','').replace('，','').replace('。','').replace('“','').replace('”','').replace('：','').replace('；','').replace('\n','').replace('！','').replace('？','').replace('/','').lower().split(' ')

 #去掉中文字符   
    import re
    en_pattern = re.compile(r'[a-zA-Z]+[\'\-]?[a-zA-Z]+')
    text_en = re.findall(en_pattern, text1)

    # 如果字典里有该单词则词频+1，否则添加入字典
    for word in text_en:
        if word in count.keys():
            count[word] = count[word] + 1
        else:
            count[word] = 1
    #按照词频从高到低排列
    count_list=sorted(count.items(),key=lambda a:a[1],reverse=True)
    return count_list
#print ("单词出现频率排列如下：",state_text_en(text))


#中文字频排序
def stats_text_cn(text2):

#去掉符号    
    text = text2.replace('—','').replace(' ','').replace(',','').replace('.','').replace(':','').replace(';','').replace('"','').replace('!','').replace('?','').replace('、','').replace('，','').replace('。','').replace('“','').replace('”','').replace('：','').replace('；','').replace('\n','').replace('！','').replace('？','').replace('/','')
#建立字典
    count = {}

 #去掉英文字符   
    import re
    cn_pattern = re.compile(r'[\u4e00-\u9fa5]')
    text_cn = re.findall(cn_pattern, text2)

#用for循环做字频统计    
    for word in text_cn:
        if word in count.keys():
            count[word] = count[word] + 1
        else:
            count[word]=1
#调整排序并输出
    count_list = sorted(count.items(),key=lambda a:a[1],reverse=True)
    return count_list
#输出
#print ("字出现频率排列如下：",state_text_cn(text))

#定义stats_text函数，合并输出
def stats_text(text):
    #用isinstance（变量名，类型）判断字符串类型是否正确，如果不正确抛出ValueError
    if isinstance(text,str) != True:
        raise ValueError
    else:
        return (stats_text_en(text),stats_text_cn(text))

#print ("单词出现频率排列如下：",stats_text(text))