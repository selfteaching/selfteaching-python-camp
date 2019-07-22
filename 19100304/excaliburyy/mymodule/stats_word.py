# 19100304 day10 银零
# 1.通过 jieba 精确模式将 stats_text_cn 函数的输入字符串进行分次
# 2.统计分词完成之后的词频（中文词只同级长度大于等于2的词）
# 3.输出tang300.json 文件内容中的词频前20的词和词频数


# 19100304 day9 银零
# 1.使用标准库中的 counter 函数，使 stats_word 函数能够按照词频出现的次数有序输出
# 2.分别给两个函数添加一个 int 类型变量 count, 用于限制输出元素的个数

# 19100304 day8 银零
# 为 my.module 下 stats_word.py 中的三个个函数添加参数类型检查，如果输入参数不为字符串类型则抛出 ValueError 错误，并包含完整的错误提示信息

# 19100304 day7 银零
# 1.定义 stats_text 函数，实现功能：分别调用stats_text_en, stats_text_cn, 输出合并词频统计结果
# 2.为 stats_text 添加注释说明



from collections import Counter

# 这是一个封装统计英文单词词频的函数，并按词频降序排列数组

def stats_text_en(string):
    if type(string) == str:                             #检查输入值是否为字符串类型
        import re                                       #导入正则表达式模块
        import collections
        list1 = re.split(r'\W+',string)                 #将字符串转换为列表list1，只保留单词为list1中的元素
        while '' in list1:                              #删除list1中为空的元素
            list1.remove('')
        result = collections.Counter(list1).most_common(100)                     #使用 counter 函数统计元素出现次数；使用 most_common 函数使结果按照频率最高的100个元素和其计数输出为列表                 
        return result
    else:                                               #若输入值不是字符串类型
        raise ValueError('输入值不是字符串')


# 这是一个封装统计中文汉字字频的函数，并按字频降序排列数组

def stats_text_cn(string,count):
    if type(string) == str:                             #检查输入值是否为字符串类型
        import re                                       #导入正则表达式模块
        import collections
        import jieba        
        result_cn_interpunction = re.sub('[^\u4e00-\u9fa5]','',string)                      #提取中文字符串
        string = string.replace(' ','').replace('\n','')#删除空元素与换行元素
        list1 = jieba.lcut(string,cut_all=False)
        for i in list1:
            if len(i)>=2:
                list1.append(i)
            else:
                pass
        result = collections.Counter(list1).most_common(count)        
        return result                                   #使用 counter 函数统计元素出现次数；使用 most_common 函数使结果按照频率最高的100个元素和其计数输出为列表                 
    else:                                               #若输入值不是字符串类型
        raise ValueError('输入值不是字符串')


# 定义 stats_text 函数，功能是分别调用 stats_text_en 与 stats_text_cn 函数并合并输出词频统计结果

def stats_text(string):
    if type(string) == str:                             #检查输入值是否为字符串类型
        stats_text_en(string)
        stats_text_cn(string)
    else:                                               #若输入值不是字符串类型
        raise ValueError('输入值不是字符串')
