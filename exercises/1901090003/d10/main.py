from mymodule import stats_word

file = open('/Users/Justco/selfteaching-python-camp/exercises/1901090003/d09/tang300.json','rb')
text1 = file.read()
text = text1.decode()

print(stats_word.stats_text_cn(text,20))

file.close()




