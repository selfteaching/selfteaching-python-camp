import jieba
from collections import Counter
def stats_text_en(text):
    """
    统计英⽂单词词频的函数
    """
    if not isinstance(text, str):
        raise ValueError("参数必须是str类型，输入类型%s" % type(text))
    a_text = text.split()
    b_words = []
    c_text = ".,!?*-"
    for d_text in a_text:
        for e_text in c_text:
            d_text = d_text.replace(e_text,"")
            # error: 函数replace没有拼对。
        # error: d_text名称前后没有保持一致。
        if len(d_text) and d_text.isascii():
            b_words.append(d_text)
    return b_words

def stats_text_cn(text,count):
    """
    统计中⽂汉字字频的函数
    """
    if not isinstance(text, str):
        raise ValueError("参数必须是str类型，输入类型%s" % type(text))
    words = jieba.cut(text)
    tmp = []
    for i in words:
        if len(i) > 1:
            tmp.append(i)
    return Counter(tmp).most_common(count)

def stats_text_text(text,count):
    """
    综合统计英⽂单词词频和中⽂汉字字频的函数,中英⽂词频统计的排序功能,使函数能够按照词频出现的次数有序输出。
    """
    a_text = stats_text_en(text) + stats_text_cn(text,9)
    from collections import Counter
    cnt = Counter()
    for b_word in a_text:
        cnt[b_word] += 1
    return cnt.most_common(count)

text = '''
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Sparse is better than dense.
封装统计英文文文单词词频的函数,封装统计中文汉字字频的函数.
'''

if __name__ == '__main__':
    print("词频统计的函数:\n",stats_text_text(text,9))