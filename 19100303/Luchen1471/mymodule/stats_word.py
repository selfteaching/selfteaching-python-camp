# this is d8 excercise for errors and exceptions
# date : 2019.3.25
# author by : qiming
# Luchen：延用上次作业，完善本次内容。+1


import collections
import re
import jieba


def stats_text_en(en,x): #还没找到方法限制x为int
    ''' 1. 英文词频统计。
        2. 参数类型检查，不为字符串抛出异常。
    '''    
    if type(en) == str : 
            text_en = re.sub("[^A-Za-z]", " ", en.strip())
            enList = text_en.split( )
            return collections.Counter(enList).most_common(x)
    else : 
            raise ValueError ('type of argumengt is not str')

def stats_text_cn(cn): #还没找到方法限制y为int,这次把20这个参数内置了#d11作业改成100
    ''' 1. 汉字字频统计 
        2. 参数类型检查，不为字符串抛出异常。
    '''
    if type(cn) == str : 
            #cnList0 = re.findall(u'[\u4e00-\u9fff]+', cn.strip())#d11看看能不能过滤网址源码里面的英文单词,做完了看到要求用pyquery
            #txt = ' '.join(cnList0)
            cn = re.sub(r'[^\w\s]','',cn)#试图去掉标点符号
            cnList = jieba.cut(cn)#默认精确模式
            #cnList1 = []
            #for i in cnList:
                    #if len(i) >= 3:
                        #cnList1.append(i)
            #cnString = ''.join(cnList)
            return collections.Counter(cnList).most_common(10)
    else :
            raise ValueError ('type of argumengt is not str')


#def stats_text(text_en_cn) :
#    ''' 1. 合并英汉词频统计 
#        2. 参数类型检查，不为字符串抛出异常。
#    '''
#    if type(text_en_cn) == str : 
#            return (stats_text_en(text_en_cn)+stats_text_cn(text_en_cn))
#    else :
#            raise ValueError ('type of argumengt is not str')

#print(stats_text_cn("我来到北京清华，。“”/n大学"))#试验成功

def text_strip(cn0):
        list1 = cn0.split( )
        i=0
        for i in range(0,len(list1)):
                list1[i]=list1[i].strip('，。“” \n')
                if list1[i]==' ': 
                        list1[i].remove(' ')
                else:
                        i=i+1
        #return str_cn0_stripped = ''.join(list1)
        return list1
