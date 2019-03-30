

# 函数2：统计输入文本中中文字的词频：
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
    count = int(input('请输入要限制输出的元素个数：'))
    dic = collections.Counter(text_list1).most_common(count)  #调用标准库collections.Counter，按出现次数从大到小排列
    return dic




with open('tang300.json','r',encoding='UTF-8') as f:
    text = f.read()
try:
    if not isinstance(text,str):
        raise ValueError()
    
except ValueError:
    print('输入的不是文本格式，请重新输入：')   
    
print(stats_text_cn(text))   
