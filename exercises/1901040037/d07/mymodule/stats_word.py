def stats_text_cn(text):
    """
    统计中文字符字频
    """
    # 处理掉杂七杂八，变为小写之后拆分成单词
    text = text.replace('，' ,' ').replace('。' ,' ').replace('--' ,'').replace('!' ,'').replace('*' ,' ')
    #print(text)

    dic = {}  #搞一个字典统计词频

    for i in text:
        count = text.count(i)
        r = {i:count}
        dic.update(r)
    final = sorted(dic.items(),key=lambda item:item[1], reverse=True)
    print(final)
    
    
def stats_text_en(text):
    """
    统计英文字符字频
    """
    # 处理掉杂七杂八，变为小写之后拆分成单词
    text = text.replace(',' ,' ').replace('.' ,' ').replace('--' ,'').replace('!' ,'').replace('*' ,' ')
    text = text.lower()
    text = text.split()
    #print(text) 尝试输出看是否正确，字符串是不可变，故而要用新的变量接收

    dic = {}

    for i in text:
        count = text.count(i)
        r = {i:count}
        dic.update(r)
    print(dic)

    final = sorted(dic.items(), key=lambda x: x[1], reverse=True)  # 按照单词出现次数，从小到大排序
    print(final) 
    
def stats_text(text):  # 合并英文词频和中文字频的结果
    return stats_text_en(text) + stats_text_cn(text)
