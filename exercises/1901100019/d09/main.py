from mymodule import stats_word

if __name__ == '__main__':
    f = open('/Users/chaishaoguo/Documents/myGitHub/selfteaching-python-camp/exercises/1901100019/d09/tang300.json', 'r')
    text = f.read()

    print('统计中文词频:')
    print(stats_word.stats_text_cn(text, 100))

    f.close()