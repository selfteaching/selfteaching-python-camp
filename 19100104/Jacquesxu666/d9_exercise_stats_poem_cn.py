# _*_ coding:utf-8 _*_

from mymodule import stats_word as sw
with open('tang300.json',encoding='UTF-8') as poem:
    read_file = poem.read()
poem.closed

print ('唐诗中最多的100个字：',sw.stats_text_cn(read_file,100))
