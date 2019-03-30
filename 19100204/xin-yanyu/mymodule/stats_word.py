# 第八天作业1
# 2019年3月28日
# 修改stats_text、stats_text_en，stats_text_cn函数,
#  在非字符串输入的时候出错提示.



def  stats_text(text_string) :
	'''统计字符样本。返回一个词频统计表.
	
	 stats_text函数分别调用stats_text_en，stats_text_cn,
	输出合并词频统计结果.
	'''
	# z为最终的结果词频字典
	z={}
	#检查是否是字符串
	if text_type_err(text_string)  :
		#数据输入出错，报警，并退出程序
		print('Funtion:stats_text input date  is ValueError')
		return 
	
	x=stats_text_en(text_string)
	y=stats_text_cn(text_string)
	z.update(x)
	z.update(y)
	return z


def  text_type_err(text_string) :
	'''检测字符样本是否是字符串,
	
	错误就返回错误信息.正确返回空
	'''
	# 出错为空
	text_tmp=''
	#字符串相加，检测是否是字符
	err_text=''
	try:
		text_tmep=text_string + ''
		return (err_text)
	except (AttributeError, TypeError) as err_text :
		return (err_text)



def stats_text_en(text_string):
    """ 统计参数中每个英文单词出现的次数，最后返回一个按词频率降序排列的数组.

        使用字典(dict)统计字符串样本text中各个英文单词出现的次数，
        按照出现次数从大到小输出所有的单词及出现的次数 .
    """
    # 将字符串变成列表
    if text_type_err(text_string) :
        print('Funtion:stats_text_en input date is ValueError')
        return 
    
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

	# 检查是否是字符串
	if text_type_err(text_cn_string) :
		#数据输入出错，报警，并退出程序
		print('Funtion:stats_text_cn input date is ValueError')
		return 
	
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





# 调试主程序

#sss='fa sd dfsad dfs adasd收到阿斯蒂芬就发大水 ffsafas  is  is sa'
#sss=0

#print('1')
#print(stats_text(sss))
#print('2')
#print(stats_text_en(sss))
#print('3')
#print(stats_text_cn(sss))



