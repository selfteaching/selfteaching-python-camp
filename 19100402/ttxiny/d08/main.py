a={1,2,3,4,5}
from mymodule import stats_word
try:
    stats_word.stats_text(a)
except ValueError:
    print('Error: input is not string.')
