from mymodule import stats_word
from collections import Counter
import json

json_file = open('/Users/adamlu/Documents/GitHub/selfteaching-python-camp/exercises/1901090022/d09/1001S02E09.json')
jason_data = json.load(json_file)

text = ""
for poetry in jason_data:
    text += poetry['contents']
word_list = stats_word.stats_text_cn(text, 20)
print(word_list)