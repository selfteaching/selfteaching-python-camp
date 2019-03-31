#统计参数中每个英文单词出现的次数，按词频降序排列数组
def stats_text_en(str):
    str = str.replace("\n"," ").replace(","," ").replace("."," ").replace("*"," ").replace("--"," ")
    d = {}
    for x in str.split():
        if x not in d:
            d[x] =1
        else:
            d[x]=d[x]+1
    print (sorted(d.items(), key=lambda item: item[1],reverse=True)) 


#统计参数中每个汉字单词出现的次数，按字频降序排列数组
def stats_text_cn(text):
    d = {}
    for x in text:
        if u'\u4e00' <= x <= u'\u9fff' :
            d[x] = text.count(x)
    print(sorted(d.items(), key=lambda item: item[1], reverse=True))  #按出现数字从大到小排列
