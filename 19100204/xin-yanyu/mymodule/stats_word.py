# 第10天作业
# 2019年3月30日
# 完善词频统计的排序功能子程序
# 修改stats_text、stats_text_en，stats_text_cn函数,
# 使用标准库中Counter来完善stats_word模块中，
# 中英文词频统计的排序功能，使函数能够按照词频出现的次数有序输出.
# 重点注意 collections.Counter most_common([n])这个函数
# 分别给两个函数添加一个int类型变量，用于限制输出元素的个数


def  stats_text(text_string, out_num) :
	'''统计字符样本。返回一个词频统计表.
	
	text_string为字符样板, out_num输出元素个数
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
	
	x=stats_text_en(text_string, out_num)
	y=stats_text_cn(text_string, out_num)
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



def stats_text_en(text_string, out_num):
    """ 统计参数中每个英文单词出现的次数，最后返回一个按词频率降序排列的数组.
	   
	    text_string为字符样板, out_num输出元素个数
        使用字典(dict)统计字符串样本text中各个英文单词出现的次数，
        按照出现次数从大到小输出所有的单词及出现的次数 .
    """
    # 将字符串变成列表
    if text_type_err(text_string) :
        print('Funtion:stats_text_en input date is ValueError')
        return 
    
    text_string_1 = text_string.split(" ")
    # 建立空列表
    text_string_dict=[]
    # 对列表循环遍历
    for text_word in text_string_1 :
	    # 判断是否是全是字母
        if text_word.isalpha() : 
		    #判断是否为中文
            if not(is_Chinese(text_word)) :
				#汉字添加进列表
                text_string_dict.append(text_word)
    # 排序
    from collections import Counter
    kk=Counter(text_string_dict)
	# 按需要输出长度输出数据
    return(kk.most_common(out_num))
    
    


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

def stats_text_cn_old(text_cn_string, out_num):
	""" 统计参数中每个中文汉字出现的次数，最后返回一个按中文汉字频率降序排列的数组.
	    
	    text_string为字符样板, out_num输出元素个数
        使用字典(dict)统计字符串样本text中各个汉字词出现的次数，
        按照出现次数从大到小输出所有的汉字及出现的次数 .
	"""

	# 检查是否是字符串
	if text_type_err(text_cn_string) :
		#数据输入出错，报警，并退出程序
		print('Funtion:stats_text_cn input date is ValueError')
		return 
		
	text_string_1 = text_cn_string
    # 建立空列表
	text_string_dict=[]
    # 对列表循环遍历
	for text_word in text_string_1 :
	    # 判断是否是全是字母
		if text_word.isalpha() : 
		    #判断是否为中文
			if is_Chinese(text_word) :
				#汉字添加进列表
				text_string_dict.append(text_word)
    # 排序
	from collections import Counter
	kk=Counter(text_string_dict)
	# 按需要输出长度输出数据
	return(kk.most_common(out_num))

def stats_text_cn(text_cn_string, out_num):
	""" 统计参数中每个中文汉字出现的次数，最后返回一个按中文汉字频率降序排列的数组.
	    
	    text_string为字符样板, out_num输出元素个数
        使用字典(dict)统计字符串样本text中各个汉字词出现的次数，
        按照出现次数从大到小输出所有的汉字及出现的次数 .
	"""

	# 检查是否是字符串
	if text_type_err(text_cn_string) :
		#数据输入出错，报警，并退出程序
		print('Funtion:stats_text_cn input date is ValueError')
		return 
		
	str = text_cn_string

	#采用 jieba 第三方库
	import jieba
	# 精确模式识别
	seg_list = jieba.cut(str, cut_all=False)
	sss= "/".join(seg_list)
	#print(sss)
	#sss_beg开始
	sss_beg=sss
	num_beg=0
	#词语切片
	sss_cut=''
	#词的断句标志符
	sStr2 = '/'

	# 建立汉字词语空列表
	text_string_dict=[]

	#用find查找逗号所在的索引位置
	while True :
		num_beg=(sss.find(sStr2))

		#取出词汇,-1表示没有、或到结尾
		if num_beg==-1 :
			sss_cut=sss[:num_beg+1]
			#最后一个汉字添加进列表,长度要大于1
			if len(sss_cut)>1 :
				text_string_dict.append(sss)
			break
		else :
			sss_cut=sss[:num_beg]
			#汉字词语添加进列表
			# 判断是否是全是字母
			if sss_cut.isalpha() : 
				#判断是否为中文
				if is_Chinese(sss_cut) :
					#汉字添加进列表,长度要大于1
					if len(sss_cut)>1 :
						text_string_dict.append(sss_cut)
		#删除，找下一组词
		sss = sss[num_beg+1:]
	#排序
	from collections import Counter
	kk=Counter(text_string_dict)
	# 按需要输出长度输出数据
	return(kk.most_common(out_num))









