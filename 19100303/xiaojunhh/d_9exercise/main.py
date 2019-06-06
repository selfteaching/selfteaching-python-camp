# -*- coding: UTF-8 -*-

from mymodule import stats_word #导入stats_word模块
with open('tang300.json') as tan:
    read_file = tan.read()
tan.closed

try:
    print('字数最多前100统计： ', stats_word.stats_text_cn(read_file, 100))
except ValueError as w:
    print(w)