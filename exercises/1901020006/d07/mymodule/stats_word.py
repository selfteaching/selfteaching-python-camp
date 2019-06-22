# 封装统计英文单词词频的函数
def stats_text_en(text):
    elements = text.split()
    words = []
    symbols = ',.*-!'
    for element in elements:
        for symbol in symbols:
            element = element.replace(symbol,'')
# master
        # 用 str 类型的 isascii 方法判断是否是英文单词
        if len(element) and element.isascii:
#=======
        if len(element):
# master
            words.append(element)
    counter = {}
    word_set = set(words)
    
    for word in word_set:
        counter[word] = words.count(word)
    return sorted(counter.items(),key=lambda x:x[1],reverse=True)        

# 统计参数中每个中文汉字出现的次数
def stats_text_cn(text):
    cn_characters = []
    for character in text:
        if'u4e00' <= character <= '\u9fff':
            cn_characters.append(character)
    counter = {}
    cn_character_set = set(cn_characters)
    for character in cn_character_set:
        counter[character] = character.count(character)
    return sorted(counter.items(),key=lambda x:x[1],reverse=True)

en_text = '''
The Zen of Python, by Tim Peters
'''

cn_text = '''

优美胜于丑陋
'''
    
    #搜索 __name__ ==__main__
    # 一般情况下在文件内 测试 代码的事后以下面的形式进行
if __name__ =='__main__':
    en_result = stats_text_en(en_text)
    cn_result = stats_text_cn(cn_text)
    print('统计参数中每个英文单词出现的次数 ==>\n', en_result)
    print('统计参数中每个英文单词出现的次数 ==>\n', cn_result)


# master
def stats_text(text):
    '''
    合并 英文词频 和 中文词频 的结果
    '''
    return stats_text_en(text) + stats_text_cn(text)
#
def stats_text_cn(text):    #定义函数，参数text可变
    setb=set(text)   #设定集合set，并把集合元素赋值给setb
    d = []   #设定列表
    for char in setb:        #char从集合setb中取值
	    if char >= u'\u4e00' and char <= u'\u9fa5':       #如果c是在u4e00 到u9fa5之间（汉字）
	        count=text.count(char)     #统计每个汉字的数量
	        n=(char,count)
	        d.append(n)         #将y加到x列表中
    x=sorted(d,key=lambda kv:kv[1],reverse=True)    #按重复次数，由大到小排列
    return x
    #print('\n按照出现次数降序输出所有汉字:\n')
    #print(x)
# master
