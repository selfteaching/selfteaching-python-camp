# 第五天作业1-完成
#  2019年3月25日
# 1.字符串的基本处理
# 2.将字符串样本text里的better全部替换成worse
# 3.从第2步的结果里，将单词中包含ea的单词剔除
# 4.将第3步的结果里的字母进行大小写翻转(将大写字母转成小写，小写字母转成大写)
# 5.将第4步的结果里所有单词按a…z升序排列，并输出结果

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

# 将字符串样本text里的better全部替换成worse
text_string_1=text_string.replace('better','worse')

# 将字符串变成列表
text_string_2 = text_string_1.split(" ")

# 3.从第2步的结果里，将列表中单词中包含ea的单词剔除
for del_word in text_string_2 :
	if 'ea' in  del_word :
		text_string_2.remove(del_word) 
		

# 4.将第3步的结果里的字母进行大小写翻转(将大写字母转成小写，小写字母转成大写)
text_string_3=text_string_2

for i in range(len(text_string_3)):
   text_string_3[i]=text_string_3[i].swapcase()

# 打印结果
print('========================')
print(sorted(text_string_3))
