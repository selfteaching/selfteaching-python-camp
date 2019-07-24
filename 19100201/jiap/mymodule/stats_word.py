# -*- encoding:utf-8 -*-
import re
import jieba
from collections import Counter





def stats_text_en(text,num):
	if type(text) != str:
		# print("Not string")
		raise ValueError("Not en_string")
	else:
		en = re.compile(r'[\u0061-\u007a,\u0020]')
		en = "".join(en.findall(text.lower()))
		count_en = num
		if en == "":
			return "There is no English characters."
		else:
			# substitute useless characters
			replace_text = en.replace('--','').replace(',','').replace('.','').replace('*','').replace('!','').replace('”','').replace('“','').replace('「','').replace('」','').replace('?','').replace('\n','')
			# split the words
			split_text = replace_text.split()
			# creat a new blank dict
			
			cnt_en = Counter()
			for word in split_text:
				cnt_en[word] += 1

			return cnt_en.most_common(count_en)
			# return sorted(frequency.items(), key=lambda d: d[1], reverse=True)


def stats_text_cn(text,num):
	if type(text) != str:
		raise ValueError("Not cn_string")
	else:
		cn = re.compile(r'[^\u0061-\u007a,\u0020]')
		cn = "".join(cn.findall(text.lower()))
		count_cn = num
		# 考虑到中文字符串为空，输出结果
		if cn == "":
			return "There is not Chinese characters."
		else: 
		# remove Chinese characters
			replace_text = cn.replace('--','').replace('，','').replace('。','').replace('*','').replace('！','').replace('”','').replace('“','').replace('「','').replace('」','').replace('？','').replace('\n','')
			words = [word for word in jieba.cut(text, cut_all=False) if len(word) >= 2]
			cnt_cn = Counter()
			for word in words:
				cnt_cn[word] += 1

			return cnt_cn.most_common(count_cn)
			# return sorted(frequency_cn.items(), key=lambda d: d[1], reverse=True)




def stats_text(text,num):
	if type(text) != str:
		raise ValueError("Not string")
	else:
		s_en = stats_text_en(text, num)
		s_cn = stats_text_cn(text, num)
		# frequency_sum = {**s_en, **s_cn}
		frequency_sum = s_cn + s_en
		return frequency_sum

# 任务1. 直接运行：python stat_words.py 会抛出错误结果（下面两行）
# test = 'a a a c d s 中文 英文 中文'

# print(stats_text(test, 4))





