def stats_text_cn(checkcn):    # 定义检索中文字符
    countcn={}    # 初始化一个词典
    """Count the chinese in the text"""    # 注释
    for i in checkcn:
        if u'\u4e00' <= i <= u'\u9fff':    # 中文字符的正则表达式
            countcn[i] = checkcn.count(i)
    countcn = sorted(countcn.items(), key=lambda item:item[1], reverse=True)
    print(countcn)
    return countcn

def stats_text_en(checken):    # 定义检索英文字符（在D5的作业基础上添加检查英文字符功能）
    counten={}    # 新字典
    entext=" "    # 空的字符串
    checken=checken.replace(',',' ').replace('.',' ').replace('--',' ').replace('!',' ').replace('*',' ')
    
    for i in checken:
        if i.isascii():    # 去掉非英文字符
            entext=entext+i    #放进空字符串中
            
    entext=entext.split()    # 分隔
    
    for i in entext:
        counten[i]=entext.count(i)    # 检索出来的内容放进新字典
    counten=sorted(counten.items(),key=lambda item:item[1],reverse=True)    # 安置排序
    print(counten)
    return counten

def stats_text(check_cn_en):   # 定义函数
    '''定义函数功能，分别统计中英文词频'''
    stats_text_cn(checkcn)
    stats_text_en(checken)