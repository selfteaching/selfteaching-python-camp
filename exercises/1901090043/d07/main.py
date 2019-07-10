import mymodule.stats_word as stats_word

#读取/007/text.txt
file_object = open('./d07/text.txt')
file_content = file_object.read()
file_object.close()

#对列表中中英文字符，进行统计降序排列
sort_list = stats_word.stats_text(file_content)

print(sort_list)