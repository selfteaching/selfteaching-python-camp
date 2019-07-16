from os import path
import mymodule.stats_word as stats_word

cwd = path.abspath(path.dirname(__file__))
txt_path = path.join(cwd,'tang300.json')
#读取 /009/tang300.json
file_content = ''
with open(txt_path,'r') as file_object:
    for line in file_object:
        file_content = file_content + line
try:
    #对列表中中英文字符，进行统计降序排列
    sort_list = stats_word.stats_text_cn(file_content,20)
except ValueError as result:
    print(result)
    
print(sort_list)


