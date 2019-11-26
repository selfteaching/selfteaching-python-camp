
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
There should be one-- and preferably only one --obvious way to do
it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
#  1.定义⼀个名为 stats_text_en 的函数，函数接受⼀个字符串 text 作为参数
# 2. 实现该函数的功能（同 day5 任务 2）：统计参数中每个英⽂单词出现的次数，最后返回⼀个按词频降序排列的数组
# 3. 为 stats_text_en 添加注释说明
#定义一个接受字符串的函数，1.统计样本text中英文单词出现的次数
                        #2.按照出现次数从大到小只输出所有单词及出现的次数，不要非英文字符和其他符号
# 定义一个接受字符串的函数
def stats_text_en(str):
#1.将英文单词全部转换为小写
    text_lower = str.lower()
#2.分割text文本，并转换为list
    text_split = text_lower.split()
#3.为了只统计英文单词
    symbols = ',*-.!'
#4.构建空列表，用来存储处理过的单词。[]→代表list列表数据类型，
    words = []

    for word in text_split:
        for symbol in symbols:#symbol→符号的意思
            word = word.replace(symbol, '')#  .replace(old, new) →是吧所有的符号全部转换成''，也就是去掉所有符号
        if len(word): #如果单词的长度不为0，则把单词加入list
            words.append(word) 
#print('正常的英文单词 ==>',words) #打印更改过后的字符串文本text
#5.定义一个字典
    text_count = {}
#6.利用set去掉list里重复的单词，减少遍历的次数，也去除了重复计算
    text_set = set(words)
#7.count()方法来统计word字符列表里单词出现的次数，每循环一次，就给字典里加入一个元素
    for word in text_set:
        text_count[word] = words.count(word)
    #print('英文单词出现的次数 ==>',text_count)
    print('从大到小输出所有单词及出现的次数 ==>\n', sorted(text_count.items(), key = lambda x: x[1], reverse = True)) 
    """
    用sorted()函数对所有可迭代的对象进行排序操作，以下格式是固定写法
    key=lambda x : x[1] 中的x可以是任何字母，[]中的数字是，相对元素第几个字段排序时，就写几
    比如第一位 →[0]，第二位[1]...     reverse = True 降序 ， reverse = False 升序（默认）
    """
stats_text_en(text)
# 函数的参数为text

text_cn = """
木兰诗 / 木兰辞

南北朝：佚名

唧唧复唧唧，木兰当户织。不闻机杼声，惟闻女叹息。(惟闻 通：唯)问女何所思，问女何所忆。女亦无所思，女亦无所忆。昨夜见军帖，可汗大点兵，军书十二卷，卷卷有爷名。

阿爷无大儿，木兰无长兄，愿为市鞍马，从此替爷征。东市买骏马，西市买鞍鞯，南市买辔头，北市买长鞭。旦辞爷娘去，暮宿黄河边，不闻爷娘唤女声，但闻黄河流水鸣溅溅。

旦辞黄河去，暮至黑山头，不闻爷娘唤女声，但闻燕山胡骑鸣啾啾。万里赴戎机，关山度若飞。朔气传金柝，寒光照铁衣。将军百战死，壮士十年归。

归来见天子，天子坐明堂。策勋十二转，赏赐百千强。可汗问所欲，木兰不用尚书郎，愿驰千里足，送儿还故乡。

爷娘闻女来，出郭相扶将；阿姊闻妹来，当户理红妆；小弟闻姊来，磨刀霍霍向猪羊。开我东阁门，坐我西阁床，脱我战时袍，著我旧时裳。当窗理云鬓，对镜帖花黄。

出门看火伴，火伴皆惊忙：同行十二年，不知木兰是女郎。雄兔脚扑朔，雌兔眼迷离；双兔傍地走，安能辨我是雄雌？

"""
#定义一个接受字符串的函数，1.统计样本text_cn中中文单词出现的次数
                        #2.按照出现次数从大到小只输出所有中文字及出现的次数，不要其他符号

def stats_text_cn(str):
     # 定义一个list来存放处理过的汉字，[]→代表list列表数据类型，
    cn = []
    # 把汉字拆分
    for i in str:#在中文中一个字符串本质上来讲就是一个列表，所以不用转换
        cn.append(i)#将拆分完的汉字重新组合起来
#<<<<<<< master
    #print(cn)
#=======
#>>>>>>> master
    # 定义标点符号合集，把\n放在和标点符号一起去除
    symbols = '，。()：；/\n？'
    #定义一个list来存放处理过标点符号的汉字
    z = []
    # 替换掉标点符号
    for zi in str:#在中文中一个字符串本质上来讲就是一个列表，所以不用转换
        for s in symbols:
           zi = zi.replace(s, '') #  .replace(old, new) →是吧所有的符号全部转换成''，也就是去掉所有符号
    # 只存储长度不为零的字符
        if len(zi):
            z.append(zi)
    # 定义一个字典
    text_ccc= {}
    # 用内置的set去除重复字（元素），这样做结果中相同的字就只会统计一次
    text_cnset = set(z)
    # 每循环一次，统计一个汉字的次数，加入一个元素
    for zi in text_cnset:
        text_ccc[zi] = z.count(zi)
    # 把字典里的每个元素都转换为一个元组，按元组中索引为1的item进行排序。
    """
    用sorted()函数对所有可迭代的对象进行排序操作，以下格式是固定写法
    key=lambda x : x[1] 中的x可以是任何字母，[]中的数字是，相对元素第几个字段排序时，就写几
    比如第一位 →[0]，第二位[1]...     reverse = True 降序 ， reverse = False 升序（默认）
    """
    print('从大到小输出所有汉字及出现的次数:\n', sorted(text_ccc.items(), key = lambda x: x[1], reverse = True))
stats_text_cn(text_cn)#执行定义的方法