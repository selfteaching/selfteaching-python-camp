text_en = '''
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
def stats_text_en(str): #定义该函数为用于统计上面text中各个英文单字出现的次数，并按词频降序排列
    a = str.lower() #将所有单词的字母转换成小写
    b = a.split() #将字符串转换为单词列表
    word = {} #第28行-第35行为统计各单词出现的次数
    for word1 in b:
        if word1 in word:
            count = word[word1]
        else:
            count = 0
        count = count + 1
        word[word1] = count
    print(sorted(word.items(), key = lambda e:e[1], reverse = True)) #将统计结果按次数的大小将序排列并输出结果
stats_text_en(text_en) #按上述定义函数统计text各英文单词出现的次数并输出

text_cn = '''
明月几时有，把酒问青天。
不知天上宫阙，今夕是何年。
我欲乘风归去，又恐琼楼玉宇，高处不胜寒。
起舞弄清影，何似在人间。
转朱阁，低绮户，照无眠。
不应又恨，何事长向别时圆。
人有悲欢离合，月有阴晴圆缺，此事古难全。
但愿人长久，千里共婵娟。

大江东去，浪淘尽，千古风流人物。
故垒西边，人道是、三国周郎赤壁。
乱石穿空，惊涛拍岸，卷起千堆雪。
江山如画，一时多少豪杰。
遥想公瑾当年，小乔初嫁了，雄姿英发。
羽扇纶巾，谈笑间、樯橹灰飞烟灭。
故国神游，多情应笑我，早生华发。
人生如梦，一尊还酹江月。
'''
def stats_text_cn(str): #定义该函数为用于统计上面text中各个汉字出现的次数，并按词频降序排列
    str = str.strip() #去除首尾空格
    str = str.replace('\n', '') #去除换行符
    punc = '。，、' #第61行-第64行为去掉文中的标点符号
    for i in punc:
        if i in str:
            str = str.replace(i, '')
    pas = {} #第65行-第72行为统计各汉字出现的次数
    for char1 in str:
        if char1 in pas:
            count = pas[char1]
        else:
            count = 0
        count = count + 1
        pas[char1] = count
    print(sorted(pas.items(), key = lambda e:e[1], reverse = True)) #将统计的汉字的数量按降序排列并输出
stats_text_cn(text_cn) #调用函数命令统计上面两首诗的每个汉字出现的次数并降序排列