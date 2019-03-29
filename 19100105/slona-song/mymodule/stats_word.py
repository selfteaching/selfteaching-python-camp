import collections

import jieba
#-*- coding:utf-8 -*-
# -*- coding:gbk -*-
    
#定义注释函数
def annotation(string) -> '''This is a Word frequency searcher''':     #用文档字符串进行注释
    print("Annotation:",annotation.__annotations__) 


#定义中文检查器，同d6                      
def stats_text_cn(checkstr,count):
    try:
        if type(checkstr) != str:
            raise ValueError(checkstr)
    except ValueError as error:
        print(type(error))
        print("This data is not a string!")
    else:
        cndict={}
        cnstr=""
        

        for i in checkstr:                      #遍历原始字符串
            if u'\u4e00' <= i <= u'\u9fff':     #判断是否是中文
                cnstr=cnstr+i                   #讲中文写入到一个新的字符串中

        seg_list=jieba.cut(cnstr,cut_all=False,HMM=False)       #使用导入的外部结巴分词库，对字符串进行分词

        string = "/".join(seg_list)             #分好的词再以字符串的形式合并，原来的seg_list是生成器，生成的是元组
        string = string.split("/")              #对字符串再进行分割，就像分割英文一样
        

        for i in string:                        #遍历分割后的字符串
            if len(i) >= 2:                     #挑选长度大于2的词
                cndict[i] = string.count(i)     #写入字典

            
                
    #    cndict=sorted(cndict.items(),key=lambda item:item[1],reverse=True)
        cndict = collections.Counter(cndict).most_common(count)


        print(cndict)
        return cndict
    finally:
        print("executing finally stats_text_cn!")



#定义英文检查器，增加了查找英文字符的功能
def stats_text_en(checkstr,count):
    try:
        if type(checkstr) != str:
            raise ValueError(checkstr)
    except ValueError as error:
        print(type(error))
        print("This data is not a string!")
    else:
        endict={}               #新建一个字典
        entext=""               #新建一个空字符串
        
        
        checkstr=checkstr.replace(',',' ').replace('.',' ').replace('--',' ').replace('!',' ').replace('*',' ')  #去标点
        
        #遍历原始字符串
        for i in checkstr: 
            if i.isascii():         #去掉中文或者说非英文字符  
                entext=entext+i     #将英文字符放入新建的字符串中

        entext=entext.split( )      #分隔字符串

        for i in entext:            #遍历新字符串
            endict[i]=entext.count(i)        #创建字典
    #    endict=sorted(endict.items(),key=lambda item:item[1],reverse=True) #按照值排序，从小到大
        endict = collections.Counter(endict).most_common(count)         #使用collection的counter方法，按照词频进行排序
        print(endict)
        return endict
    finally:
        print("executing finally stats_text_en!")

#定义stats_text函数
def stats_text(string,n):
    try:
        if type(string) != str:
            raise ValueError(string)
    except ValueError as error:
         print(type(error)) 
         print("This data is not a string!")
    else:
        stats_text_cn(string,n)          #导入stats_text_cn函数
        stats_text_en(string,n)          #导入stats_text_en函数
        annotation(string)             #加入注释功能
    finally:
        print("executing finally stats_text!")
    return stats_text_cn(string,n)+stats_text_en(string,n)



 

    

