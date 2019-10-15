
# 使用jieba第三方库，优化中文词频统计函数的功能
import jieba   # 导入第三方库，jieba中文分词
import re      # re模块来使用正则表达式，正则表达式匹配中文
from collections import Counter          # 使用collections模块下的Counter计数器函数


# 1. 封装统计英文单词次数的函数
def stats_text_en(text, count:int):            # 定义函数，形式参数名为text，增加int类型的变量count，用于限制输出元素的个数
    if not isinstance(text, str):                       # type()用来判断参数类型，还有一种方法是 if type(text) != str: 
        raise ValueError('Invalid text! Not a string!')   # 用户自定义异常为ValueError

    text1 = text.replace(';', '').replace('.', '')     # 去掉字符串中的特殊符号
    list1 = text1.split()                              # 字符串转换为列表
    
    from collections import Counter             # 使用collections模块下的Counter计数器函数
    c_en = Counter(list1)                       # Counter对象（记住，是dict的子类）的key是待计数元素，value是对应的计数
    return c_en.most_common(count)              # 用变量count来限制输出最高词频元素的个数

  

# 2. 封装统计中文汉字字频的函数
def stats_text_cn(text,count:int):         # 定义函数，形式参数名为text，增加int类型的变量count，用于限制输出元素的个数
    if isinstance(text, str):                       # 表示text参数类型为字符串。另外type()用来判断参数类型，还要一种方法是 if type(text) != str: 
        cn_list = re.findall(u'[\u4e00-\u9fff]+', text)   # 正则表达式re.findall方法能够以列表的形式返回能匹配的子串。这行代码意思是找所有的汉字，但不一定是单个，因为正则中+代码一个或者多个
        cn_str = ''.join(cn_list)                      # 把列表中各个元素拼接生成新的字符串，每个元素没有间隙地进行拼接【注意''无空格就是直接拼接，有空格就是以空格拼接】  
        cn_jieba = [x for x in jieba.cut(cn_str) if len(x) >= 2]    # 分词后的长度大于等于2。len(x) >= 2就是词组
        c_cn = Counter(cn_jieba)                    # Counter对象（记住，是dict的子类）的key是待计数元素，value是对应的计数
        return c_cn.most_common(count)           # 用变量count来限制输出最高词频元素的个数（python 函数返回值 return，函数中一定要有return返回值才是完整的函数）

# 笔记：视频讲解的代码如下：
# def stats_text_cn(text, count):
#     words = jieba.cut(text)
#     tmp = []
#     for i in words:
#         if len(i) > 1:
#             tmp.append(i)
#     return Counter(tmp).most_common(count)



# 3. 添加名为stats_text的函数，对提取结果进行分析和词频统计处理
def stats_text(text,count:int):                             # 形式参数名为text，增加int类型的变量count，用于限制输出元素的个数
    if not isinstance(text, str):                       # type()用来判断参数类型，还要一种方法是 if type(text) != str: 
        raise ValueError('Invalid text! Not a string!')
        
    return stats_text_cn(text,count)                   # 只对中文分词进行分析和词频统计，因此返回stats_text_cn函数的结果



