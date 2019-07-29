
#将英文进行词频统计。
def stats_text_en(text):
    #去除字符串中的中文字符
    for chara in text:
        if '\u4e00' <= chara <= '\u9fa5':
            text = text.replace(chara,",")
    #清洗英文字符串中的特殊字符
    for chara in ",.!-*？，。：「」、”":
        text = text.replace(chara," ")
    #将字符串中的英文全部变成小写
    text = text.lower()
    list1 = text.split()
    counts = {}
    #统计每个单词出现的词频
    for word in list1:
        counts[word] = counts.get(word,0) + 1
    list2 = list(counts.items())
    #将单词词频进行降序排序
    list2.sort(key=lambda x:x[1], reverse=True)
    return print(list2)

#将中文进行词频统计。
def stats_text_cn(text):
    list1 = []
    counts = {}
    #选取字符串中的中文字符
    for chara in text:
        if '\u4e00' <= chara <= '\u9fa5':
            list1.append(chara)
    #统计字符串中的中文词频
    for i in list1:
        counts[i] = counts.get(i,0) + 1
    list2 = list(counts.items())
    #将统计后的中文词频按降序排序
    list2.sort(key=lambda x: x[1], reverse=True)
    return print(list2)

#分别调用stats_text_en()函数和stats_text_cn()函数。
def stats_text(text):
    stats_text_en(text)
    stats_text_cn(text)

#清洗英文字符串中的特殊字符,使其仅对单个英文单词进行排序。
def data_cleaning_en(data_sample_str):
    for chara in ",.!-*":
        data_sample_str = data_sample_str.replace(chara," ")
    return data_sample_str

#将清洗后的英文字符串进行词频统计。
def stats_text_en(text):
    list1 = text.split()
    counts = {}
    for word in list1:
        counts[word] = counts.get(word,0) + 1
    list2 = list(counts.items())
    list2.sort(key=lambda x:x[1], reverse=True)
    print(list2)

#清洗中文字符串中的特殊字符，使其仅对单个中文单词进行排序。
def data_cleaning_cn(data_sample_str):
    for chara in ["，","。","？","！"," ","\n"]:
        data_sample_str = data_sample_str.replace(chara,"")
    return data_sample_str

#将清洗后的中文字符串进行词频统计。
def stats_text_cn(text):
    counts = {}
    for i in text:
        counts[i] = counts.get(i,0) + 1
    list2 = list(counts.items())
    list2.sort(key=lambda x: x[1], reverse=True)
    print(list2)

#主函数调用上述所有函数。
def main():
    text_en = """
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
    """
    text_cn='''
    蜀道难
    噫吁嚱，危乎高哉！
    蜀道之难，难于上青天！
    蚕丛及鱼凫，开国何茫然！
    尔来四万八千岁，不与秦塞通人烟。
    西当太白有鸟道，可以横绝峨眉巅。
    地崩山摧壮士死，然后天梯石栈相钩连。
    上有六龙回日之高标，下有冲波逆折之回川。
    黄鹤之飞尚不得过，猿猱欲度愁攀援。
    青泥何盘盘，百步九折萦岩峦。
    扪参历井仰胁息，以手抚膺坐长叹。
    问君西游何时还？畏途巉岩不可攀。
    但见悲鸟号古木，雄飞雌从绕林间。
    又闻子规啼夜月，愁空山。
    蜀道之难，难于上青天，使人听此凋朱颜。
    连峰去天不盈尺，枯松倒挂倚绝壁。
    飞湍瀑流争喧豗，砯崖转石万壑雷。
    其险也如此，嗟尔远道之人胡为乎来哉！
    剑阁峥嵘而崔嵬，一夫当关，万夫莫开。
    所守或匪亲，化为狼与豺。
    朝避猛虎，夕避长蛇；磨牙吮血，杀人如麻。
    锦城虽云乐，不如早还家。
    蜀道之难，难于上青天，侧身西望长咨嗟！
    '''
    string1 = data_cleaning_en(text_en)
    stats_text_en(string1)
    string2 = data_cleaning_cn(text_cn)
    stats_text_cn(string2)

main()

