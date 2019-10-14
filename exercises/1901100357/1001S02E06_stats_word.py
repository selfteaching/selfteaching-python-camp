#coding:utf-8
#统计英文词频
def stats_text_en(text):
	from collections import Counter
	import re
	cutt = re.compile(r'[-.*,!?]')#定义去除符号规则
	cuttext = cutt.sub('',text)#去除符号
	glist = sorted(cuttext.split(), key=str.lower)#单词生成数组并排序
	counttext = Counter(glist)#统计次数
	list1 = sorted(counttext.items(), key=lambda x:x[1], reverse=True)#词频排序
	print('统计数据为：', list1)

# 以下为测试
# a = 'I like apple, do you like apple?'
# stats_text_en(a)
# b = 'adjoahgod'
# stats_text_en(b)

#统计中文词频
def stats_text_cn(text):
	
	symbols ='，。！？、（）【】<>《》=：+-*—“”…'#定义需要去掉的字符

	#去掉字符
	for i in symbols:
	    text = text.replace(i, '')

	counter = {}
	#在字典里统计次数
	for j in text:
		if j not in counter:
			counter[j] = 1
		else:
			counter[j] += 1

	list1 = sorted(counter.items(), key=lambda x:x[1], reverse=True)
	
	# print('中文文字去符号 ==>', text)
	# print('文字出现的次数 ==>', counter)
	print('字频排序 ==>', list1)

# 以下是测试
# x = '如果你不觉得正则表达式很难读写的话，要么你是一个天才，要么，你不是地球人。正则表达式的语法很令人头疼，即使对经常使用它的人来说也是如此。由于难于读写，容易出错，所以找一种工具对正则表达式进行测试是很有必要的。'
# stats_text_cn(x)
