def stats_text_en(text):
    """
    函数 stats_text_en(text) 的功能: 统计字符串 text 里的各个英文单词出现的次数, 按降序排列

    函数的返回结果 en_counter_sort 是 list 类型, 它的元素是 tuple 类型, 
    这里的 tuple 的元素包含一个字符串（单词）和一个数字（出现的次数）, 例如('good', 10)
    """
    
    # 英文单词是一串字母, 单词间由空格或标点符号分隔, 先将标点符号替换成空格, 
    # 然后利用 str.split() 根据空白将 text 拆分成单个的单词
    # 剔除 text 里的标点符号, 替换成“空格”, 如果替换成“空”就相当于删除
    symbols = ',./<>?:;"[]\\{}|~`!@#$%^&*()_-+=\
        ，。、《》？：；‘’“”【】{}|~·！@#￥%……&*（）——-+=\
        ，。、《》？：；‘’“”【】＼｛｝｜～·！＠＃￥％……＆×（）——－＋＝\
        \t\n\r\xa0\u3000'
    for symbol in symbols:
        text = text.replace( symbol, ' ' )
    
    # 根据空白，将字符串 text 拆分成单个的单词, 存放在列表 text_list 里
    # 得到了“单词”, 才能统计“单词”出现的次数
    # 所有的单词都在列表 text_list 里, 所以就在列表 text_list 里统计各单词出现的次数
    text_list = text.split()
    
    # 将 list 类型转换成 set 类型, 这样就去掉了 list 里重复的“单词”, 可以减少统计时的迭代次数
    text_set = set( text_list )

    # 初始化一个 dict 类型的变量, 用于存放单词和出现的次数
    en_counter = {}
    
    # 从集合 text_set 取单词, 在列表 text_list 里统计出现的次数, 
    # 然后存入字典 en_counter 里
    for en in text_set:
        en_counter[ en ] = text_list.count( en )   # 向字典赋值
    
    # 按照单词出现的次数, 降序排列
    # 函数的返回结果 en_counter_sort 是 list 类型, 它的元素是 tuple 类型, 
    # 这里的 tuple 的元素包含一个字符串（单词）和一个数字（出现的次数）, 例如('good', 10)
    en_counter_sort = sorted( en_counter.items(), key=lambda value:value[1], reverse=True )

    return en_counter_sort


def stats_text_cn(text):
    """
    函数 stats_text_cn 的功能: 统计字符串 text 里的每个汉字出现的次数, 按降序排列

    函数的返回结果 cn_counter_sort 是 list 类型, 它的元素是 tuple 类型, 
    这里的 tuple 的元素包含一个字符串（汉字）和一个数字（出现的次数）, 例如('好', 10)
    """
    # 不像英文单词是一串字母, 汉字本身就单个的
    # 根据 unicode 里中文字符的范围, 将 text 里的所有汉字挑出来, 
    # 存放在 list 类型变量 cn_characters_list 里
    cn_characters_list = [] 
    for character in text:
        if '\u4e00' <= character <= '\u9fef' :
            cn_characters_list.append( character )
    
    # 将 list 类型转换成 set 类型, 去掉 cn_characters_list 里重复的汉字
    cn_characters_set = set( cn_characters_list )

    # 初始化一个 dict 类型的变量，用于存放单词和出现的次数
    cn_counter = {}

    # 从集合 cn_characters_set 取汉字，在列表 cn_characters_list 里统计该汉字出现的次数，
    # 然后存入字典 cn_counter 里
    for cn_character in cn_characters_set :
        cn_counter[ cn_character ] = cn_characters_list.count( cn_character )
    
    # 根据汉字在 text 里出现的次数, 按降序排列
    # 函数的返回结果 cn_counter_sort 是 list 类型, 它的元素是 tuple 类型, 
    # 这里的 tuple 的元素包含一个字符串（汉字）和一个数字（出现的次数）, 例如('好', 10)
    cn_counter_sort = sorted( cn_counter.items(), key=lambda elem:elem[1], reverse=True )
    
    return cn_counter_sort


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

text_cn = '''
　学 而 第 一

子曰：“学而时习之，不亦说乎？有朋自远方来，不亦乐乎？人不知，而不愠，不亦君子乎？”

有子曰：“其为人也孝弟，而好犯上者，鲜矣；不好犯上，而好作乱者，未之有也。君子务本，本立而道生。孝弟也者，其为仁之本与！”

子曰：“巧言令色，鲜矣仁！”

曾子曰：“吾日三省吾身：为人谋而不忠乎？与朋友交而不信乎？传不习乎？”

子曰：“道千乘之国，敬事而信，节用而爱人，使民以时。”

子曰：“弟子入则孝，出则悌，谨而信，泛爱众，而亲仁。行有馀力，则以学文。”

子夏曰：“贤贤易色；事父母，能竭其力，事君，能致其身；与朋友交，言而有信。虽曰未学，吾必谓之学矣。”

子曰：“君子不重，则不威。学则不固。主忠信。无友不如己者。过则勿惮改。”
曾子曰：“慎终追远，民德归厚矣。”

子禽问于子贡曰：“夫子至于是邦也，必闻其政。求之与？抑与之与？”
子贡曰：“夫子温、良、恭、俭、让以得之。夫子之求之也，其诸异乎人之求之与！”

子曰：“父在，观其志；父没，观其行；三年无改于父之道，可谓孝矣。”

有子曰：“礼之用，和为贵。先王之道斯为美，小大由之。有所不行，知和而和，不以礼节之，亦不可行也。”

有子曰：“信近于义，言可复也。恭近于礼，远耻辱也。因不失其亲，亦可宗也。”

子曰：“君子食无求饱，居无求安，敏于事而慎于言，就有道而正焉，可谓好学也已。”

子贡曰：“贫而无谄，富而无骄，何如？”子曰：“可也。未若贫而乐，富而好礼者也。”

子贡曰：“《诗》云‘如切如磋，如琢如磨’，其斯之谓与？”
子曰：“赐也，始可与言《诗》已矣。告诸往而知来者。”

子曰：“不患人之不己知，患不知人也。”
'''

# print( f'text_en中各个单词出现的次数，降序排列：', stats_text_en(text_en), sep='\n' )
print( f'text_en中的英文单词总数：', len( stats_text_en(text_en) ) )
print( f'text_en中各个英文单词出现的次数，降序排列：' )
for word,freq in stats_text_en(text_en):
    print( word, freq )

print( f'text_cn中各个汉字出现的次数，降序排列：', stats_text_cn(text_cn), sep='\n' )
print( f'text_cn中的汉字总数：', len( stats_text_cn(text_cn) ) )
print( f'text_cn中各个汉字出现的次数，降序排列：' )
for word,freq in stats_text_cn(text_cn):
    print( word, freq )