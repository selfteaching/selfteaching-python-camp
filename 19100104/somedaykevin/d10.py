# _*_ coding:utf-8 _*_

from mymodule import stats_word as sw
with open('tang300.json', encoding='UTF-8') as poem:
    read_file = poem.read()
poem.closed

print('最多的20个词：', sw.stats_text_cn(read_file, 20))