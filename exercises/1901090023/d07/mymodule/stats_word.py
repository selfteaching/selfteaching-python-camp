
# 将统计中文词频和英文词频的函数封装为一个模块

# 1. 封装统计英文单词次数的函数
def stats_text_en(text):                   # 定义函数，形式参数名为text
    """ 函数名：stats_text_en               # 文档字符串用来为函数添加注释说明

    参数名：text
    统计参数中英文单词词频
    最后返回一个按词频降序排列的数组
    """
    
    text1 = text.replace(';', '').replace('.', '')     # 去掉字符串中的特殊符号
    list1 = text1.split()                              # 字符串转换为列表
   
    d={}                                               # 创建一个空字典d
    for i in list1:                                    # for循环遍历列表, i 为列表中的各个元素
        d[i]=list1.count(i)                            # list1.count(i)是i 单词元素在列表中的次数，将其赋值给字典d中key为i单词元素的value值
    d1=sorted(d.items(),key=lambda x:x[1],reverse=True) # items() 函数以列表返回可遍历的(键, 值) 元组数组；sorted()函数，通过key参数，指定第二个字段（value值）的值的降序来排序
    return d1                                           # python 函数返回值 return，函数中一定要有return返回值才是完整的函数。              【非常重要】


# 2. 封装统计中文汉字字频的函数
def stats_text_cn(text):         # 定义函数，用来统计中文汉字字频，并且给函数名添加注释说明
    """ 函数名：stats_text_cn                 # 文档字符串用来为函数添加注释说明

    参数名：text
    统计参数中中文汉字词频
    最后返回一个按词频降序排列的数组
    """

    text = text.replace('。','').replace('、','').replace('', ' ')    # 前两个去掉特殊符号，最后一个是把字符串拆成一个个汉字 【非常重要】
    list1 = text.split()                    # 将字符串转换为列表

    characters = []
    for character in list1:
        if len(character):                       # 如果charater的长度不为0，则算作正常汉字
            characters.append(character)          # characters列表中添加中文汉字元素
    charanum = {}
    character_set = set(characters)              # 去掉列表中重复汉字元素后的集合

    for hanzi in character_set:
        charanum[hanzi] = characters.count(hanzi)
    return sorted(charanum.items(), key=lambda x: x[1], reverse=True)
       

# 3. 添加名为stats_text的函数，实现分别调用stats_text_en, stats_text_cn的功能
def stats_text(text):
    """ 函数名：stats_text

    参数名：text
    实现分别调用stats_text_en, stats_text_cn的功能
    """
    return stats_text_en(text) + stats_text_cn(text) 

