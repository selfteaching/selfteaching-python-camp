def stats_text_cn(text):    #定义检索中文函数
    dict={}
    for i in text:
        if u'\u4e00' <= i <= u'\u9fa5': #提取中文汉字，\u是unincode编码，u4e00是十六进制表达值
            dict[i]=text.count(i)
        list2= sorted(dict.items(),key=lambda x:x[1],reverse=True) #降序排列
    print(list2)
    return


def stats_text_en(text):#定义检索英文函数
    t = text.replace(',',' ').replace('.',' ').replace('-',' ').replace('"',' ').replace('!',' ').replace('?',' ') #替换标点为空格

    list = ''   #存储英文单词的字符串
    
    for s in t:  # 只保留英文单词
        if s.isascii():
            list += s

    t1= list.split()
    
    dict = {}#统计单词出现次数
    for i in t1:
        dict[i] = dict.get(i, 0) + 1
    
    list1= sorted(dict.items(),key=lambda x:x[1],reverse=True) #降序排列
    print(list1)
    return

def stats_text(text):
    stats_text_cn(text)
    stats_text_en(text)
    return

        

