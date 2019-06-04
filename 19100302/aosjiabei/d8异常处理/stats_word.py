import re#导入正则表达式模块
def stats_text_en(text):
   
    found = {}#建立空的字典
    a= text.lower()
    a=re.sub("[^\\u0061-\u007a]", " ", a)#小写字母unicode范围，筛选英文
    a=a.split()#指定分隔符对字符串进行切片
    
    for i in a:
        if i  in found:
            found[i]+=1
        else:
            found[i]=0
            found[i]+=1
    print('英文单词统计结果：',sorted(found.items(),key=lambda x:x[1],reverse=True))#词频降序
 
#统计中文词频

def stats_text_cn(text):
    found={}
    #提取中文字符串
    text= re.sub("[^\u4e00-\u9fa5]", "", text)#中文汉字unicode范围
    

    for i in text:
        if i  in found:
            found[i]+=1
        else:
            found[i]=0
            found[i]+=1

    print('中文汉字字频统计结果： ',sorted(found.items(),key=lambda x:x[1],reverse=True))


#调用stats_text_en , stats_text_cn 函数，合并统计结果

def stats_text(text):
    stats_text_en(text)
    stats_text_cn(text)




