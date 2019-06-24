text = '''hello, world 你好，世界'''

def stats_text_cn(text, count):  # 统计中文词频，增加变量count控制输出
    """Count the chinese words in the text """  # 使用文档字符串说明
    from collections import Counter  # 调用Counter计数器
    import jieba
    if not isinstance(text, str):  # 如果不是字符串类型触发异常
        raise ValueError("input data is not string type")
    text = [x for x in jieba.cut(text) if len(x) >= 2]  #使用精确模式分词
    countcn = {}
    count = int(count)
    for i in text:
        if u'\u4e00' <= i <= u'\u9fff':
            countcn[i] = text.count(i)

    countcn = Counter(countcn).most_common(count)  # 按词频排序并用count控制输出
    return countcn


def stats_text_en(text, count):  # 统计英文词频，增加变量count控制输出
    """Count the english words in the text"""  # 使用文档字符串说明
    from collections import Counter  # 调用Counter计数器
    import re
    if not isinstance(text, str):  # 如果不是字符串类型，触发异常
        raise ValueError("input data is not string type")
    text = re.sub("[^A-Za-z]", " ", text.strip())  #确保是英文
    text = text.replace(',', ' ').replace('.', ' ').replace(
        '--', ' ').replace('!', ' ').replace('*', ' ')  # 去除特殊字符
    text = text.lower()
    text = text.split()
    count = int(count)
    a = {}
    for i in text:
        quantity = text.count(i)
        b = {i: quantity}
        a.update(b)
    a = Counter(a).most_common(count)  # 按词频排序并用count控制输出
    return a


def stats_text(text,count):  # 合并中英文词频统计
        """combine the stats_text_cn and stats_text_en."""
        if not isinstance(text, str):    #如果不是字符串类型，触发异常
            raise ValueError("input data is not string type")
        a = stats_text_en(text,count)
        b = stats_text_cn(text,count)
        c = a+b
        return c