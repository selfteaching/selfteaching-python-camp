from mymodule import stats_word
if __name__ == "__main__":
    try:
        stats_word.stats_file('D:/Documents/GitHub/selfteaching-python-camp/exercises/1901010167/d09/tang300.json','r',100,0)
    except ValueError :
        print('输入的为非字符串')

                          