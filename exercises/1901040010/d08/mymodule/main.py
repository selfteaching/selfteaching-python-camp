text = False

from stats_word import stats_text

try:
    stats_text(text)
except ValueError:
    print('The text should be a string.')