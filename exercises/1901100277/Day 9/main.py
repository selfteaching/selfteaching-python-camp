from mymodule import stats_word
import json


# string = 123456789
# try:
#     stats_word.stats_text(string)
# except ValueError as error:
#     print(error)


#读取本地文件，进行词频统计

with open(r'E:\xuefeng\selfteaching-python-camp\exercises\1901100277\Day 09\mymodule\tang300.json', 'r',encoding='utf-8') as f:
    #  https://www.liaoxuefeng.com/wiki/1016959663602400/1017607179232640  廖雪峰:文件的读写

    cn_text = f.read()  # 读取文件全部内容
    

print(stats_word.stats_text_cn(cn_text))



