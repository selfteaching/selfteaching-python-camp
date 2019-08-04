from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = 'all'

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

# 函数 stats_text_en 的功能：统计 text 里的每个单词出现的次数，按次数降序排列
def stats_text_en(text):
    
    # 剔除 text 里的标点符号，替换成“空”相当于删除
    symbols = ',.-:;!@#$%^&*()-+=<>?/\\`~|[]{}，。？、·~！@#￥%……&*（）——+-={}【】、|；：“”‘’'
    for symbol in symbols:
        text = text.replace( symbol, '' )

    # 将字符串 text 拆分成单个的单词，得到了“单词”，才能统计“单词”出现的次数
    # 拆分是必须的！在这个列表里，统计各单词出现的次数
    text_list = text.split()

    # 将 list 类型转换成 set 类型，这样就去掉了 list 里重复的“单词”，可以减少统计时的迭代次数
    text_set = set( text_list )

    # 初始化一个 dict 类型的变量，用于存放单词和出现的次数
    en_counter = {}

    # 从集合 text_set 取单词，在列表 text_list 里统计出现的次数，然后存入字典 en_counter 里
    for en in text_set:
        en_counter[ en ] = text_list.count( en )   # 向字典赋值

    # 按照单词出现的次数，降序排列
    # en_counter_sort 是一个 list, 它的元素是 tuple
    # 这里的 tuple 的元素包含一个字符串和一个数字，('str', 8)
    en_counter_sort = sorted( en_counter.items(), key=lambda value:value[1], reverse=True )

    return en_counter_sort

# 函数 stats_text_cn 的功能：统计 text 里的每个汉字出现的次数，按次数降序排列
def stats_text_cn(text):

    # 剔除 text 里的标点符号，替换成“空”相当于删除
    symbols = ',.-:;!@#$%^&*()-+=<>?/\\`~|[]{}\
    ，。？、·~！@#￥%……&*（）——+-={}【】、|；：“”‘’《》\
    \n\t\r\xa0\u3000'

    for symbol in symbols:
        text = text.replace( symbol, '' )
    
    # 去除字符串 text 里的空白
    # txt = text.strip()

    # 方法一：不区分重复的字，⽤字符串切⽚的⽅式依次取出单个的汉字，利用 dict 的自动去重功能
    cn_counter = {}
    for cn in text:
        cn_counter[ cn ] = text.count( cn )
    cn_counter_sort = sorted( cn_counter.items(), key=lambda value:value[1], reverse=True )
    return cn_counter_sort
    
    # # 方法二：与统计英文单词的方法类似，先获得单个的汉字，再利用 set 的去重功能
    # # 将字符串 text 里的汉字打散成单个的字，这样才能统计“汉字”出现的次数
    # text_list = []
    # for i in range( len(text) ):
    #     if len( text[i] ):
    #         text_list.append( text[ i ] )

    # # 将 list 类型转换成 set 类型，这样就去掉了 list 里重复的“汉字”
    # text_set = set( text_list )

    # # 初始化一个 dict 类型的变量，用于存放“汉字和出现的次数”
    # cn_counter = {}

    # # 从集合 text_set 取汉字，在字符串 text 里统计出现的次数，然后存入字典 cn_counter 里
    # for cn in text_set:
    #     cn_counter[ cn ] = text.count( cn )   # 向字典赋值

    # # 按照单词出现的次数，降序排列
    # # cn_counter_sort 是一个 list, 它的元素是 tuple
    # # 这里的 tuple 的元素包含一个字符串和一个数字，('str', 8)
    # cn_counter_sort = sorted( cn_counter.items(), key=lambda value:value[1], reverse=True )

    # return cn_counter_sort


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