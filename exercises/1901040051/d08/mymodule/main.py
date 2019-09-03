import sys
sys.path.append('C:')
import stats_word
try:
    stats_word.stats_text()
except  ValueError:
    print('Invalid argument.')
