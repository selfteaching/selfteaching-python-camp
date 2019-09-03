import stats_word

text =1234
try:
    stats_word.stats_text_en(text)
except ValueError:
    print('Invalid string')
