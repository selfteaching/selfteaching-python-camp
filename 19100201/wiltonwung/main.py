
from mymodule import stats_word
try:
    stats_word.stats_text(text)
except ValueError as error:
    print(error)
   
text = (3,4,5,6)
