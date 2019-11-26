# day10 第三方库使用
# 2019年7月19日
# 陈浩 学号 1901100030

from collections import Counter
import jieba

# 定义字母统计函数，返回降序排列数组
def stats_text_en(text, count):
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
    # 调用counter函数
    return Counter(words).most_common(count)

# 统计参数中每个汉字出现的次数
def stats_text_cn(text, count):
    words = jieba.cut(text)
    tmp = []
    for word in words:
        if len(word) > 1:
            tmp.append(word)
    # 调用counter函数
    return Counter(tmp).most_common(count)

# 添加stats_text函数，调用stats_text_en和stats_text_cn函数，合并输出统计结果
def stats_text(text, count):
    if not isinstance(text, str):
        raise ValueError("参数必须是str类型，输入类型 %s" %type(text))
#   返回合并输出结果
    return stats_text_cn(text,count) + stats_text_en(text,count)

#测试程序
# if __name__ == "__main__":
#     en_result = stats_text_en(sample_text)
#     cn_result = stats_text_cn(cn_text)
# print(en_result)
# print(cn_result)