import re

def stats_text_en(t): #定义函数，参数为t
    if not isinstance(t,str): #如果t不是字符串
        raise ValueError('wrong operand type') #则报错
    else: #如果t是字符串
        t = t.lower() #文本转小写
        t_list = t.split() #文本转列表
        t_dict = {} #新建一个空字典
        for i in t_list: #指定i遍历上述列表
            ii = i.strip(' ,.*!-') #清洗i中元素
            if ii not in t_dict: #如果单词不在新建字典中
                t_dict[ii] = 1 #则字典添加单词
            else: #如果单词已在新建字典中
                t_dict[ii] = t_dict[ii] + 1 #则该单词对应的计数增加1
        t_dict_sorted = sorted(t_dict.items(),key = lambda x:x[1],reverse = True) #items()函数用于把字典转为元组；key=lambda x:x[1]用于设定键按值大小排列；reverse=True用于设定键按降序排列
        return t_dict_sorted #返回函数结果



def stats_text_cn(t): #定义函数，参数为t
    if not isinstance(t,str): #如果t不是字符串
        raise ValueError('wrong operand type') #则报错
    else: #如果t是字符串
        t_list = [] #新建一个空列表
        t_dict = {} #新建一个空字典
        exclude_str = '\n ，。！？/”“「」:\',[]' #新建一个字符串,备用（将要消除的中文符号）
        for char in t: #遍历文本中的字节
            t_list.append(char) #把拆解的所有字节（包括单个汉字和符号）放入新建的列表中
        for char in t_list: #遍历列表中的元素
            if char not in exclude_str: #如果该字节为汉字，不是符号
                if char.strip() not in t_dict: #又如果（strip(）用于消除空格）汉字不在新建的字典中
                    t_dict[char] = 1 #则字典添加汉字
                else: #如果汉字已在字典中
                    t_dict[char] = t_dict[char] + 1 #则对字典中该单词对应的计数增加1
        t_dict_sorted = sorted(t_dict.items(),key = lambda x:x[1],reverse = True)#items()函数用于把字典转为元组；key=lambda x:x[1]用于设定键按值大小排列；reverse=True用于设定键按降序排列
        return t_dict_sorted #返回函数结果



def stats_text(t):
    if not isinstance(t,str): #如果t不是字符串
        raise ValueError('wrong operand type') #则报错
    else: #如果t是字符串
        a = re.sub(r'[^A-Za-z]',' ',t)
        stats_text_en(a)
        b = [i for i in t if '\u4e00' <= i <= '\u9fa5']
        b = str(b) #这里再次把列表转化为字符串
        stats_text_cn(b)
        return (print(stats_text_en(a) + stats_text_cn(b)))