# 1. 定义一个 stats_text_en 函数，统计输入给函数一个字符串中的所有的不同的英文单词的个数并按照从大到小排序

def stats_text_en (text_in):
    #提示输入一串字符串后，系统将统计其中英文单词个数并按照出现的频度进行排序，假设输入字符串除了字母外仅包括如
    # ．，：；！？-*'—'‘’\“\”()[ ]<>{}《》.\¨\"‖／＆～§→|,.-! 等常用非字母

    print('请输入一串字符串，除了字母外，仅包括,.*-!非字母字符串：==>')
    text = text_in
    print('您所输入的字字符串为==>', text)
    #1. 使用字典 dict 类型 统计字符串样本 text 中各个英文单词出现的次数
    #先将字符串根据 空白字符 分割成 list, 要调用 str 类型
    elements = text.split()
    
    #定义一个新的 list 类型变量，存储处理过的单词
    words = []
 
    for element in elements:
        #定义一下新的 字符串 类型变量，存储每个处理过的英文单词
        word = ""
        #遍历一遍 element 字符串，保留所有字母
        for uchar in element:
            if (uchar >= u'\u0041' and uchar <= u'\u005a') or (uchar >= u'\u0061' and uchar <= u'\u007a'):
                word = word + uchar
        #剔除了字符后如果 element 的长度不为 0，则算作正常单词
        if len(word):
          words.append(word)

    print('正常的英文单词 ==>', words)

    # 初始化一个 dict字典 类型的变量，用来存放单词出现的次数
    counter = {}

    # set 集合 类型 可以去掉 列表里的重复元素，可以在 for ... in 里减少循环次数

    word_set = set(words)

    for word in word_set:
        counter[word] = words.count(word)

    print('英文单词出现的次数 ==>', counter)

    #2. 按照出现次数从大到小输出所有的单词及出现次数

    #内置函数 sorted 的参数 key 表示按元素的那一项的值进行排序
    # dict 类型 counter 的 items 方法会返回一个 包含 相应 项 （key, value）的 元组 列表
    print('从大到小输出所有的单词及出现的次数==>', sorted(counter.items(), key=lambda x: x[1], reverse=True))
    return counter

# 1. 定义一个 stats_text_cn 函数，统计输入给函数一个字符串中的所有的不同的中文汉字的个数
# 并按照出现的频度从大到小排序

def stats_text_cn (textIn):
    #提示输入一串字符串后，系统将统计其中包括中文汉字个数并按照出现的频度进行排序

    print('请输入一串包含中文的字符串==>')
    text = textIn
    print('您所输入的包含中文的字符串为==>', text)
    #1. 使用字典 dict 类型 统计字符串样本 text 中各个英文单词出现的次数
    #先将字符串根据 采用强制 list 类型转换成单个字符, 要调用 str 类型
    elements = list(text)
    
    #定义一个新的 list 类型变量，存储处理过的单词
    words_cn = []
 
    #遍历选择出字符串中所有的中文汉字
    
    for element in elements:
        #判断如果是汉字，测将此汉字添加到 words_cn中
        if  '\u4e00' <= element <= '\u9fff':
            words_cn.append(element)

    print('正常的所有其中的汉字 ==>', words_cn)

    # 初始化一个 dict字典 类型的变量，用来存放单词出现的次数
    counter = {}

    # set 集合 类型 可以去掉 列表里的重复元素，可以在 for ... in 里减少循环次数

    word_set = set(words_cn)

    for word in word_set:
        counter[word] = words_cn.count(word)

    print('中文汉字出现的次数 ==>', counter)

    #2. 按照出现次数从大到小输出所有的汉字及出现次数

    #内置函数 sorted 的参数 key 表示按元素的那一项的值进行排序
    # dict 类型 counter 的 items 方法会返回一个 包含 相应 项 （key, value）的 元组 列表
    print('从大到小输出所有的单词及出现的次数==>', sorted(counter.items(), key=lambda x: x[1], reverse=True))
    return counter

def stats_text(text_en_cn):
    # 通过调用分别汉字和英文统计词频的两个函数并返回最终的统计结果，并进行合并并重新进行汉字英文词频混合排序


    # 调用英文词频统计 函数 stats_text_en 将结果存入 临时字典 dictTmpEn
    dictTmpEn = stats_text_en(text_en_cn)

    # 调用汉字词频统计 函数 stats_text_cn 将结果存入 临时字典 dictTmpCn
    dictTmpCn = stats_text_cn(text_en_cn)

    # 合并 汉字、英文丙个 dict 类型 数据 为一个字典 dictEnCn
    dictEnCn = dict(dictTmpEn, **dictTmpCn)
    
    #按照出现次数从大到小输出所有的汉字及出现次数

    #内置函数 sorted 的参数 key 表示按元素的那一项的值进行排序
    # dict 类型 counter 的 items 方法会返回一个 包含 相应 项 （key, value）的 元组 列表
    print('从大到小输出所有的单词及出现的次数==>', sorted(dictEnCn.items(), key=lambda x: x[1], reverse=True))
    return dictEnCn
    