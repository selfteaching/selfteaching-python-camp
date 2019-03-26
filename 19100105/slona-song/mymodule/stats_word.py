import collections
#-*- coding:utf-8 -*-
# -*- coding:gbk -*-
    
#定义注释函数
def annotation(string) -> '''This is a Word frequency searcher''':     #用文档字符串进行注释
    print("Annotation:",annotation.__annotations__) 


#定义中文检查器，同d6                      
def stats_text_cn(checkstr):
    try:
        if type(checkstr) != str:
            raise ValueError(checkstr)
    except ValueError as error:
        print(type(error))
        print("This data is not a string!")
    else:
        cndict={}
        count = 100
        # dict_text = []
        # init(dict_text)
        # splitstr = spl(checkstr,dict_text)
        for i in checkstr:
            if u'\u4e00' <= i <= u'\u9fff':
                cndict[i] = checkstr.count(i)
    #    cndict=sorted(cndict.items(),key=lambda item:item[1],reverse=True)
        cndict = collections.Counter(cndict).most_common(count)


        print(cndict)
        return cndict
    finally:
        print("executing finally stats_text_cn!")

# import re

# def init(dic):
    
#     with open("dictionary.txt",'rb') as test:
#         test = str(test)
#         text=re.findall(r'[【](.*?)[】]',test)

#         for i in text :
#             temp = i.split( )
#             dic.append(temp(0))

            

# def if_contain(words,dic):
#     flag = False
#     for d in dic:
#         if d == words:
#             flag = True
#             break
#     return flag


# def spl(string,dic):
#     result = ''
#     words = []
#     while len(string) > 0:
#         except_flag = False
#         for i in range(len(string),0,-1):
#             temp = string[:i]
#             flag = if_contain(temp,dic)
#             if flag:
#                 words.append(temp)
#                 string = string[:i]
#                 except_flag = True
#                 break
#         if not except_flag:
#             words.append(string)
#     for w in words:
#         result += (w + '/')
#     return result
                


#定义英文检查器，增加了查找英文字符的功能
def stats_text_en(checkstr):
    try:
        if type(checkstr) != str:
            raise ValueError(checkstr)
    except ValueError as error:
        print(type(error))
        print("This data is not a string!")
    else:
        endict={}               #新建一个字典
        entext=""               #新建一个空字符串
        count = 20 

        checkstr=checkstr.replace(',',' ').replace('.',' ').replace('--',' ').replace('!',' ').replace('*',' ')  #去标点

        #遍历原始字符串
        for i in checkstr: 
            if i.isascii():         #去掉中文或者说非英文字符
                entext=entext+i     #将英文字符放入新建的字符串中

        entext=entext.split( )      #分隔字符串

        for i in entext:            #遍历新字符串
            endict[i]=entext.count(i)        #创建字典
    #    endict=sorted(endict.items(),key=lambda item:item[1],reverse=True) #按照值排序，从小到大
        endict = collections.Counter(endict).most_common(count)
        print(endict)
        return endict
    finally:
        print("executing finally stats_text_en!")

#定义stats_text函数
def stats_text(string):
    try:
        if type(string) != str:
            raise ValueError(string)
    except ValueError as error:
         print(type(error)) 
         print("This data is not a string!")
    else:
        stats_text_cn(string)          #导入stats_text_cn函数
        stats_text_en(string)          #导入stats_text_en函数
        annotation(string)             #加入注释功能
    finally:
        print("executing finally stats_text!")
    
    

