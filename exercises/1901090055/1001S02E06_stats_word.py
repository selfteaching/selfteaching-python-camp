text='''
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
There should be one-- and preferably only one --obvious way to do
it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

'''
def stats_text_en(text):
    elements = text.split()         #用空白字符分隔chenglist
    words = []                      #定义新变量，储存处理过的单词
    symbols = ',.*_!'               #要剔除的非单词符号
    for element in elements:        #遍历要剔除的符号
        for symbol in symbols:      #逐个替换字符
            element = element.replace(symbol,'')
        if len(element):
            words.append(element)   #element长度不为零算作正常单词
    counter = {}                    #dict变量，用于存放出现的次数
    word_set = set(words)           #去掉重复单词
    for word in word_set:           #统计出现次数
        counter[word] = words.count(word)
    return sorted(counter.items(),key=lambda x: x[1],reverse=True) #按照出现次数倒序排列
print('统计参数中每个英文单词出现的次数 ==>\n', stats_text_en(text))

cn_text='''
定投

投资，是我能找到的唯一一个普通人可以跨越阶层的通路。而定投则是唯一一种所有普通人都有机会做、并且都有能力做好的投资方式。

所谓的定投，就是针对某个投资标的在很长的时间内定期投资一定的金额。

例如，在未来的 5 到 10 年之中（很长的时间），每周（定期）投资 BOX 这个无管理费的区块链 ETF 产品（投资标的）150 美元或者 1000 元人民币（一定的金额）…… 当然，你可以把 BOX 替换为任何值得长期投资并持有的标的，比如苹果公司股票、贵州茅台股票，可口可乐股票，或者标准普尔指数基金。

在任何一个社会，在任何一个时代，绝大多数人都处于终生抱怨的状态。然而，在今天这个时代 —— 今天这个有着自由且成熟的证券交易市场存在的时代 —— 绝大多数终生抱怨的人其实并不知道他们每个人（对，就是每个人）都实际上因为无知错过了自己摆脱一切抱怨的机会。

可自由参与的证券交易市场，是当今现代世界里的奇迹 —— 正是因为它的存在，所有的普通人才有了至高无上的机会 —— 这一点书中会详细论述。
'''

def stats_text_cn(text):       
    characters = []                        #定义新变量，储存处理过的单词
    for character in text:
        if '\u4e00'<=character<='\u9fa5':  #筛选中文字符
            characters.append(character)   #存放到character dict里
    counter = {}                           #dict变量，用于存放出现的次数
    character_set = set(characters)        #去掉重复单词
    for word in character_set:             #统计出现次数
        counter[word] = characters.count(word)
    return sorted(counter.items(),key=lambda x: x[1],reverse=True)#按照出现次数倒序排列
print('统计参数中每个英文单词出现的次数 ==>\n', stats_text_cn(cn_text))

