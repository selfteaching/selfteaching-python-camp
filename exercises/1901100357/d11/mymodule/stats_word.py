# encoding=utf-8
from collections import Counter 
import jieba

# 统计参数中每个英文单词出现的次数
def stats_text_en(text, count):
	elements = text.split()
	words = []
	symbols = ',.*-!?'
	for element in elements:
		for symbol in symbols:
			element = element.replace(symbol, '')
		if len(element) and element.isascii():
			words.append(element)
	return Counter(words).most_common(int(count))


# 统计参数中每个中文汉字出现的次数
def stats_text_cn(text, count):
	words = jieba.cut(text)
	tmp = []
	for i in words:
		if len(i) > 1:
			tmp.append(i)
	return Counter(tmp).most_common(count)
	
	# cut_list = jieba.lcut(text, cut_all=False)
	# texts = ", ".join(cut_list)
	# print(cut_list)
	# cn_characters = []
	# for character in texts:
	# 	# unicode中 中文字符的范围
	# 	if '\u4e00' <= character <= '\u9fff':
	# 		cn_characters.append(character)
	# return Counter(cn_characters).most_common(int(count))

	# cut_list = jieba.lcut(text, cut_all=False)
	# print(cut_list)
	# cn_characters = []
	# cn_character_set = set(cut_list)
	# for character in cn_character_set:
	# 	# unicode中 中文字符的范围
	# 	if '\u4e00' <= character <= '\u9fff':
	# 		cn_characters.append(character)
	# # return Counter(cn_characters).most_common(int(count))
	# print(Counter(cn_characters).most_common(int(count)))

	# cut_list = jieba.lcut(text, cut_all=False)
	# print(cut_list)
	# cn_characters = []
	# for character in text:
	# 	# unicode中 中文字符的范围
	# 	if '\u4e00' <= character <= '\u9fff':
	# 		cn_characters.append(character)
	
	# counter = {}
	# cn_character_set = set(cn_characters)
	
	# for character in cn_character_set:
	# 	counter[character] = cn_characters.count(character)
	# # return sorted(counter.items(), key=lambda x:x[1], reverse=True)
	# print(sorted(counter.items(), key=lambda x:x[1], reverse=True))





def stats_text(text, count):
	# if not isinstance(text, str):
	# 	raise ValueError('参数必须是 str 类型，输入类型 %s' % type(text))	
	return stats_text_en(text, count) + stats_text_cn(text,count)

# if __name__ == "__main__":
# 	text = "他来到了网易杭研大厦,网易杭研大厦,网易杭研"
# 	stats_text_cn(text, 10)
