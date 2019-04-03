#import stats_word
import mymodule.stats_word

#text1 = 1

#while True:
    #try:
        #stats_word.stats_text(text1)
       #break
    #except ValueError:
        #print("导入字符非法")
        #raise


#from mymodule import stats_word as sw
with open('tang300.json',encoding='UTF-8') as poem:
    read_file = poem.read()
poem.closed

print ('唐诗中最多的100个字：',sw.stats_text_cn(read_file,100))