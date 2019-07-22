
text={1,2,3,4,5}

from mymodule import stats_word
try:
    stats_word.stats_text(text)
except ValueError:
    print('error:text is not the string')