# 第七天作业1
# 2019年3月27日
# stats_text函数分别调用stats_text_en，stats_text_cn，输出合并词频统计结果



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
		    #判断是否为中文
		    kk=is_Chinese(text_word)

		    # k,V变量的关键字、键值
		    for k , v in text_string_dict.items():
				#非中文，非第一次
			    if not(kk) and k == text_word :
				    text_string_dict[k]=v+1
				    i = 1
		    # # 0为第一次，非中文，字典添加
		    if not(kk) and i == 0 :
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


def  stats_text(text_string) :
	'''统计字符样本。返回一个词频统计表.
	
	 stats_text函数分别调用stats_text_en，stats_text_cn,
	输出合并词频统计结果.
	'''
	x=stats_text_en(text_string)
	y=stats_text_cn(text_string)
	z={}
	z.update(x)
	z.update(y)
#	print(z)
	return (z)

