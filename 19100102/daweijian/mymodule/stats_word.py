
#封装d5的代码
def cut_clean(s):
    #切分字符串
    s=s.split()
    #清洗标点符号
    i=0
    while i<len(s):
        s[i]=s[i].strip('*-.')
        if s[i]=='': #清洗完成之后若为空元素‘’，则删除元素
            s.remove('')
        else:
            i=i+1
    return s

#把list转化为dict并统计词频
def list_dict(aList):
    aDict={}
    for i in range(len(aList)):
        aDict[aList[i]]=0
    for i in range(len(aList)):
        aDict[aList[i]]=aDict[aList[i]]+1
    return aDict

def stats_text_en(checkstr):
    checkstr = cut_clean(checkstr) #切分字符串并清洗标点符号
    s_dict = list_dict(checkstr) #将tempiate转化为字典并统计词频
    #对字典按照value值排序
    s_s_dict = sorted(s_dict.items(),key=lambda item:item[1],reverse=True)
    print(s_s_dict)
    return s_s_dict

def stats_text_cn(checkstr):    #定义检索中文函数
    cut_clean(checkstr)
    cndic = {}
	for i in checkstr:
		if '\u4e00' <= i <= '\u9fff':
			cndic[i] = checkstr.count(i)
	return cndic

#定义stats_text函数
def stats_text(str):
    stats_text_cn(str)          #导入stats_text_cn函数
    stats_text_en(str)          #导入stats_text_en函数

