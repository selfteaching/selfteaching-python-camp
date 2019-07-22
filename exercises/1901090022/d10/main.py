from mymodule import stats_word
from collections import Counter
import json
import os

json_file_path = os.path.join(os.path.dirname(__file__), '1001S02E09.json')
json_file = open(json_file_path)
json_data = json.load(json_file)

text = ""
for poetry in json_data:
    text += poetry['contents']
word_list = stats_word.stats_text_cn(text, 20)
print(word_list)