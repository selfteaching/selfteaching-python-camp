# 19100304 day8 银零
# 为 my.module 下 stats_word.py 中的三个个函数添加参数类型检查，如果输入参数不为字符串类型则抛出 ValueError 错误，并包含完整的错误提示信息

# 19100304 day7 银零
# 1.定义 stats_text 函数，实现功能：分别调用stats_text_en, stats_text_cn, 输出合并词频统计结果
# 2.为 stats_text 添加注释说明



# 这是一个封装统计英文单词词频的函数，并按词频降序排列数组

def stats_text_en(string):
    if type(string) == str:                             #检查输入值是否为字符串类型
        import re                                       #导入正则表达式模块
        list1 = re.split(r'\W+',string)                 #将字符串转换为列表list1，只保留单词为list1中的元素
        while '' in list1:                              #删除list1中为空的元素
            list1.remove('')
        dict1 = {}                                      #建立空的字典
        for i in list1:                                 #i属于list1中的元素，开始循环
            dict1.setdefault(i,list1.count(i))          #将列表中的单词及单词的出现次数，分别赋值给dict1的键和值
        tup1 = sorted(dict1.items(),key = lambda items:items[1],reverse = True)             #将dict1按照value值从大到小排列，并将结果赋值给元祖tup1
        print(tup1)
        return tup1                                     #输出tup1的值
    else:                                               #若输入值不是字符串类型
        raise ValueError('输入值不是字符串')


# 这是一个封装统计中文汉字字频的函数，并按字频降序排列数组

def stats_text_cn(string):
    if type(string) == str:                             #检查输入值是否为字符串类型
        import re                                       #导入正则表达式模块
        result_cn_interpunction = re.sub('[^\u4e00-\u9fa5]','',string)                      #提取中文字符串
        string = string.replace(' ','').replace('\n','')#删除空元素与换行元素
        list1 = re.split('',string)                     #将字符串转换为列表list1
        dict1 = {}                                      #建立空的字典
        for i in list1:                                 #i属于list1中的元素，开始循环
            dict1.setdefault(i,list1.count(i))          #将列表中的汉字及汉字的出现次数，分别赋值给dict1的键和值
        tup1 = sorted(dict1.items(),key = lambda items:items[1],reverse = True)             #将dict1按照value值从大到小排列，并将结果赋值给元祖tup1
        print(tup1)                                     #输出tup1的值
    else:                                               #若输入值不是字符串类型
        raise ValueError('输入值不是字符串')


# 定义 stats_text 函数，功能是分别调用 stats_text_en 与 stats_text_cn 函数并合并输出词频统计结果

def stats_text(string):
    if type(string) == str:                             #检查输入值是否为字符串类型
        stats_text_en(string)
        stats_text_cn(string)
    else:                                               #若输入值不是字符串类型
        raise ValueError('输入值不是字符串')
