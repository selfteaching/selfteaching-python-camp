# 自定义函数，该函数用于统计参数text中每个英文单词出现的次数，最后返回一个按词频降序排列的数组
def stats_text_en(text):   
    text1 = text.split()   # 先将字符串根据 空白字符 分割成 list, 要调用 str 类型
    text2 = []             # 定义一个新的 list 型变量，存储处理过的单词          
    symbols = ",.-!*"      # 先针对样本文本挑选出需要剔除的非单词符号

    for En in text1:       # 在列表text1中遍历一遍要剔除的符号
        for symbol in symbols:  # 如果包含symbols中需要剔除的字符，用replace语句替换掉
            En = En.replace(symbol, '')  # 逐个替换字符号，用''是为了同时剔除符号所占的位置
        if len(En):        # 剔除了字符后如果单词En的长度不为0，那么就算正常单词，可以加入到新的列表中
            text2.append(En)
   
    # 先把text中的符号剔除掉
    text3 = " ".join(text2)
    text3 = text3.lower()
    text3 = text3.lower()   

    # 把所有的单词变成小写格式
    text3 = text3.split() 

    # 把text变成list格式
    d = {}   

    # 采用空字典形式保存结果
    for i in text3:    
        a = text3.count(i)
        d[i] = a    # 统计text2中i的频次a，并将结果导入字典
    d1 = sorted(d.items(), key = lambda item : item[1], reverse = True)
    # 将字典里的元素按照value的降序排列
    print(d1, '\n')
    return


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


stats_text_en(text)

def stats_text_cn(text):
    text1 = []   # 设置一个空列表用来存储中文字符
    for cn in text:     
        if '\u4e00' <= cn <= '\u9fff':    # 判断text中的每个字符是否属于中文字符，是的话就加入到列表text1中，中文标点符号都去掉
            text1.append(cn)

    d = {}    # 新建一个空字典保存统计结果
    for zh in text1:
        d[zh] = text1.count(zh)    # 将统计text1中的字频a导入到字典d中
    d1 = sorted(d.items(), key = lambda item : item[1], reverse = True) # 按字频降序排列
    print(d1)
    return

text = '''
提姆·彼得斯（Tim Peters）撰写的《 Python之禅》


美丽胜于丑陋。
显式胜于隐式。
简单胜于复杂。
复杂胜于复杂。
扁平比嵌套更好。
稀疏胜于密集。
可读性很重要。
特殊情况还不足以打破规则。
尽管实用性胜过纯度。
错误绝不能默默传递。
除非明确地保持沉默。
面对不解之谜，拒绝猜测的诱惑。
应该有一种-最好只有一种-显而易见的方法。
尽管除非您是荷兰人，否则一开始这种方式可能并不明显。
现在总比没有好。
尽管从来没有比现在“正确”好。
如果实现难以解释，那是个坏主意。
如果实现易于解释，则可能是个好主意。
命名空间是一个很棒的主意-让我们做更多这些吧！
'''
stats_text_cn(text)