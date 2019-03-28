
from mymodule import stats_word
text = (3,4,5,6)
try:
    stats_word.stats_text(text)
except ValueError as error:
    print(error)
   

