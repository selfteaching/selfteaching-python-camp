#第9天的添加
import re   #调用正則表達式 (regular expression)，字串處理module。
import collections  #调用collections
count=int()   #定义整数型变量count

##################################################################
#第8天的基础，找到一位学友的代码，非常简洁，copy了：）
# 使用“字典”统计文本中出现的单词次数，把结果从大到小输出
#\u4e00-\u9fa5 	漢字的unicode範圍
#\u0030-\u0039 	數字的unicode範圍
#\u0041-\u005a 	大寫字母unicode範圍
#\u0061-\u007a 	小寫字母unicode範圍
#def stats_text_en(text_en，count):   #定义函数，其中text是可变的量
#    if  isinstance(text_en,str):     ##如果不是字符串，抛出异常
#        #把en中非英文字符轉換成" "
#        t1=re.sub(u"([^\u0041-\u005a\u0061-\u007a])"," ",text_en)
#        #將text_en中非英文字符轉換成“”
#       text1=t1.split()    #分割字符串
#        d=collections.Counter(text1).most_common(count)
        #Counter计数器用法：most_common([n])（下一行python教程抄一遍：）
        #返回一个列表，提供 n 个频率最高的元素和计数。 如果没提供 n ，或者是 None ， most_common() 返回计数器中的 所有 元素。相等个数的元素顺序随机。
#        return d
#    else：
#        raise ValueError ("您输入的非字符串类型，请检查。")    

####################################################################################################################
#统计字符串中每个汉字出现的个数。输出的结果降序排列
#该函数用于统计字符串中每个汉字出现的个数。输出的结果按照降序排列，格式为以中文汉字及其字频为元组的一个字典
def stats_text_cn(text_cn):    #定义函数，参数text可变
    if not isinstance(text_cn,str):     ##如果不是字符串，抛出异常
	    raise ValueError ("您输入的非字符串类型，请检查。")   
    setb=set(text_cn)   #设定集合set，并把集合元素赋值给setb
    d = []   #设定列表
    for char in setb:        #char从集合setb中取值
	    if char >= u'\u4e00' and char <= u'\u9fa5':       #如果c是在u4e00 到u9fa5之间（汉字）
	        count=text_cn.count(char)     #统计每个汉字的数量
	        n=(char,count)
	        d.append(n)         #将y加到x列表中
    #x=sorted(d,key=lambda kv:kv[1],reverse=True)    #按重复次数，由大到小排列
    return collections.Counter(d).most_common(count)
    #return x    #返回排序x
    
######################################################################################################
def stats_text(text_join,count):   #将两个函数合并成一个函数。
#都有点怀疑python是不是太简单了，封装函数只是定义函数名+参数就行
    if isinstance(text_join,str):     #如果不是字符串，抛出异常
	    a=stats_text_cn(text_join,count)+stats_text_en(text_join,count)
        #还是惊讶于python的调用直接拼接
    else:    
        raise ValueError ("您输入的非字符串类型，请检查。")   