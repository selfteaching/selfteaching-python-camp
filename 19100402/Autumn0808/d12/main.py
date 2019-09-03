from mymodule import stats_word
with open('C:/Users/lvqia/Documents/GitHub/selfteaching-python-camp/19100402/Autumn0808/d09/tang300.json',encoding='UTF-8') as t:
    read_file = t.read()
t.closed
   
try: 
    print('前20汉字字频统计结果： ', stats_word.stats_text_cn(read_file,20))
except ValueError as modify :
    print(modify)