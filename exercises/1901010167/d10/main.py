from mymodule import stats_word
if __name__ == "__main__":
    try:
        stats_word.stats_text_cn('D:/Documents/GitHub/selfteaching-python-camp/exercises/1901010167/d10/tang300.json',20)
    except ValueError :
        print('输入的为非字符串')

                          