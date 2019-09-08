from mymodule import stats_word

if __name__ == '__main__':
    with open('C:/Users/Github/selfteaching-python-camp/exercises/1901100042/d09/tang300.json',encoding='UTF-8') as f:
        text = f.read()

    print('统计中文词频:',)
    print(stats_word.stats_text_cn(text, 100))

 