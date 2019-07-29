import re

def stats_text_en(text):
    '''
    输入参数text为一串英文字符
    统计英文字符串中各个单词出现的频次，按频次从高到低进行排序
    返回值sorted_list为最终排序的结果
    '''
    # 将非字母和’号, 全部替换成空格
    pttn = r'[^a-zA-Z\']'
    text = re.sub(pttn, ' ', text)

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

def stats_text_cn(text):
    '''
    输入参数text为一串中文字符
    统计英文字符串中各个单词出现的频次，按频次从高到低进行排序
    返回值sorted_list为最终排序的结果
    '''
    # 将字符串转成列表
    list1 = list(text)
 
    # 从列表中统计每个单词的个数，并写入字典
    dict1 = {}
    while len(list1) > 0:
        if '\u4e00' <= list1[0] <= '\u9fff':
            if list1[0] in dict1.keys():
                dict1[list1[0]] += 1
            else:
                dict1[list1[0]] = 1
        del list1[0]

    # 将字典按单词的个数排序，并保存到一个列表中
    sorted_list = sorted(dict1.items(), key=lambda x:x[1], reverse=True)
    return sorted_list

def stats_text(text):
    '''
    输入参数text为一串字符，可包括中英文及其它符号
    统计字符串中各个单词出现的频次，按频次从高到低进行排序
    返回值sorted_list为最终排序的结果
    '''
    list_en = stats_text_en(text)
    list_cn = stats_text_cn(text)

    return list_cn + list_en

print(stats_text.__doc__)

text = '''
1234.，；‘【】；here’。l。，；-&~！@#￥%返+返,回值 你sorted和list他 为
最终。排序的结果.hello world你好is't我是谁
'''
if __name__ == '__main__':
    print('合并统计中英文频次')
    print(stats_text(text))