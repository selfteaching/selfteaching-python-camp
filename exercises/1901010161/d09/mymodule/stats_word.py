import re    # 调用正则表达式
import collections
count = int()


def stats_text_en(text, count):  # 定义英语文本统计函数
    if type(text) == str:
        m = re.sub(r'[^A-Za-z]', ' ', text)    # 将text中任意非字母成分替换为空
        stri = m.split()        # 切分英文单词，建立字符串
        return(collections.Counter(stri).most_common(count))
    else:
        raise ValueError('type of argument is not string')


def stats_text_cn(text, count):     # 定义中文文本统计函数
    if type(text) == str:
        p = re.compile(r'[\u4e00-\u9fa5]')    # 中文基本汉字（20902字）的编码范围是：\u4e00到\u9fa5
        res = re.findall(p, text)   # 获取所有中文字符
        return(collections.Counter(res).most_common(count))
    else:
        raise ValueError('type of argument is not string')


def stats_text(text, count):     # 定义文本统计函数
    if type(text) == str:
        return(stats_text_en(text, count) + stats_text_cn(text, count))    # 输出合并英文和中文词频统计结果
    else:
        raise ValueError('type of argument is not string')
