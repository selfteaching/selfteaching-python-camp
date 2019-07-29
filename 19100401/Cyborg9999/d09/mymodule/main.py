# _*_ coding:utf-8 _*_

import stats_word as sw
with open(r'/Users/chengyue/Documents/GitHub/selfteaching-python-camp/19100401/Cyborg9999/d09/mymodule/tang300.json',encoding='UTF-8') as poem:
    read_file = poem.read()

print ('唐诗中最多的100个字：',sw.stats_text_cn(read_file,100))
