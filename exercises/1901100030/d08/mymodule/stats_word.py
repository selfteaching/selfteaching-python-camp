# day8 异常处理
# 2019年7月14日
# 陈浩 学号 1901100030

sample_text = '''
The Zen of Python, by Tim Peters

Beautiful is better than ugly. 
Explicit is better than implicit.
Simple is better than complex. 
Complex is better than complicated. 
Flat is better than nested. 
Sparse is better than dense. Readability counts. 
Special cases aren't special enough to break the rules. 
Although practicality beats purity. 
Errors should never pass silently. 
Unless explicitly silenced. 
In the face of ambxiguity, refuse the temptation to guess. 
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch. 
Now is better than never. 
Although never is often better than *right* now. 
If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
cn_text = '''
14天python训练营欢迎您!
锦瑟无端五十弦
一弦一柱思华年
沧海月明珠有泪
蓝田日暖玉生烟
'''
# 定义字母统计函数，返回降序排列数组
def stats_text_en(text):
    if not isinstance(text, str):
        raise ValueError("参数必须是str类型，输入类型 %s" %type(text))
    elements = text.split()
    # 定义新存储变量
    words = []
    # 定义待剔除的符号
    symbols = ",.*-!"
    # 遍历所有元素，剔除特殊符号
    for element in elements:
        for symbol in symbols:
            element = element.replace(symbol,"")
        if len(element) and element.isascii():
            words.append(element)
    # print(words)
    # 初始化字典
    counter = {}
    # 定义集合，剔除重复元素，降低遍历次数
    words_set = set(words)
    #print(words_set)
    #根据单词进行遍历、统计
    for word in words_set:
        counter[word] = words.count(word)
    # print(counter)
    # 按照出现次数，进行排序，并输出
    return sorted(counter.items(), key=lambda x:x[1], reverse=True )
#print(stats_text_en(sample_text))

# 统计参数中每个汉字出现的次数
def stats_text_cn(text):
    if not isinstance(text, str):
        raise ValueError("参数必须是str类型，输入类型 %s" %type(text))
    # 定义新存储变量
    cn_characters = []
    #遍历字符串，取出所有汉字
    for character in text:
        if "\u4e00" <= character <= "\u9efff":
            cn_characters.append(character)
    # 初始化字典
    counter = {}
    # 定义集合，剔除重复元素，降低遍历次数
    characters_set = set(cn_characters)
    #print(words_set)
    #根据单词进行遍历、统计
    for character in characters_set:
        counter[character] = cn_characters.count(character)
    # print(counter)
    # 按照出现次数，进行排序，并输出
    return sorted(counter.items(), key=lambda x:x[1], reverse=True )

# 添加stats_text函数，调用stats_text_en和stats_text_cn函数，合并输出统计结果
def stats_text(text):
    if not isinstance(text, str):
        raise ValueError("参数必须是str类型，输入类型 %s" %type(text))
#   返回合并输出结果
    return stats_text_cn(text) + stats_text_en(text)

#测试程序
# if __name__ == "__main__":
#     en_result = stats_text_en(sample_text)
#     cn_result = stats_text_cn(cn_text)
# print(en_result)
# print(cn_result)