
# coding: utf-8

# In[14]:


def stats_text_en (text):
    temp=text.replace(',','').replace('.','').replace('!','').replace(':','').replace('\n',' ').strip().lower() #把特殊符号都去掉，并全部换成小写
    dit={}
    lst = temp.split(' ') #把字符串变为列表
    max = 0
    maxkey = ""
    for item in lst:
        if (dit.get(item)):
            dit[item] = dit[item] + 1 #如果读入的每个单词作为key存在对应的值，则累加
        else:
            dit[item] = 1 #如果读入的单词作为key没有找到对应的值，则赋值为1
        if (dit[item] > max): #如果每个单词的统计数大于最大值，则重新赋值给最大值，并把对应的key赋值给maxkey
            max = dit[item]
            maxkey = item
    result=sorted(dit.items(),key=lambda x:x[1],reverse=True) #按照value的值，从大到小排序
    return result

text='''this is a dog.
That is a cat.
that is a duck.'''
stats_text_en(text)

 # -*- coding: utf-8 -*- 
def stats_text_cn (text):
    item=text.replace('，','').replace('。','').replace('！','').replace('？','') #去掉特殊符号
    dit={}
    max = 0
    maxkey = ""
    for i in range(len(item)):
        if (dit.get(item[i])):
            dit[item[i]] = dit[item[i]] + 1 #如果读入的字作为key存在对应的值，则累加
        else:
            dit[item[i]] = 1 #如果读入的字作为key没有找到对应的值，则赋值为1
        if (dit[item[i]] > max): #如果字的统计数大于最大值，则重新赋值给最大值，并把对应的key赋值给maxkey
            max = dit[item[i]]
            maxkey = item
    result=sorted(dit.items(),key=lambda x:x[1],reverse=True) #按照value的值，从大到小排序
    return result

text='''门前大桥下，游过一只鸭，快来快来数一数，二四六七八。'''
stats_text_cn(text)
