def stats_text_en():
    """统计英文词频的函数""" #使用文档字符串添加注释说明
    import d5_exercise_stats_text #封装代码

def stats_text_cn(s):
    """统计中文词频的函数""" #使用文档字符串添加注释说明
    countcn={}
    for i in s:
        if u'\u4e00'<= i <= u'\u9fff':
            countcn[i]=s.count(i)
    result=sorted(countcn.items(),key=lambda item:item[1],reverse=True)
    return result
