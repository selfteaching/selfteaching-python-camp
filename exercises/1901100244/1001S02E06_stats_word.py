# -*- coding: UTF-8 -*-

# Filename : 1001S02E05_string.py
# author by : @shen-huang

# 函数的用法


def stats_text_en(text: str) -> str:
    import re  # 加载正则表达式模块
    from nltk.tokenize import regexp_tokenize  # 加载正则表达式分词函数

    pattern = r"""             # 设置以编写较长的正则条件
        (?x)(?:[A-Z]\.)+       # 缩略词
        |\$?\d+(?:\.\d+)?%?    # 货币、百分数
        |\w+(?:[-']\w+)*       # 用连字符链接的词汇
        |\.\.\.                # 省略符号
        |(?:[.,;"'?():-_`])    # 特殊含义字符
        """

    # 去掉 text 里的多余符号和空格，添加分词用空格，全文转为小写
    text2 = re.sub(r",|\*|!", " ", text)
    text2 = re.sub("—", " ", text2)
    text2 = re.sub("([0-9A-Za-z]*)['’]([0-9A-Za-z]*)", "\\1 ’\\2", text2)
    text2 = re.sub("\n", " ", text2)
    text2 = re.sub(" +", " ", text2)
    text2 = str.lower(text2)

    # 分词，去掉空元素，排序
    text3 = regexp_tokenize(text2, pattern)
    text3 = [i for i in text3 if i != '' and i != '.']
    text3 = sorted(text3)

    # 生成非重复单词列表
    text4 = []
    [text4.append(w) for w in text3 if w not in text4]

    # 生成词频统计字典
    text_freq = {w: text3.count(w) for w in text4}

    # 按词频排序
    text_freq = sorted(text_freq.items(), key=lambda x: x[1], reverse=True)
    text_freq = dict(text_freq)

    # 返回数组
    return text_freq


def stats_text_cn(text: str) -> str:
    import re  # 加载正则表达式模块

    # 去掉 text 里除汉字外的符号
    text2 = re.sub(r"[^\u4e00-\u9fa5]", "", text)

    # 分词，排序
    text3 = re.split("", text2)
    text3 = sorted(text3)

    # 生成非重复汉字列表
    text4 = []
    [text4.append(w) for w in text3 if w not in text4]

    # 生成字频统计字典
    text_freq = {w: text3.count(w) for w in text4}

    # 按字频排序
    text_freq = sorted(text_freq.items(), key=lambda x: x[1], reverse=True)
    text_freq = dict(text_freq)

    # 返回数组
    return text_freq
