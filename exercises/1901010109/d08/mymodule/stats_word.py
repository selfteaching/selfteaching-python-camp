def stats_text_en(text):
    """
    函数 stats_text_en(text) 的功能: 统计字符串 text 里的各个英文单词出现的次数, 按降序排列

    函数的返回结果 en_counter_sort 是 list 类型, 它的元素是 tuple 类型, 
    这里的 tuple 的元素包含一个字符串（单词）和一个数字（出现的次数）, 例如('good', 10)
    """

    # 参数类型检查, 如果输⼊参数不为字符串类型则抛出 ValueError 错误, 并包含完整的错误提示信息
    if type(text) != str:
        raise ValueError("您输入的是非字符串类型") 
    
    # if not isinstance(text, str): 
	#     raise ValueError("您输入的是非字符串类型" % type(text)) 

    # 统计 text 里某个单词出现的次数时不区分大小写, 将字符串 text 里的字母全部转化成小写
    text = text.lower()

    # 利用 str.split() 根据空白将 text 拆分成单个的“单词”, 返回结果是 list
    text_list = text.split()

    word_list = []

    # 英文单词是一串字母, 单词间由空格或标点符号分隔, 先将标点符号替换成空格, 
    # 剔除 text_list 里的各单词里的标点符号, 替换成“空格”, 如果替换成“空”就相当于删除
    symbols = ',./<>?:;"[]\\{}|~`!@#$%^&*()_-+=\
        ，。、《》？：；‘’“”【】{}|~·！@#￥%……&*（）——-+=\
        ，。、《》？：；‘’“”【】＼｛｝｜～·！＠＃￥％……＆×（）——－＋＝「」\
        \t\n\r\xa0\u3000'
    
    for element in text_list:
        for symbol in symbols:
            element = element.replace( symbol, '' )
        if len(element) and element.isascii():
            word_list.append(element)
    
    # 得到了“单词”, 才能统计“单词”出现的次数
    # 所有的单词都在列表 word_list 里, 所以就在列表 word_list 里统计各单词出现的次数

    # 将 list 类型转换成 set 类型, 这样就去掉了 list 里重复的“单词”, 可以减少统计时的迭代次数
    word_set = set( word_list )

    # 初始化一个 dict 类型的变量, 用于存放单词和出现的次数
    en_counter = {}
    
    # 从集合 word_set 取单词, 在列表 word_list 里统计出现的次数, 
    # 然后存入字典 en_counter 里
    for en in word_set:
        en_counter[ en ] = word_list.count( en )   # 向字典赋值
    
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

    # 参数类型检查, 如果输⼊参数不为字符串类型则抛出 ValueError 错误, 并包含完整的错误提示信息
    if type(text) != str:
        raise ValueError("您输入的是非字符串类型") 
    
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


def stats_text(text):
    """
    函数 stats_text(text) 的功能: 分别调⽤ stats_text_en, stats_text_cn, 输出合并词频统计结果
    """
    
    # 参数类型检查, 如果输⼊参数不为字符串类型则抛出 ValueError 错误, 并包含完整的错误提示信息
    if type(text) != str:
        raise ValueError("您输入的是非字符串类型") 
        
    # 首先对 text 进行中英文拆分, 得到一个只有中文的 cn_text, 一个只有英文 en_text
    # en_text = text
    # cn_text = text

    # 将字符串拆分为单个字符
    # text_list = list( text )
    # 分离出英文字符与中文字符
    # cn_text = ''.join( i for i in text_list if ord(i)>256 )
    # en_text = ''.join( i for i in text_list if ord(i)<257 )

    # # 根据 unicode 里中文字符的编码范围, 将 text 里的所有汉字替换成“空”, 相当于删除
    # # en_text 变成了只有英文的字符串
    # for character in text:
    #     if '\u4e00' <= character <= '\u9fa5' :
    #         en_text = en_text.replace( character, '' )    # 将 text 里的汉字替换成“空”

    # # 根据 unicode 里英文字符的编码范围, 将 text 里的所有英文字母替换成“空”, 相当于删除
    # # cn_text 变成了只有中文的字符串
    # for character in text:
    #     if ( '\u0041' <= character <= '\u005A' ) or ( '\u0061' <= character <= '\u007A') :
    #         cn_text = cn_text.replace( character, '')
    
    word_counter = stats_text_en(text) + stats_text_cn( text )

    return word_counter