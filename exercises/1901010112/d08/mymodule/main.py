from stats_word import stats_text
text = 2665656
try:
    print(stats_text(text))
except ValueError as err:
    print('Handling error:', err)