def stats_text_en(text):
    """统计输入文本中的英文字频，从大到小排序"""
    import re 
    scope_en="[a-zA-Z]+" #定义英文单词
    list_en=re.findall(scope_en,text) #将提取的英文放入列表
    dic={}
    for it in list_en:
        if it not in dic:
            dic[it] = 1
        else: dic[it] += 1###统计词频
    dic = sorted(dic.items(),key=lambda x:x[1],reverse=True)#排序
    print(dic)
################################
def stats_text_cn(text):
    """统计输入文本中的中文字频，从大到小排序"""
    import re
    dic1={}
    for i in text:
        if u'\u4e00' <= i <= u'\u9fa5':   #提取中文汉字   
            dic1[i]=text.count(i)
    dic2=sorted(dic1.items(),key=lambda x:x[1],reverse=True)
    print(dic2)

text="I love this game,but I think it is very hard to me.我很喜欢这个游戏，但是这游戏于我而言太难了"
print(stats_text_en(text))
print(stats_text_cn(text))
