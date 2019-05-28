# today's tasks used the same one parameter "text"
# (a variable should be assigned with strings including both en and cn)
import jieba
import re
import collections
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

真, 有改天换地的伟力. by 核聚 @ wechat id: hejupai
...循序渐进虽然难受, 但它能够有效避免思维混乱, 也因此, 循序渐进就是学习的捷径...
...最后, 最重要的是, 你是真的在学习.
真, 太难了.
只一日之间, 你已经联想到'衣带渐宽终不悔,为伊消得人憔悴'.
那么, 两日三日, 乃至日以继夜数十年, 那会有多少难?
真, 太难.
但, 真, 有改天换地的伟力.
在人的精神世界里, 真, 能改变一切, 造就一切.
祝, 开心.
祝, 勇猛精进.
'''
# because its called out errors about I redefined this function... I moved this part into a comment for later review.

# stats_text 函数，实现调用stats_text_en , stats_text_cn ，输出合并词频统计结果


def stats_text_en(en, count):
    ''' 英文词频统计'''

    if type(en) == str:
        text_en = re.sub("[^A-Za-z]", " ", en.strip())
        enList = text_en.split()
        isinstance(count, int)
        int(count) <= len(enList)  # day 10 try to debug
        # day9 using 1 counter objects supported method -most_common([n])
        return collections.Counter(enList).most_common(count)
    else:
        print("Inappropriate argument value (of correct type)")


def stats_text_cn(cn, count):
    ''' 汉字字频统计 使用标准库collections.Counter()统计词频并限制统计数量。
        1. 使用jieba第三方库精确模式进行分词。
        2. 使用正则表达式过滤汉字字符。
        3. 使用for循环判断分词后词频列表元素长度大于等于2的生成新列表。
        4. 使用标准库collections.Counter()统计词频并限制统计数量。 
        5. 参数类型检查，不为字符串抛出异常。'''
    if type(cn) == str:
        cnList = re.findall(u'[\u4e00-\u9fff]+', cn.strip())
        cnString = ''.join(cnList)
        segList = jieba.cut(cnString, cut_all=False)
        cnnewList = []
        for i in segList:
            if len(i) >= 2:
                cnnewList.append(i)
        countList = collections.Counter(cnnewList).most_common(count)
        return countList
    else:
        raise ValueError('Inappropriate argument value (of correct type)')


def stats_text(text, count=20):
    ''' 合并英汉词频统计 '''  # whole text words frequence stats (en + cn) """?inside qualified comments?"""
    if type(text) == str and isinstance(count, int):
        return (stats_text_en(text, count)+stats_text_cn(text, count))
    else:
        print("Inappropriate argument value (of correct type)")


# day7code:
#y = stats_text(text)
# if stats_text == "_main_" : # using this to solve my problem when imported in main?
#    print(y)  #without if statement above this .py file will print my function "stats_text" in d6's works


# day10 finally I got what I did --bug here collections.Counter(cnString).most_common([count])-list vs int~!!!
