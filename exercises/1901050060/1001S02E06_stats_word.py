text= '''
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


# 封装统计单词词现的次数
# def stats_text_en(text):
#     text1 = text.replace(',', ' ').replace('.', ' ').replace('--', ' ').replace('!', ' ').replace('*', ' ')#清除不必要的字符
#     text2 = text1.split()
#     text3 = set(text2)#去重处理
#     dict2 = {}
#     for i in text3:
#         j = text.count(i)#单词计数
#         dict1 = {i: j}
#         dict2.update(dict1)#创建新字典
#     dict3 = sorted(dict2.items(), key=lambda x: x[1], reverse=True)#按照值进行排序
#     return dict3#返回值
# print(stats_text_en(text))  #打印测试


text_cn = '''
美丽胜过丑陋。
显式优于隐式。
简单比复杂更好。
复杂比复杂更好。
Flat优于嵌套。
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


def stast_text_cn(text_cn):
    text = text_cn.replace('。', '').replace('，', '').replace('-', '').replace('*', '').replace('!', '').replace('\n','').replace(' ','')
    d3 = {}
    for i in text:
        count = text.count(i)
        dict2 = {i:count}
        d3.update(dict2)
    d4 = sorted(d3.items(),key = lambda x:x[1],reverse = True)
    return d4

print(stast_text_cn(text_cn))