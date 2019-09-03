from collections import Counter
import jieba

# 统计参数中每个英文单词出现的次数
# 定义函数
def stats_text_en(text,count):
    # 先将字符串根据 空白字符 分割成 list，要调用 str 类型
    elements = text.split()
    # 定义一个新的 list 型变量，存储处理过得单词
    words=[]
    # 先针对样本文本挑选出需要剔除的非单词符号
    symbols = ', . * !'
    # 遍历一遍要剔除的符号
    for element in elements:
        # 逐个替换字符号，用‘’是为了同时剔除符号所占的位置
        for symbol in symbols:
            element = element.replace(symbols,'')
    # 用str类型的isascii方法判断是否是英文单词
        if len(element) and element.isascii():
            words.append(element)
    return Counter(words).most_common(count)

    # 统计参数中每个中文汉字出现的次数
    # 定义函数
def stats_text_cn(text,count):
    words = jieba.cut(text)
    tmp = []
    for i in words:
        if len(i)>1:
            tmp.append(i)
    return Counter(tmp).most_common(count)

def stats_text(text,count):
    '''
    合并英文词频和中文字频的结果
    '''
    if not isinstance(text,str):
        raise ValueError('参数必须是str类型，输入类型 %s' % type(text))
    return stats_text_en(text,count) + stats_text_cn(text,count)

