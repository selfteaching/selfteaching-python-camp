text = 123

from mymodule.stats_word import stats_text
try:
    stats_text(text)
    print(stats_text(text))
except ValueError:
    print("The text is not a string. Please input a string.")

