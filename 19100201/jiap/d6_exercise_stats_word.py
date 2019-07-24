# -*- encoding:utf-8 -*-
def stats_text_en(text):
	# substitute useless characters
	replace_text = text.replace('--','').replace(',','').replace('.','').replace('*','').replace('!','')
	# split the words
	split_text = replace_text.split()
	# creat a new blank dict
	frequency = {}
	for word in split_text:
	    if word not in frequency:
	    	# if word is not in split_text, creat a new key and let counts be 1
	        frequency[word] = 1
	    else:
	    	# if words is in split_text, let counts added 1
	        frequency[word] += 1

	# sorted reverse        
	return sorted(frequency.items(), key=lambda d: d[1], reverse=True)


def stats_text_cn(text):
	# remove Chinese characters
	replace_text = text.replace('-','').replace('，','').replace('。','').replace('；','').replace('！','')
	# set new dict
	frequency_cn = {}
	# frequency stat
	for word_cn in replace_text:
		if word_cn not in frequency_cn:
			frequency_cn[word_cn] = 1
		else:
			frequency_cn[word_cn] += 1
	return sorted(frequency_cn.items(), key=lambda d: d[1], reverse=True)



text = "为蛇口蛇设阿拉的喝口茶"
print(stats_text_cn(text))

text_en = '''
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
'''
print(stats_text_en(text_en))








