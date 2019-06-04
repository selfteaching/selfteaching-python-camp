def stats_text_en():
    #封装代码
    import d5_exercise_stats_text 

def stats_text_cn(text):
    countcn={}
    for i in text:
        if u'\u4e00'<= i <= u'\u9fff':
            countcn[i]=text.count(i)  #统计中文词频
    result=sorted(countcn.items(),key=lambda item:item[1],reverse=True)  #按字频率降序排列
    return result #返回数组