t = 5

from stats_word import stats_text
try:
    stats_text(t)
except TypeError:
    print('The input is not string...')
else:
    print('Figure out what\'s wrong then...I have no clue either...')