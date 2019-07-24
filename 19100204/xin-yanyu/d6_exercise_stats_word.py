# 第六天作业
# 2019年3月26日
# 掌握函数的用法
def stats_text_en(text_string):
    """ 统计参数中每个英文单词出现的次数，最后返回一个按词频率降序排列的数组.

        使用字典(dict)统计字符串样本text中各个英文单词出现的次数，
        按照出现次数从大到小输出所有的单词及出现的次数 .
    """
    
    # 将字符串变成列表
    text_string_1 = text_string.split(" ")
    # 建立空白字典
    text_string_dict={}

    # 对列表循环遍历
    for text_word in text_string_1 :
	
	    # 判断是否是全是字母
	    if text_word.isalpha() : 

		    # 0为第一次
		    i=0
		    # k,V变量的关键字、键值
		    for k , v in text_string_dict.items():
			    if k == text_word :
				    text_string_dict[k]=v+1
				    i = 1
		    # # 0为第一次，字典添加
		    if i == 0 :
			    text_string_dict.setdefault(text_word,1)

    #按照item中的第2字符进行排序，即按照key排序
    import operator
    sorted_x=sorted(text_string_dict.items(),key=operator.itemgetter(1),reverse=True)

    return  sorted_x


def is_Chinese(word):
	""" 判断是否是汉字.
	
	汉字也是有数字表示的，Unicdoe4E00~9FFF表示中文，
	所以如果一个字符的utf-8编码在这个区间内，
	就说明它是中文。
	"""
	for ch in word:
		if '\u4e00' <= ch <= '\u9fff':
			return True
	return False

def stats_text_cn(text_cn_string):
	""" 统计参数中每个中文汉字出现的次数，最后返回一个按中文汉字频率降序排列的数组.

        使用字典(dict)统计字符串样本text中各个汉字词出现的次数，
        按照出现次数从大到小输出所有的汉字及出现的次数 .
	"""
	i=0
	# 建立空白字典
	text_string_dict={}	
	s_3 = text_cn_string
	#遍历字符串
	for j in s_3:
		#是否是中文
		if is_Chinese(j):
			i=0
			#遍历词典
			for k , v in text_string_dict.items():
				if k == j :
					text_string_dict[k]=v+1
					i = 1
			if i == 0 :
				text_string_dict.setdefault(j,1)
	
	    #按照item中的第2字符进行排序，即按照key排序
	import operator
	sorted_x=sorted(text_string_dict.items(),key=operator.itemgetter(1),reverse=True)
	return sorted_x


# 主程序
# 英文处理主程序
# 长字符串
text_string_1 = (' \'\'\''  +  ' ' +
                'The Zen of Python, by Tim Peters'  +  ' ' +
                'Beautiful is better than ugly.'  +  ' ' +
                 'Explicit is better than implicit.'  +  ' ' +
                 'Simple is better than complex.'  +  ' ' +
                 'Complex is better than complicated.'  +  ' ' +
                 'Flat is better than nested.'  +  ' ' +
                 'Sparse is better than dense.'  +  ' ' +
                 'Readability counts.'  +  ' ' +
                 'Special cases aren\'t special enough to break the rules.'  +  ' ' +
                 'Although practicality beats purity.'  +  ' ' +
                 'Errors should never pass silently.'  +  ' ' +
                 'Unless explicitly silenced.'  +  ' ' +
                 'In the face of ambxiguity, refuse the temptation to guess.'  +  ' ' +
                 'There should be one-- and preferably only one --obvious way to do it.'  +  ' ' +
                 'Although that way may not be obvious at first unless you\'re Dutch.'  +  ' ' +
                 'Now is better than never.'  +  ' ' +
                 'Although never is often better than *right* now.'  +  ' ' +
                 'If the implementation is hard to explain, it\'s a bad idea.'  +  ' ' +
                 'If the implementation is easy to explain, it may be a good idea.'  +  ' ' +
                 'Namespaces are one honking great idea -- let\'s do more of those!'  +  ' ' +
                  '\'\'\''  )

    
# 打印按照出现次数从大到小输出所有的单词及出现的次数 
print (text_string_1)
print ('-----------------------')
text_num = stats_text_en(text_string_1)
print('打印按照出现次数从大到小输出所有的单词及出现的次数')
print(text_num)

# 中文处理主程序
text_string_2 = ('自我成长 严雨学习李笑来 灯心草心随风动 sdfggsfg' +
                 ' 学习学习再学习 ' +
                 '自学能力asdfsdf 坚持就是' )
                 
# 打印按照出现次数从大到小输出所有的汉字及出现的次数 
print('\n\n原中文字符串 =')
print (text_string_2)
print ('\n\n-----------------------')
print('打印按照出现次数从大到小输出所有的汉字及出现的次数')
print(stats_text_cn(text_string_2))
