text1 = '''
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated. 9 Flat is better than nested.
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

text2 = '''
列表中的元素可以是不同类型。不过，在解决现实问题的时候，
我们总是倾向于创建由同一个类型的数据构成的列表。
遇到由不同类型数据构成的列表，我们更可能做的是想办法！把不同类型的数据分门别类地拆分出来，
整理清楚 —— 这种工作甚至有个专门的名称与之关联：数据清洗。
'''

def stats_text_en(text):
    '''
    输入参数text为一串英文字符
    统计英文字符串中各个单词出现的频次，按频次从高到低进行排序
    返回值sorted_list为最终排序的结果
    '''
    # 去掉所有的标点符号
    symbols = '.,-!*'
    for symbol in symbols:
        text = text.replace(symbol, ' ')

    # 按空格分隔字符串，转换成列表
    list1 = text.split()

    # 从列表中统计每个单词的个数，并写入字典
    dict1 = {}
    while len(list1) > 0:
        if list1[0] in dict1.keys():
            dict1[list1[0]] += 1
        else:
            dict1[list1[0]] = 1
        del list1[0]

    # 将字典按单词的个数排序，并保存到一个列表中
    sorted_list = sorted(dict1.items(), key=lambda x:x[1], reverse=True)
    return sorted_list

print(stats_text_en.__doc__)

def stats_text_cn(text):
    '''
    输入参数text为一串中文字符
    统计英文字符串中各个单词出现的频次，按频次从高到低进行排序
    返回值sorted_list为最终排序的结果
    '''
    # 去掉所有的标点符号，包括空格和换行
    symbols = '。，！：？—\n '
    for symbol in symbols:
        text = text.replace(symbol, '')

    # 按单个字符来分隔字符串，转换成列表
    list1 = []
    for s in text:
        list1.append(s)

    # 从列表中统计每个单词的个数，并写入字典
    dict1 = {}
    while len(list1) > 0:
        if list1[0] in dict1.keys():
            dict1[list1[0]] += 1
        else:
            dict1[list1[0]] = 1
        del list1[0]

    # 将字典按单词的个数排序，并保存到一个列表中
    sorted_list = sorted(dict1.items(), key=lambda x:x[1], reverse=True)
    return sorted_list
print(stats_text_cn.__doc__)

def main():
    print('英文字符频次统计：')
    print(stats_text_en(text1))
    print('中文字符频次统计：')
    print(stats_text_cn(text2))

if __name__ == '__main__':
    main()