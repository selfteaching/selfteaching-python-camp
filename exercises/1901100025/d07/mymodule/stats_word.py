text1 = '''
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
If the implementation is easy to explain, it's may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
def stats_text_en(t):
     # 定义一个接收字符串的函数，该函数统计参数中每个英⽂文单词出现的次数，最后返回⼀一个按词频降序排列列的数组
    text_lower = t.lower()
    # 先将英文单词全部转换为小写
    text_split = text_lower.split()
    # 将字符串按空格拆分，并转换为list
    symbols = ',*-.!'
    # 标点符号可以再全一点
    words = []
    # 定义一个list变量，用来存储处理过的单词
    for word in text_split:
        for symbol in symbols:
            word = word.replace(symbol, '')
    # 把每个单词中的标点符号都除去
        if len(word):
            words.append(word)
    # 如果单词的长度不为0，则把单词加入list
    text_count ={}
    # 定义一个字典
    text_set = set(words)
    # 利用set去掉list里重复的单词，减少遍历次数，也去除了重复计算
    for word in text_set:
        text_count[word] = words.count(word)
    # 每循环一次，就给字典里加入一个元素
    list_en = sorted(text_count.items(), key = lambda x: x[1], reverse = True)
# 把字典里的每个元素都转换为一个元组，按元组中索引为1的item进行排序。
    return list_en
# 函数的参数为text

text = '''
《逍遥游》
作者：庄周
  北冥有鱼，其名为鲲。鲲之大，不知其几千里也。化而为鸟，其名为鹏。鹏之背，不知其几千里也，怒而飞，其翼若垂天之云。是鸟也，海运则将徙于南冥。南冥者，天池也。《齐谐》者，志怪者也。《谐》之言曰：“鹏之徙于南冥也，水击三千里，抟扶摇而上者九万里，去以六月息者也。”野马也，尘埃也，生物之以息相吹也。天之苍苍，其正色邪？其远而无所至极邪？其视下也，亦若是则已矣。且夫水之积也不厚，则其负大舟也无力。覆杯水于坳堂之上，则芥为之舟；置杯焉则胶，水浅而舟大也。风之积也不厚，则其负大翼也无力。故九万里，则风斯在下矣，面后乃今培风；背负青天而莫之夭阏者，而后乃今将图南。

  蜩与学鸠笑之曰：“我决起而飞，抢榆枋而止，时则不至，而控于地而已矣，奚以之九万里而南为？”适莽苍者，三餐而反，腹犹果然；适百里者宿舂粮，适千里者，三月聚粮。之二虫又何知？

  小知不及大知，小年不及大年。奚以知其然也？朝菌不知晦朔，蟪蛄不知春秋，此小年也。楚之南有冥灵者，以五百岁为春，五百岁为秋。上占有大椿者，以八千岁为春，八千岁为秋。而彭祖乃今以久特闻，众人匹之。不亦悲平！
  汤之问棘也是已：“穷发之北有冥海者，天池也。有鱼焉，其广数千里，未有知其修者，其名为鲲。有鸟焉，其名为鹏。背若泰山，翼若垂天之云。抟扶摇羊角而上者九万里，绝云气，负青天，然后图南，且适南冥也。斥鹅笑之曰：‘彼且奚适也？我腾跃而上，不过数仞而下，翱翔蓬蒿之间，此亦飞之至也。面彼且奚适也？’”此小大之辩也。
  故夫知效一官，行比一乡，德合一君而征一国者，其自视也，亦若此矣。而宋荣子犹然笑之。且举世而誉之而不加劝，举世而非之而不加沮，定乎内外之分，辩乎荣辱之境，斯已矣。彼其于世，未数数然也。虽然，犹有未树也。夫列子御风而行，泠然善也。旬有五日而后反。彼于致福者，未数数然也。此虽免乎行，犹有所待者也。若夫乘天地之正，而御六气之辩，以游无穷者，彼且恶乎待哉？故曰：至人无己，神人无功，圣人无名。
'''
# 定义一个接收字符串的函数，该函数统计参数中每个中文汉字出现的次数，最后返回⼀一个按词频降序排列列的数组
def stats_text_cn(s):
     # 定义一个list来存放处理过的汉字
    cn = []
    # 把汉子拆分
    for i in s:
        cn.append(i)
    # 定义标点符号合集，因为不会单独去除'\n'，所以放在标点符号一起去除
    symb = '，。“”‘’《》\n！？:'
    z = []
    # 替换掉标点符号
    for zi in s:
        for si in symb:
           zi = zi.replace(si, '') 
    # 只存储长度不为零的字符
        if len(zi):
            z.append(zi)
    # 定义一个字典
    text_cndic = {}
    # 用set去除重复字，这样做结果中相同的字就只会统计一次
    text_cnset = set(z)
    # 每循环一次，统计一个汉子的次数，加入一个元素
    for zi in text_cnset:
        text_cndic[zi] = z.count(zi)
    # 把字典里的每个元素都转换为一个元组，按元组中索引为1的item进行排序。
    list_cn = sorted(text_cndic.items(), key = lambda x: x[1], reverse = True)
    return list_cn

# 定义一个函数用来统计中英文混合的词频
def stats_text(w):
# 将字符串拆分为单个字符
    w = list(w)
# 分离出英文字符与中文字符，等我搞懂了正则函数再把这块改改  
    cn = ''.join(i for i in w if ord(i)>256)
    en = ''.join(i for i in w if ord(i)<257)
# 调用之前的函数，分别统计中英文词频
    list_cn = stats_text_cn(cn)
    list_en = stats_text_en(en)
# 合并中英文词频list，并排序
    list_all = sorted((list_cn+list_en), key = lambda x:x[1], reverse = True)
    return list_all