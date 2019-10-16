import mymodule.stats_word as stats_word

#读取 /009/tang300.json
file_object = open('./d09/tang300.json')
file_content = file_object.read()
file_object.close()

sort_list = {}
try:
    #对列表中中英文字符，进行统计降序排列
    sort_list = stats_word.stats_text_cn(file_content,20)
except ValueError as result:
    print(result)
    
print(sort_list)


