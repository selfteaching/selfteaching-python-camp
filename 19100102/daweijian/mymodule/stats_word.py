# 封装d5的代码
import re


def clean_ip_list(words):  # 清理掉空格 标点符号
    i = 0
    while i < len(words):
        words[i] = words[i].strip('*-.')
        if words[i] == '':  # 清洗完成之后若为空元素‘’，则删除元素
            words.remove('')
        else:
            i = i + 1
    return words


def cut_clean(s):
    # 切分字符串
    s = s.split()
    # 清洗标点符号
    clean_ip_list(s)
    return s


# 把list转化为dict并统计词频
def list_dict(l):
    cadiz = {}
    b = True  # 是否是英文
    for word in l:
        for char in word:
            if ('\u0041' <= char <= '\u005a') or ('\u0061' <= char <= '\u007a'):  # 字符是英文
                b = True
                break
            else:  # 存在一个字符非英文 所以整个词非英文单词
                b = False
                break
        if (b):
            if word in cadiz:
                cadiz[word] += 1
            else:
                cadiz[word] = 1
    return cadiz


def stats_text_en(s):
    if isinstance(s, str):
        s = cut_clean(s)  # 切分字符串并清洗标点符号
        s_dict = list_dict(s)  # 将tempiate转化为字典并统计词频
        # 对字典按照value值排序
        s_s_dict = sorted(s_dict.items(), key=lambda item: item[1], reverse=True)
        print(s_s_dict)
    else:
        raise ValueError("is not str")
    return s_s_dict


def cut_count_cn(c, regex):  # 取出所有中文 是一个列表
    words = regex.findall(c)  # 对整段文字进行分词
    words = clean_ip_list(words)  # 分词后去掉空格标点符号
    cadiz = {}
    for word in words:  # 取出每一个词语
        for char in word:  # 取出每个词语中的每一个词
            if '\u4e00' <= char <= '\u9fff':  # 如果是中文
                if char in cadiz:
                    cadiz[char] += 1
                else:
                    cadiz[char] = 1
    return cadiz


def stats_text_cn(s):  # 定义检索中文函数
    if isinstance(s, str):
        regex = re.compile("(?x)(?: [\w -]+ | [\x80 -\xff]{3} )")
        words = cut_count_cn(s, regex)
        s_s_dict = sorted(words.items(), key=lambda item: item[1], reverse=True)
        print(s_s_dict)
    else:
        raise ValueError("is not str")
    return s_s_dict


# 定义stats_text函数
def stats_text(s):
    stats_text_cn(s)  # 导入stats_text_cn函数
    stats_text_en(s)  # 导入stats_text_en函数
