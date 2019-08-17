# 定义函数，统计参数中每个英⽂单词出现的次数，最后返回⼀个按词频降序排列的数组
def stats_text_en(text):
    # 先将字符串根据空白字符分割成list，要调用str类型
    elements = text.split()
    #定义一个新的list型变量，存储处理过的单词
    words = []
    #先针对样本文本挑选出需要剔除的非单词符号
    symbols = ',.*-!'
    for element in elements:
        #遍历一遍要剔除的符号
        for symbol in symbols:
            #逐个替换字符号，用''是为了同时剔除符号所占的位置
            element = element.replace(symbol,'')
        #剔除了字符后如果element的长度不为0，则算作正常单词
        if len(element):
            #过滤出英文单词，剔除非英文单词
            if ('\u0041' <= element <= '\u005a') or ('\u0061' <= element <= '\u007a'):
                words.append(element)
    
    #初始化一个dict类型的变量，用来存放单词出现的次数
    counter = {}
    #set(集合)类型可以去掉列表里的重复元素，可以在 for...in里减少循环次数
    word_set = set(words)

    for word in word_set:
        counter[word] = words.count(word)
    
    #按照出现次数降序排列
    print(sorted(counter.items(), key=lambda x: x[1], reverse=True))

stats_text_en('你好 你好 不好 呵呵 aa bb')

# 定义函数，统计参数中每个中文汉字出现的次数，最后返回⼀个按词频降序排列的数组
def stats_text_cn(text):
    # 先将字符串根据空白字符分割成list，要调用str类型
    elements = text.split()
    #定义一个新的list型变量，存储处理过的单词
    words = []
    #先针对样本文本挑选出需要剔除的非单词符号
    symbols = ',.*-!'
    for element in elements:
        #遍历一遍要剔除的符号
        for symbol in symbols:
            #逐个替换字符号，用''是为了同时剔除符号所占的位置
            element = element.replace(symbol,'')
        #剔除了字符后如果element的长度不为0，则算作正常单词
        if len(element):
            #过滤出英文单词，剔除非中文汉字
            if ('\u4e00' <= element <= '\u9fff'):
                words.append(element)
    
    #初始化一个dict类型的变量，用来存放单词出现的次数
    counter = {}
    #set(集合)类型可以去掉列表里的重复元素，可以在 for...in里减少循环次数
    word_set = set(words)

    for word in word_set:
        counter[word] = words.count(word)
    
    #按照出现次数降序排列
    print(sorted(counter.items(), key=lambda x: x[1], reverse=True))

stats_text_cn('你好 你好 不好 呵呵 aa bb')