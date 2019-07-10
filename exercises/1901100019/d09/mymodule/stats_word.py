import re
import collections

def stats_text_en(text, count):
    '''
    统计字符串中英文单词的词频。

    :param text:需要统计的字符串\t
    :type text: str字符串\t
    :param count:需要输出的字符的个数\t
    :type count: int整型\t
    :return: 统计结果\t
    :rtype: list列表\t
    '''
    if isinstance(text, str) != True:
        raise ValueError('输入参数非字符串！')

    # 将非字母和’号, 全部替换成空格
    pttn = r'[^a-zA-Z\']'
    text = re.sub(pttn, ' ', text)

    # 按空格分隔字符串，转换成列表
    list1 = text.split()

    obj_cnt = collections.Counter()
    for word in list1:
        obj_cnt[word] += 1

    return obj_cnt.most_common(count)

def stats_text_cn(text, count):
    '''
    统计字符串中中文的词频。

    :param text:需要统计的字符串\t
    :type text: str字符串\t
    :param count:需要输出的字符的个数\t
    :type count: int整型\t
    :return: 统计结果\t
    :rtype: list列表\t
    '''
    if isinstance(text, str) != True:
        raise ValueError('输入参数非字符串！')

    # 将字符串转成列表
    list1 = list(text)

    # 从列表中提取中文字符，并写入新的列表
    list2 = []
    while len(list1) > 0:
        if '\u4e00' <= list1[0] <= '\u9fff':
            list2.append(list1[0])
        del list1[0]

    obj_cnt = collections.Counter()
    for word in list2:
        obj_cnt[word] += 1

    return obj_cnt.most_common(count)

print(stats_text_en.__doc__)
print(stats_text_cn.__doc__)

text = '''
1234.，；‘【】；here’。l。，；-&~！@#￥%返+返,回值 你sorted和list他 为
最终。排list序的list结果.hello world你好is't我我我sorted我我我是谁
'''
if __name__ == '__main__':
    print('合并统计中英文频次')
    print(stats_text_en(text, 10))
    print(stats_text_cn(text, 10))