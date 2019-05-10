from mymodule import stats_word

try:
    text = 123456677
    result=stats_word.stats_text(text)

except ValueError:
    print('ValueError: {}'.format('unexpected type'))

print()