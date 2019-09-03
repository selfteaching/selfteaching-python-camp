import stats_word as a

text=1234545
try:
    a.stats_text(text)
except ValueError:
    print('ValueError:input date is not string!')


print(a.stats_text(text))