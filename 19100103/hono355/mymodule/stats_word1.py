template = '''
The Zen of Python, by Tim Peters
美丽 is better than 丑陋.
清楚 is better than 含糊.
简单 is better than 复杂.
复杂 is better than 难懂.
单一 is better than 嵌套.
稀疏 is better than 稠密.
可读性计数.
Special cases aren't special enough to 打破规则.
即使练习会使得不再纯粹.
但错误不应该用沉默来掩盖.
Unless explicitly silenced.
面对起义，拒绝猜的诱惑.
有且只有一个办法.
Although that way may not be obvious at first unless you're Dutch.
尝试总比从未试过要强.
Although never is often better than *right* now.
如果执行很难被解释，那将是一个很糟的想法.
如果执行很容易解释，这会是一个好点子.
Namespaces are one honking great idea -- 让我们继续为之努力!
'''
from collections import Counter
import jieba


def test(text):
    if not isinstance(text, str):
        raise ValueError('The type of text is not string')

def test(count):
    if not isinstance(count, int):
        raise TypeError('The type of count is not int')

def stats_text_en(text, count):
    #统计英文词频的函数
    word_en = "".join(i for i in text if ord(i) < 256)    #分离出文本中的英文
    for i in '*,，。.-!、？！“”""?「」':
        word_en = word_en.replace(i,'')    #去掉标点等符号
    word_en = word_en.lower()    #将所有大写变成小写，以便后面单词计数
    word_en_list = word_en.split()    #将text的字符串以空格为分隔符分割成字符串并赋值
    word_en_counter = Counter(word_en_list).most_common(count)    #用Counter计数排序，返回指定个数频率最高的元素及计数
    result = word_en_counter
    print('stats_text_en =>', result)
    return result
    

def stats_text_cn(text, count):
    #统计中文词频的函数
    word_cn = "".join(i for i in text if ord(i) >= 256)    #分离出文本中的中文
    for i in '*,，。.-!、？！“”""?「」:：':
        word_cn = word_cn.replace(i,'')    #去掉标点等符号

    word_cn_list = [x for x in jieba.cut(word_cn, cut_all=False) if len(x) >= 2]
    word_cn_counter = Counter(word_cn_list).most_common(count)    #用Counter计数排序，返回指定个数频率最高的元素及计数
    result = word_cn_counter
    print('stats_text_cn => ', result)
    return result


def stats_text(text, count):
    #调用stats_text_en与stats_text_cn函数，输出合并词频统计结果
    result = stats_text_en(text, count) + stats_text_cn(text, count)
    print('stats_text => ', result)
    return result





   
def main():
    stats_text_en(template, None)
    stats_text_cn(template, None)
    stats_text(template, None)
    

if __name__ == '__main__':
    main()




