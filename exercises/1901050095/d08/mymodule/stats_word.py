# 使用“字典”统计以上文本中出现的单词次数，并把结果从大到小输出
text=123456     #输入数字，检查非字符串出错异常
def stats_text_en(text):   #定义函数，其中text是可变的量
    if not isinstance(text,str):     ##如果不是字符串，抛出异常
	    raise ValueError ("您输入的非字符串类型，请检查。")    
    text = text.replace(',',' ').replace('.',' ').replace('--',' ').replace('*',' ').replace('!',' ') # 去标点
    text = text.lower() # 全部换成小写
    text = text.split() # 拆成字符串
    d = {} #定义字典
    for i in text:    #遍历文本text
        count = text.count(i) # 数单词i个数
        r1 = {i:count} # 定义字典r1，单词在前，词频在后
        d.update(r1) #上传r1到d中去
    d = sorted(d.items(),key=lambda x:x[1],reverse=True)    #最终字典d里面元素排序
    return d    #返回字典d


####################################################################################################################

#该函数用于统计字符串中每个汉字出现的个数。输出的结果按照降序排列，格式为以中文汉字及其字频为元组的一个字典
def stats_text_cn(text):    #定义函数，参数text可变
    if not isinstance(text,str):     ##如果不是字符串，抛出异常
	    raise ValueError ("您输入的非字符串类型，请检查。")   
    setb=set(text)   #设定集合set，并把集合元素赋值给setb
    d = []   #设定列表
    for char in setb:        #char从集合setb中取值
	    if char >= u'\u4e00' and char <= u'\u9fa5':       #如果c是在u4e00 到u9fa5之间（汉字）
	        count=text.count(char)     #统计每个汉字的数量
	        n=(char,count)
	        d.append(n)         #将y加到x列表中
    x=sorted(d,key=lambda kv:kv[1],reverse=True)    #按重复次数，由大到小排列
    return x    #返回排序x
    
######################################################################################################

def stats_text(text):   #将两个函数合并成一个函数。
                    #都有点怀疑python是不是太简单了，封装函数只是定义函数名+参数就行
    if not isinstance(text,str):     ##如果不是字符串，抛出异常
	    raise ValueError ("您输入的非字符串类型，请检查。")      
    print('\n按照出现次数降序输出所有单词:\n')
    print(stats_text_en(text),'\n')
    print('\n按照出现次数降序输出所有汉字:\n')
    print(stats_text_cn(text),'\n')     
#该函数用于统计字符串中英文单词和汉字出现的个数。输出的结果按照降序排列，格式为以单词、汉字及其字频为元组的一个字典