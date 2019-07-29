
# coding: utf-8

# In[25]:


from collections import Counter
import re
def stats_text_en (text,count):
    text,count=checktype(text,count)
    temp=text.replace(',','').replace('.','').replace('*','').replace('!','').replace(':','').replace('\n',' ').replace('\t','').replace('，','').replace('。','').replace('！','').replace('？','').strip().lower() #把特殊符号都去掉，并全部换成小写
    dit_en={}
    list_en = temp.split(' ') #把字符串变为列表
    max = 0
    maxkey = ""
    for item in list_en:
        if (dit_en.get(item)):
            dit_en[item] = dit_en[item] + 1 #如果读入的每个单词作为key存在对应的值，则累加
        else:
            dit_en[item] = 1 #如果读入的单词作为key没有找到对应的值，则赋值为1
        if (dit_en[item] > max): #如果每个单词的统计数大于最大值，则重新赋值给最大值，并把对应的key赋值给maxkey
            max = dit_en[item]
            maxkey = item
    result_en=sorted(dit_en.items(),key=lambda x:x[1],reverse=True)[:count] #按照value的值，从大到小排序
    return result_en

 # -*- coding: utf-8 -*- 
def stats_text_cn (text,count):
    text,count=checktype(text,count)
    item=text.replace('，','').replace('。','').replace('！','').replace('？','').replace('\n','').replace('\t','').replace(' ','') #去掉特殊符号
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
    result_cn=sorted(dit_cn.items(),key=lambda x:x[1],reverse=True)[:count] #按照value的值，从大到小排序
    return result_cn


def stats_text(text,count):
    text,count=checktype(text,count)
    list_cn=[]     
    for char in text:
        if (char >= u'\u4e00' and char<=u'\u9fa5') or (char >= u'\u0041' and char<=u'\u005a') or (char >= u'\u0061' and char<=u'\u007a') or (char >= u'\u0030' and char<=u'\u0039'): #判断一个字符是否为标点符号
            if char >= u'\u4e00' and char<=u'\u9fa5' :#如果是中文，则统一放进list_cn中，标点符号全部去掉
                list_cn.append("".join(char))  
            else: #如果是数字和字母，则统一放进list_en中，标点符号全部去掉
                continue #如果是汉字，就把汉字逐个放进list_cn中
        else: 
            continue
    for t in range(len(list_cn)):
        w1=list_cn[t]
        text=text.replace(w1,"").replace(',','').replace('.','').replace('*','').replace('!','').replace(':','').replace('\n',' ').replace('\t','').replace('，','').replace('。','').replace('！','').replace('？','').strip()
    text_cn= "".join(list_cn)
    list_en=text.split(" ")
    result_list=list_en+list_cn
#     result=stats_text_cn(text_cn)+stats_text_en(text)
    return(Counter(result_list).most_common(count))


def checktype(x,count):
    if not isinstance(x,str):
        raise ValueError('input a string!')
    elif not isinstance(count,int):
        raise ValueError('input a int!')
    else:
        return x,count


# text='''o ehoig gweohi shio. 我是一只小小小小鸟'''
# stats_text_cn(text,3)
# try:
#     print(stats_text(text))
# except ValueError:
#     print("Oops!  Input was no valid string.  Try again...")
# print("done")




# In[94]:



  

