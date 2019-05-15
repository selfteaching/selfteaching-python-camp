text = ''' 学号：1901050095
姓名：陆永超
学习内容：day6掌握函数的用法
1、封装day5的函数，封装其实很简单，就是定义（def）之后，直接运行（函数名+参数）。
2、知道了汉字字符在u4e00 到u9fa5之间，
学习用时：2天
收获总结：又反复看了数据容器的内容，把day5的第2个作业又思考了多次。
遇到的难点与问题（是否解决）：
1、关于文件的读取，还是没看明白，这次作业还是把样本文档放在程序文件中。希望后面会单独存放文本文件，并进行处理
2、辅导员发的视频很好。
'''

def stats_text_cn(text):    #定义函数，参数text可变
	text = text.replace(',',' ').replace('.',' ').replace('\'','').replace('-',' ').replace('!',' ').replace('*',' ')#去标点符号
	setb=set(text)        #设定集合
	x=[]                  #设定x列表
	for c in setb:        #c从集合setb中取
	    if c >= u'\u4e00' and c <= u'\u9fa5':       #如果c是在u4e00 到u9fa5之间（汉字）
	        count=text.count(c)     #统计每个汉字的数量
	        y=(c,count)
	        x.append(y)         #将y加到x列表中
	x=sorted(x,key=lambda kv:kv[1],reverse=True)    #按重复次数，由大到小排列
	print(x)

stats_text_cn(text) #运行函数，测试通过，完成任务2