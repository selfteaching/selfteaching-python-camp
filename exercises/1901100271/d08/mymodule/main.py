from mymodule import stats_word
text = 123
try:
    stats_word.stats_text(text)
except ValueError as error:
    print(error)
