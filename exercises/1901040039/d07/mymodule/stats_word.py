#<<<<<<< master

# 此文件用函数封装统计词频及排序的操作

def stats_text_en(list_a,dic_a) :
    """通过dictionary统计list_a中每个英文单词出现的次
    数，并返回该结果"""

    # 通过dictionaries 进行统计中文词频
    for i in range(len(list_a)) :
        if list_a[i] in dic_a :
            dic_a[list_a[i]] += 1
    return dic_a




def stats_text_cn(list_a,dic_a) :
    """通过dictionary统计list_a中每个中文单词出现的次数
    ，并返回该结果"""

    # 通过dictionaries 进行统计英文词频
    for i in range(len(list_a)) :
        if list_a[i] in dic_a :
            dic_a[list_a[i]] += 1
    return dic_a


def stats_text(text) :
    """将text中的字符串放入list容器，分别调用
    stats_text_cn、stats_text_en函数输出词频统计结果"""
    list_a = []
    list_b = []
    dict_c = {}
    j = 0
# 将text文件转为list结构
    for i in range(len(text)) :
        if (text[i] >= '\u4e00') and (text[i] <= '\u9fa5') : #将中文单词放入list和dictionary
            list_a.append(text[i])
            j = i + 1
            if text[i] not in dict_c :
                dict_c[text[i]] = 0
        elif (ord(text[i]) not in range(65,91)) and (ord(text[i]) not in range(97,123)) and (text[i] != "\'") :#将英文单词放入list和dictionary
            if i == j :
                j += 1
            else :
                list_b.append(text[j:i])
                if text[j:i] not in dict_c :
                    dict_c[text[j:i]] = 0
                j = i + 1
        elif i == (len(text)-1) : #当末尾是字母或'时，增加最后一个英文单词
            list_b.append(text[j:i+1])
            if text[j:i+1] not in dict_c :
                    dict_c[text[j:i+1]] = 0
    if len(list_a) == 0  and len(list_b) == 0 :
        return
    print('列表：\n' 'list_a：', list_a,'\n\n' 'list_b：',list_b, end = '\n\n')

    #分别调用两个函数统计词频
    stats_text_cn(list_a,dict_c)
    stats_text_cn(list_b,dict_c)

    #排序输出
    return print('排序后：', sorted(dict_c.items(), key = lambda x:x[1], reverse = True), end = '\n\n') 
#=======
def stats_text_en(text,symbols):
    text = text.strip().split()
    words = [] # for store the text after processing
    for word in text:
        for  symbol in symbols:
            word = word.replace(symbol,'') # delet the redundant symbols in the text
        words.append(word)

    word_set = set(words) # transfer the list to the set
    counter_dict = {}

    for word in word_set: # count the number for each word
        counter_dict[word] = words.count(word)
    aa = sorted(counter_dict.items(),key = lambda x: x[1], reverse = True)

    return print('the sorted word frequencies for the input english text',aa)

text_sample = '''
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
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
symbols = '.,*-!'

# a example calling the function english text 
stats_text_en(text_sample,symbols)



# 2 for chinese word
def stats_text_cn(text,symbols):
    text = text.strip().split()
    words = [] # for store the text after processing
    for word in text:
        for  symbol in symbols:
            word = word.replace(symbol,'') # delet the redundant symbols in the text
        words.append(word)

    words_cn = [] # for storing the chinese single character
    for word in words:
        for _i in word:
            words_cn.append(_i)
    # print(words_cn)
    word_set = set(words_cn) # transfer the list to the set

    counter_dict = {}

    for word in word_set: # count the number for each word
        counter_dict[word] = words_cn.count(word) # for a dict{key,value} this is: dict[key] = value (value is the frequencies for the word)
    aa = sorted(counter_dict.items(),key = lambda x: x[1], reverse = True)

    return print('the sorted word frequencies for the input chinese text',aa)

text_sample1 = '''
垃圾问题解决不好，群众不答应。垃圾分类，
是生产生活发展到一定阶段之后的产物，
是社会文明水平的重要体现。培养垃圾分类意识，
养成垃圾分类习惯，可以促进群众逐步形成绿色生活方式。
而不管是垃圾分类投放还是收集、转运、处理各个环节，
都需要资金投入，必须有相应的经济社会发展基础。
'''
symbols1 = '.,*-!。，/、？'

# a example calling the function chinese text
stats_text_cn(text_sample1,symbols1)
#>>>>>>> master
