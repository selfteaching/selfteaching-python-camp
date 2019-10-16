import stats_word
text = 111
try:
    print(stats_word.stats_text(text))
except ValueError:
    print('Oops!  That was no str text.  Pls try again...')