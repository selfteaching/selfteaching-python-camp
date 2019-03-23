template = '''
    The Zen of Python, by Tim Peters
    美丽 is better than 丑陋.
    清楚 is better than 含糊.
    简单 is better than 复杂.
    复杂 is better than 难懂.
    单一 is better than 嵌套.
    稀疏 is better than 稠密.
    可读性计数.
    Special cases aren't special enough to 打破规则.
    即使练习会使得不再纯粹.
    但错误不应该用沉默来掩盖.
    Unless explicitly silenced.
    面对起义，拒绝猜的诱惑.
    有且只有一个办法.
    Although that way may not be obvious at first unless you're Dutch.
    尝试总比从未试过要强.
    Although never is often better than *right* now.
    如果执行很难被解释，那将是一个很糟的想法.
    如果执行很容易解释，这会是一个好点子.
    Namespaces are one honking great idea -- 让我们继续为之努力!
    '''
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
	cndic = {}
	for i in checkstr:
		if '\u4e00' <= i <= '\u9fff':
			cndic[i] = checkstr.count(i)
	return cndic

def main():
	cndic = stats_text_cn(template)             #调用检索中文频次的函数

	cndic=sorted(cndic.items(),key=lambda item:item[1],reverse = True)      #为了阅读方便，检索完毕后对字典进行按值从大到小排序
	print(cndic)                            #打印汉字

	endic = stats_text_en(template)             #调用检索中文频次的函数

	endic=sorted(endic.items(),key=lambda item:item[1],reverse = True)      #为了阅读方便，检索完毕后对字典进行按值从大到小排序
	print(endic)                            #打印汉字

if __name__ == '__main__':
	main()
