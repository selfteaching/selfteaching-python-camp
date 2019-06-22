
def stats_text_en(text):
    ''' 统计英文单词词频出现的次数 '''
    text1 = text.replace(',','').replace('.','').replace('--','').replace('*','').replace('!','')
    list = ''
    for i in text1: #只保留英文单词
        if i.isascii():
            list += i
    text2 = list.split() #把字符串转化为列表

    d1 = {}
    for i in text2:
        count = text2.count(i)
        r1 = {i:count}
        d1.update(r1)
    #print(d)
    d2 = sorted(d1.items(),key = lambda x:x[1],reverse = True) #按照单词出现的次数进行排序
    return d2
#print(stats_text_en(text))


def stats_text_cn(text):
    ''' 统计中文文字出现的次数 '''
    d3 = {}
    for i in text:
        if u'\u4e00' <= i <= u'\u9fa5': #提取中文汉字
            count = text.count(i)
            r2 = {i:count}
            d3.update(r2)
    d4 = sorted(d3.items(),key = lambda x:x[1],reverse = True)
    return d4
#print(stats_text_cn(text))

def stats_text(text): 
    ''' 分别调用stats_text_en和stats_text_cn方法输出合并词频统计结果 '''
    print(stats_text_en(text)+stats_text_cn(text))


    