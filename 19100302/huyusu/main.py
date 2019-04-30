#import stats_word
#import mymodule.stats_word

#import os
#import json

#text1 = 1

#while True:
    #try:
        #stats_word.stats_text(text1)
       #break
    #except ValueError:
        #print("导入字符非法")
        #raise


from mymodule import stats_word as sw
with open('tang300.json',encoding='UTF-8') as poem:

#with open('/Users/huyusu/Documents/GitHub/selfteaching-python-camp/19100302/huyusu/main.py',encoding='UTF-8') as poem:

#with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tang300.json')) as poem:

#with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tang300.json')) as f :

    read_file = poem.read()
    #read_file = f.read()

    poem.closed
    #f.closed

print ('唐诗中词频前20的词和词频数：',sw.stats_text_cn(read_file,20))





