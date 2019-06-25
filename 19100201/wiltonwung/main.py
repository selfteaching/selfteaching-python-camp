
import json
from mymodule import stats_word

with open('tang300.json') as text:
    




    #try:
        #stats_word.stats_text(text)
    #except ValueError as error:
     #   print(error)
  #  print(text)
    a = text.read()


    print(stats_word.stats_text_cn(a,20))