def stats_text_cn(text):  # 统计中文词频
    """Count the chinese words in the text """  # 使用文档字符串说明
    if not isinstance(text,str):     #如果不是字符串类型触发异常
        raise ValueError ("input data is not string type") 
    countcn = {}
    for i in text:
        if u'\u4e00' <= i <= u'\u9fff':
            countcn[i] = text.count(i)
    countcn = sorted(
        countcn.items(), key=lambda item: item[1], reverse=True)  # 按出现数字从大到小排列
    return countcn

def stats_text_en(text): #统计英文词频 
    """Count the english words in the text"""  #使用文档字符串说明
    if not isinstance(text, str):   #如果不是字符串类型，触发异常
        raise ValueError("input data is not string type")
    text = text.replace(',', ' ').replace('.', ' ').replace(   '--', ' ').replace('!', ' ').replace('*', ' ')  # 去除特殊字符
    text = text.lower()
    text = text.split()
    a = {}
    for i in text:
        quantity = text.count(i)
        b = {i: quantity}
        a.update(b)  
    a = sorted(a.items(), key=lambda x: x[1], reverse=True)
    return a


def stats_text(text):  # 合并中英文词频统计
        """combine the stats_text_cn and stats_text_en."""
        if not isinstance(text, str):    #如果不是字符串类型，触发异常
            raise ValueError("input data is not string type")
        a = stats_text_en(text)
        b = stats_text_cn(text)
        c = a+b
        print(c)

