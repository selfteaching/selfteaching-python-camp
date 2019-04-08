
# coding: utf-8

# In[63]:


def stats_text_en (text):
    temp=text.replace(',','').replace('.','').replace('*','').replace('!','').replace(':','').replace('\n',' ').replace('\t','').replace('，','').replace('。','').replace('！','').replace('？','').strip().lower() #把特殊符号都去掉，并全部换成小写
    dit_en={}
    lst = temp.split(' ') #把字符串变为列表
    max = 0
    maxkey = ""
    for item in lst:
        if (dit_en.get(item)):
            dit_en[item] = dit_en[item] + 1 #如果读入的每个单词作为key存在对应的值，则累加
        else:
            dit_en[item] = 1 #如果读入的单词作为key没有找到对应的值，则赋值为1
        if (dit_en[item] > max): #如果每个单词的统计数大于最大值，则重新赋值给最大值，并把对应的key赋值给maxkey
            max = dit_en[item]
            maxkey = item
    result_en=sorted(dit_en.items(),key=lambda x:x[1],reverse=True) #按照value的值，从大到小排序
    return result_en

 # -*- coding: utf-8 -*- 
def stats_text_cn (text):
    item=text.replace('，','').replace('。','').replace('！','').replace('？','').replace('\n','').replace('\t','') #去掉特殊符号
    dit_cn={}
    max = 0
    maxkey = ""
    for i in range(len(item)):
        if (dit_cn.get(item[i])):
            dit_cn[item[i]] = dit_cn[item[i]] + 1 #如果读入的字作为key存在对应的值，则累加
        else:
            dit_cn[item[i]] = 1 #如果读入的字作为key没有找到对应的值，则赋值为1
        if (dit_cn[item[i]] > max): #如果字的统计数大于最大值，则重新赋值给最大值，并把对应的key赋值给maxkey
            max = dit_cn[item[i]]
            maxkey = item
    result_cn=sorted(dit_cn.items(),key=lambda x:x[1],reverse=True) #按照value的值，从大到小排序
    return result_cn


def stats_text(text):
    list_cn=[]     
    for char in text:
        if (char >= u'\u4e00' and char<=u'\u9fa5') or (char >= u'\u0041' and char<=u'\u005a') or (char >= u'\u0061' and char<=u'\u007a') or (char >= u'\u0030' and char<=u'\u0039'): #判断一个字符是否为标点符号
            if char >= u'\u4e00' and char<=u'\u9fa5' :#如果是中文，则统一放进list_cn中，标点符号全部去掉
                list_cn.append("".join(char))  
            else: 
                continue 
        else: 
            continue
    for t in range(len(list_cn)):
        w1=list_cn[t]
        text=text.replace(w1,"") #把原文件中的中文字符逐一去掉，这样text中只保留了英文单词
    text_cn= "".join(list_cn) #再把只包含中文的列表转成字符串，为调用函数做准备
    result=stats_text_cn(text_cn)+stats_text_en(text) #把两次调用函数的结果列表合并后统一输出
    return result

    
  

