
def stats_text_en(text):
    elements = text.split()         #用空白字符分隔chenglist
    words = []                      #定义新变量，储存处理过的单词
    symbols = ',.*_!「」。，'         #要剔除的非单词符号
    for element in elements:        #遍历要剔除的符号
        for symbol in symbols:      #逐个替换字符
            element = element.replace(symbol,'')
        if element<='\u4e00' or element>='\u9fa5':  #剔除中文字符
            words.append(element)   #element长度不为零算作正常单词
    counter = {}                    #dict变量，用于存放出现的次数
    word_set = set(words)           #去掉重复单词
    for word in word_set:           #统计出现次数
        counter[word] = words.count(word)
    return sorted(counter.items(),key=lambda x: x[1],reverse=True) #按照出现次数倒序排列
# print('统计参数中每个中文单词出现的次数 ==>\n', stats_text_en(text))



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
# print('统计参数中每个英文单词出现的次数 ==>\n', stats_text_cn(text))

def stats_text(text):
  return stats_text_en(text) + stats_text_cn(text)   #合并中英文统计结果
# print('统计参数中每个单词出现的次数 ==>\n', stats_text(text))
