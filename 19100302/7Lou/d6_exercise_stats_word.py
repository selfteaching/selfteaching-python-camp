text='''It is the time you have wasted for your rose that makes your rose so important
你在你的玫瑰花身上耗费的时间,使得你的玫瑰花变得如此重要!!!!!!!!!。。。。、//、、、////。。!!!!'''
import re

#统计参数中每个英文单词出现的次数，按词频降序排列数组
def stats_text_en(text):
    for x in text:
        if u'\u4e00' <= x <= u'\u9fff' :
            text = text.replace(x,'')#替换掉中文字符
            text = re.sub('[\\!、。\，\,/:*?"<>|]', '', text)
            #text = text.replace("\n"," ").replace(","," ").replace("."," ").replace("*"," ").replace("--"," ").replace("!","").replace("。","").replace("、","".replace("/",""))
            d = {}
            for x in text.split():
                if x not in d:
                    d[x] =1
                else:
                    d[x]+=1
    return sorted(d.items(), key=lambda x: x[1],reverse=True)


#统计参数中每个汉字出现的次数，按字频降序排列数组
def stats_text_cn(text):
    '''统计参数中每个汉字出现的次数，按字频降序排列数组'''
    d = {}
    for x in text:
        if u'\u4e00' <= x <= u'\u9fff' :
            d[x] = text.count(x)
    return sorted(d.items(), key=lambda x: x[1], reverse=True) #按出现数字从大到小排列
