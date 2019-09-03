
import re                     #引入正则表达式
def stats_text_en(en):        #定义一个函数
    #\u4e00-\u9fa5 	汉字的unicode范围
    #\u0030-\u0039 	数字的unicode范围
    #\u0041-\u005a 	大写字母unicode范围
    #\u0061-\u007a 	小写字母unicode范围
    #sub(pattern,repl,string) 	把字符串中的所有匹配表达式pattern中的地方替换成repl
    t1= re.sub(u"([^\u0041-\u005a\u0061-\u007a])"," ",en) #将en中非英文字符转换成“ ”
    text1 = t1.split() #将字符串分割
    d = {} #创建一个空字典
    for i in text1: #循环遍历
        if i in d:
            d[i] += 1 #如果字典中没有就显示1，有的话就在原来的基础上+1
        else:
            d[i] = 1

    a = sorted(d.items(),key=lambda x:x[1],reverse = True) #利用lambda函数进行values值的排序
    return a


def stats_text_cn(cn): #定义一个统计中文汉字字频的函数
    t = re.sub(u"([^\u4e00-\u9fa5])","",cn) #将cn中非中文字符转换成“”
    d = {}
    for i in t:     #中文不需要分割，可以直接遍历！！！！！
        if i in d:
            d[i] +=1
        else:
            d[i] =1
    a = sorted(d.items(),key=lambda x:x[1],reverse = True)
    return a


def stats_text(j): #定义合并输出函数
    a = stats_text_cn(j) + stats_text_en(j) #将两次统计结果合并
    return a
