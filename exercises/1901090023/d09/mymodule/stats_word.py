
# 用标准库中的Counter完善stats_word模块中词频统计的排序功能

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
    if not isinstance(text, str):                       # type()用来判断参数类型，还要一种方法是 if type(text) != str: 
        raise ValueError('Invalid text! Not a string!')

    list1 = []
    for hanzi in text:
        #unicode中 汉字 字符的编码范围
        if '\u4e00' <= hanzi <= '\u9fff':    #英文单词是用空格分开的，中文汉字是连在一起的，区分一个汉字字符的方法：每个汉字都有相对应的unicode编码，其取值范围就是这个
            list1.append(hanzi)              # 往list1列表中不断添加text中的汉字字符

    from collections import Counter          # 使用collections模块下的Counter计数器函数
    c_cn = Counter(list1)                    # Counter对象（记住，是dict的子类）的key是待计数元素，value是对应的计数
    return c_cn.most_common(count)           # 用变量count来限制输出最高词频元素的个数（python 函数返回值 return，函数中一定要有return返回值才是完整的函数）


# 3. 添加名为stats_text的函数，实现分别调用stats_text_en, stats_text_cn的功能
def stats_text(text,count:int):                             # 形式参数名为text，增加int类型的变量count，用于限制输出元素的个数
    if not isinstance(text, str):                       # type()用来判断参数类型，还要一种方法是 if type(text) != str: 
        raise ValueError('Invalid text! Not a string!')
        
    return stats_text_en(text,count) + stats_text_cn(text,count) 



