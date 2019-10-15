import re    ##########导入入正则表达式
import collections   ######引入collections模块
def stats_text_en(t):
    t = re.sub("[^A-Za-z]", " ", t)
    t = t.lower()
    t = t.split()
    t = collections.Counter(t)
    print('英文单词词频: \n',t)

def stats_text_cn(t):
    t = re.sub("[A-Za-z.。，,'！\-* \n]", "", t)
    for t1 in t:
        t1 = t.split()
    t=collections.Counter(t)
    print('中文汉字字频：\n',t)

stats_text_en(t)
stats_text_cn(t)
def stats_text(t):
    return(stats_text_en(t),stats_text_cn(t))