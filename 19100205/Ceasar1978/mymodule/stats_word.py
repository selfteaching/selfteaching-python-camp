# 函数1：统计输入文本中英文单词的词频：
def stats_text_en(text):
    if not isinstance(text,str):
        raise ValueError('输入的不是文本格式，请重新输入：') # 第8天作业要求，添加参数类型检查
    text = text.replace('.', '').replace('!', '').replace('--', '').replace('*', '').replace(',', '').replace('(', '').replace(')', '').replace(';', '').replace(':', '').replace('\'', '').replace('?', '').replace('_', '').replace('-', '').replace('/', '') .replace('[', '') .replace(']', '') .replace('\\', '') .replace('\"', '').replace('{', '').replace('}', '').replace('\t', '').replace('\n', '').replace('\r\n', '')    
        
    # 以上替换去除各种标点符号
    list_text = text.split() # 将字符串转换为列表
    import collections
    count = int(input("请输入要限制输出的元素个数："))
    dic = collections.Counter(list_text).most_common(count)
    return dic



# 函数2：统计输入文本中中文字的词频（第10天作业更新，调用第三方库进行分词）：
def stats_text_cn(text): 
    import jieba 
    
    if not isinstance(text,str):
        raise ValueError('输入的不是文本格式，请重新输入：') # 第8天作业要求，添加参数类型检查
    
    dic = {}
    for i in text:  # 这个循环有效，说明一串汉字也是一个字符串，每个汉字就是其中的一个元素，可以用for in 来遍历，其中i代表了每个汉字的unicode编码
        if i < u'\u4e00' or i > u'\u9fff':     # 挑选出非中文字
            text = text.replace(i,'')    # 用替换删除所有非中文字的字符
    text_list = jieba.cut(text,cut_all = False) # 调用第三方库“结巴分词”将文件分词，得到一个列表
    text_list1 = []
    for j in text_list: # 该循环遍历列表中的词语，如果长度大于1，将其加入一个新列表。注意：这里的长度是汉字实际个数，而非编码长度！
        if len(j) > 1:
            text_list1.append(j)
    import collections
    # count = int(input('请输入要限制输出的元素个数：'))
    dic = collections.Counter(text_list1).most_common(10)  #调用标准库collections.Counter，按出现次数从大到小排列
    return dic


# 函数3：统计中英文混合词频：
def stats_text(text):
    '''函数说明：

    本函数的功能是统计输入文本的汉字及英语单词词频，并以降序排列输出。'''
    dic_1 = stats_text_cn(text) # 调用函数1统计中文字词频
    if not isinstance(text,str):
        raise ValueError('输入的不是文本格式，请重新输入：') # 第8天作业要求，添加参数类型检查
    for i in text:
        if u'\u4e00' <= i <= u'\u9fff':
            text = text.replace(i,"") #删除所有中文字
    text = text.replace('「', '').replace('」', '').replace('，', '').replace('。', '').replace('：', '').replace('？', '').replace('！', '')
    # 以上一句删除所有中文标点
    dic_2 = stats_text_en(text) # 调用2函数统计英文单词词频
    dic_3 = {}
    dic_3.update(dic_2)
    dic_3.update(dic_1) # 将之前分别得到的两个中英文词频结果字典合并
    dic_3 = sorted(dic_3.items(),key = lambda x:x[1],reverse = True) # 对合并后的字典进行排序，得出混合排序结果

    return(dic_3)

# print(stats_text(text))

print(stats_text.__doc__)