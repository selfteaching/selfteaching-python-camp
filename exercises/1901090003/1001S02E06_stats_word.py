
import re
# 封装统计英文单词词频的函数
def stats_text_en(text):
    # 如果不是字符串，给出提示
    if not isinstance(text,str):
        return '请输入字符串'

    # 1.替换掉所有的符号
    word_str = text.replace(',','').replace('.','').replace('!','').replace('*','').replace('--','')
    # 2.按照空格将所有的单词分割开
    word_list = word_str.split()
    # 3.对单词进行去重操作，作为字典的key
    word_one = set(word_list)
    # 4.构建一个词频字典
    dict = {}
    for word in word_one:
        dict[word] = word_list.count(word)
    # 5.对之前的词频字典按照value值进行排序
    d_list = sorted(dict.items(),key=lambda e:e[1],reverse=True)
    return d_list

# 封装统计中文汉字字频的函数
def stats_text_cn(text):
    # 如果不是字符串，给出提示
    if not isinstance(text,str):
        return '请输入字符串'

    # 1.首先将乱七八糟的符号去掉，方便之后的匹配
    d = text.replace(',','').replace('-',' ').replace('.','').replace(':','').replace(';','').replace('"','').replace('!','').replace('?','').replace('、','').replace('，','').replace('。','').replace('“','').replace('”','').replace('：','').replace('；','').replace('\n','').replace('！','').replace('？','').replace('/','').replace('*',' ').replace(' ','').replace("'",'')
    # 2.将上面字符串中的英文以及数字替换为空，即删除
    d = re.sub("[A-Za-z0-9]", "", d)
    print(d)
    # 3.将字符串中的汉字去重，作为字典的key
    d_list = list(d)
    print(d_list)
    d_index = set(d_list)
    # 4.构造词频字典
    dict = {}
    for i in d_index:
        dict[i] = d_list.count(i)
    # 5.对之前的词频字典按照value值进行排序
    d_list = sorted(dict.items(),key=lambda e:e[1],reverse=True)
    return d_list

if __name__ == "__main__":
    # 测试统计英文单词词频的函数
    text = '''
    The Zen of Python, by Tim Peters
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambxiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!
    '''
    # 测试不是字符串的情况
    test_num = 1
    # 测试正常情况
    array = stats_text_en(text)
    print(array)

    # 测试统计中文词频的函数
    text = '''
    The Zen of Python, by Tim Peters
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambxiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!
    美丽胜过丑陋。
    显式优于隐式。
    简单比复杂更好。
    复杂比复杂更好。
    优于嵌套。
    稀疏优于密集。
    可读性很重要。
    特殊情况不足以打破规则。
    虽然实用性胜过纯洁。
    错误不应该默默地传递。
    除非明确沉默。
    面对困惑，拒绝猜测的诱惑。
    应该有一个 - 最好只有一个 - 明显的方法来做到这一点。
    虽然这种方式起初可能并不明显，除非你是荷兰人。
    现在比永远好。
    虽然现在永远不会比*正确好。
    如果实施很难解释，这是一个坏主意。
    如果实现很容易解释，那可能是个好主意。
    命名空间是一个很棒的主意 - 让我们做更多的事情吧！
    '''
    # 对统计中文词频函数进行测试
    array = stats_text_cn(text)
    print(array)

