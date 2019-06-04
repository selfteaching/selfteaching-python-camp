import mymodule.stats_word
import codecs

with open('tang300.json',mode='r', encoding='UTF-8') as a:
    text_cn = a.read()
    a.closed

mymodule.stats_word.stats_text_cn(text_cn)