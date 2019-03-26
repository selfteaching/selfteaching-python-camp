# 第五天作业2-完成
#  2019年3月25日
# 统计字符串样本中英文单词出现的次数 
# 1．创建一个名为d5_exercise_stats_text. Py的文件 
# 2.使用字典(dict)统计字符串样本text中各个英文单词出现的次数。
# 示例:{'is':10, 'better': 9, . } 
# 3.按照出现次数从大到小输出所有的单词及出现的次数 
# 4.只统计英文单词，不包括非英文字符的其他任何符号，如连接符号、空白字符等 


# 长字符串
text_string = (' \'\'\''  +  ' ' +
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

# 将字符串变成列表
text_string_1 = text_string.split(" ")

print ('#####---------')
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
# 打印列表			

print ()	
		
print('#####')

#按照item中的第2字符进行排序，即按照key排序
import operator
sorted_x=sorted(text_string_dict.items(),key=operator.itemgetter(1),reverse=True)

# 打印按照出现次数从大到小输出所有的单词及出现的次数 
print (sorted_x)	
