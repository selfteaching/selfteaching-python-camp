import re
def stats_text_en(text):
    """统计输入文本中的英文字频，从大到小排序"""
    if type(text)!=str:
        raise ValueError("Could not deal with this data,please check it and try again.")
    scope_en="[a-zA-Z]+" #提取英文单词
    list_en=re.findall(scope_en,text) #将提取的英文放入列表
    dic={}
    for it in list_en:
        if it not in dic:
            dic[it] = 1
        else: dic[it] += 1###统计词频
    dic = sorted(dic.items(),key=lambda x:x[1],reverse=True)#排序
    return dic
  
################################
def stats_text_cn(text):
    """统计输入文本中的中文字频，从大到小排序"""
    if type(text)!=str:
        raise ValueError("Could not deal with this data,please check it and try again.")
    dic2={}
    for i in text:
        if u'\u4e00' <= i <= u'\u9fa5':   #提取中文汉字   
            dic2[i]=text.count(i)
    dic3=sorted(dic2.items(),key=lambda x:x[1],reverse=True)
    return dic3
    
def stats_txt(text):
    if type(text)!=str:
        raise ValueError("Could not deal with this data,please check it and try again.")
    dicall={}#创建空字典
    dic_en=stats_text_en(text)#提取英文单词及词频，创建字典en
    dic_cn=stats_text_cn(text)#提取中文字及字频，创建字典cn
    dicall.update(dic_en)#将字典en并入总字典中
    dicall.update(dic_cn)#将字典cn并入总字典中
    dicall1=sorted(dicall.items(),key=lambda x:x[1],reverse=True)#对总字典排序
    return dicall1


