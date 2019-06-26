import mymodule.stats_word as stats_word

text = 99998

#对列表中中英文字符，进行统计降序排列
sort_list = stats_word.stats_text_en(text)

print(sort_list)