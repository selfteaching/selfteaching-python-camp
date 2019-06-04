def stats_text_en() ：
    """Count the english words in the text"""  #使用文档字符串说明
    import d5_exercise_stats_text  #封装day5任务2的代码



def stats_text_cn(text):  # 统计中文词频
    """Count the chinese words in the text """  # 使用文档字符串说明
    countcn={}
    for i in text:
        if u'\u4e00' <= i <= u'\u9fff':
            countcn[i] = text.count(i)
    countcn = sorted(countcn.items(), key=lambda item: item[1], reverse=True)  #按出现数字从大到小排列
    return countcn






