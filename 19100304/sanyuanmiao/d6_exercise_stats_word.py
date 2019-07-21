#封装统计英文单词词频的函数
text='''People cry,not because they're weak.
It's because they've been strong for too long.
Not what I miss, but I can not go back the past.
Three grand essentials to happiness in this life are something to do,
something to love, and something to hope for. '''
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
print(stats_text_en(text))

#封装统计中文汉子字频的函数
text='''哭泣，不代表脆弱，只因坚强了太久，
我怀念的不是哪个人，而是我那回不去的曾经。
快乐的三大源泉是有所为，有所爱和有所希望。'''
def stats_text_cn(text):  # 统计英文词频
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
print(stats_text_cn(text))