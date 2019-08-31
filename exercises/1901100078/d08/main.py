text = 123

from mymodule import stats_word
try:
    print('中英文字频====>', stats_word.stats_text(text))
except ValueError:
    print("print out the error: ",ValueError)


