from mymodule import stats_word #从mymodule中导入stats_word
text = ("good frends","123")
try:
    stats_word.stats_text(text)
except ValueError:
    print('Input is not str. try again')
