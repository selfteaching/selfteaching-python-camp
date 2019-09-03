from mymodule import stats_word
with open('C:/Users/lvqia/Documents/GitHub/selfteaching-python-camp/19100402/Autumn0808/d09/tang300.json', encoding='UTF-8') as read_file:
    
    try: 
        print('前100汉字字频统计结果： ', stats_word.stats_text_cn(read_file,100))
    except ValueError as modify :
        print(modify)


