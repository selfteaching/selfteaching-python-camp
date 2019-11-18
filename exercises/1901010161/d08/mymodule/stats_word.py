import re    # 调用正则表达式


def stats_text_en(text):  # 定义英语文本统计函数
    if type(text) == str:
        m = re.sub(r'[^A-Za-z]', ' ', text)    # 将text中任意非字母成分替换为空
        stri = m.split()        # 切分英文单词，建立字符串
        wordcount = {}         # 建立字典
        for i in stri:
            wordcount[i] = stri.count(i)
        wordcount = sorted(wordcount.items(), key=lambda x: x[1], reverse=True)
        return wordcount      # 原来这里只写了return，系统虽然没报错，但输出时结果最后面有个none，没明白错误出在哪里，经老师提醒改正后果然没有none了
    else:
        raise ValueError('type of argument is not string')


def stats_text_cn(text):     # 定义中文文本统计函数
    if type(text) == str:
        p = re.compile(r'[\u4e00-\u9fa5]')    # 中文基本汉字（20902字）的编码范围是：\u4e00到\u9fa5
        res = re.findall(p, text)   # 获取所有中文字符
        wordcount = {}
        for i in res:
            wordcount[i] = res.count(i)     # 词频统计词典设置
        wordcount = sorted(wordcount.items(), key=lambda x: x[1], reverse=True)
        return wordcount
    else:
        raise ValueError('type of argument is not string')


def stats_text(text):     # 定义文本统计函数
    if type(text) == str:
        return(stats_text_en(text) + stats_text_cn(text))    # 输出合并英文和中文词频统计结果
    else:
        raise ValueError('type of argument is not string')
