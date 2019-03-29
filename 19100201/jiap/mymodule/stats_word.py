# -*- encoding:utf-8 -*-
import re

frequency = {}
frequency_cn = {}

def stats_text_en(text):
	if type(text) != str:
		# print("Not string")
		raise ValueError("Not en_string")

	else:
		en = re.compile(r'[\u0061-\u007a,\u0020]')
		en = "".join(en.findall(text.lower()))

		if en == "":
			return "There is no English characters."
		else:
			# substitute useless characters
			replace_text = en.replace('--','').replace(',','').replace('.','').replace('*','').replace('!','').replace('”','').replace('“','').replace('「','').replace('」','').replace('?','').replace('\n','')
			# split the words
			split_text = replace_text.split()
			# creat a new blank dict
			for word in split_text:
			    if word not in frequency:
			    	# if word is not in split_text, creat a new key and let counts be 1
			        frequency[word] = 1
			    else:
			    	# if words is in split_text, let counts added 1
			        frequency[word] += 1

			return frequency
			# return sorted(frequency.items(), key=lambda d: d[1], reverse=True)


def stats_text_cn(text):
	if type(text) != str:
		raise ValueError("Not cn_string")
	else:
		cn = re.compile(r'[^\u0061-\u007a,\u0020]')
		cn = "".join(cn.findall(text.lower()))

		# 考虑到中文字符串为空，输出结果
		if cn == "":
			return "There is not Chinese characters."
		else: 
		# remove Chinese characters
			replace_text = cn.replace('--','').replace('，','').replace('。','').replace('*','').replace('！','').replace('”','').replace('“','').replace('「','').replace('」','').replace('？','').replace('\n','')
			for word_cn in replace_text:
				if word_cn not in frequency_cn:
					frequency_cn[word_cn] = 1
				else:
					frequency_cn[word_cn] += 1
			return frequency_cn
			# return sorted(frequency_cn.items(), key=lambda d: d[1], reverse=True)


def stats_text(text):
	if type(text) != str:
		raise ValueError("Not string")
	else:
		stats_text_en(text)
		stats_text_cn(text)
		frequency_sum = {**frequency, **frequency_cn}
		return sorted(frequency_sum.items(), key=lambda d: d[1], reverse=True)

# 任务1. 直接运行：python stat_words.py 会抛出错误结果（下面两行）
# text = ["a"]
# stats_text_en(text)
