#统计参数中每个英文单词出现的次数，按词频降序排列数组
def stats_text_en(text):  # 统计英文词频
    text = text.replace('.', '')
    text = text.replace('!', '')
    text = text.replace('--', '')
    text = text.replace('*', '')
    text = text.replace(',', '') # 去除标点符号

    list_text = text.split() # 将字符串转换为列表

    import collections 
    m=collections.Counter(list_text)
    return (m)
a = 'Please enter the English word text'
print(stats_text_en(a))

#统计参数中每个中文字出现的次数，按中文出现的次数降序排列数组
def stats_text_cn(text):  # 统计中文词频
    text = text.replace('。', '')
    text = text.replace('！', '')
    text = text.replace('：', '')
    text = text.replace('*', '')
    text = text.replace('，', '') # 去除标点符号

    text = text.replace('', ' ') # 字符之间增加空格

    list_text = text.split() # 将字符串转换为列表

    import collections 
    m=collections.Counter(list_text)
    return (m)
a = '键入文本：投资一下子就跟消费打通了，它们是一回事儿，只不过是人们为了追求最大的收益，在时间上做一个平衡而已。'
print(stats_text_cn(a))


# 学长的数据 统计输入文本中中文字的词频：
def stats_text_cn(text):  
    countcn={}
    for i in text:  # 这个循环有效，说明一串汉字也是一个字符串，每个汉字就是其中的一个元素，可以用for in 来遍历，其中i代表了每个汉字的unicode编码
        if u'\u4e00' <= i <= u'\u9fff':     # 挑选出中文字
            countcn[i] = text.count(i)      # 用.count()函数/方法来对每个元素（这里是汉字）进行计数，形成一个列表
    countcn = sorted(countcn.items(), key=lambda item: item[1], reverse=True)  #按出现数字从大到小排列
    return countcn
a = input("请输入要统计中文字词频的文本：")
print(stats_text_cn(a))

