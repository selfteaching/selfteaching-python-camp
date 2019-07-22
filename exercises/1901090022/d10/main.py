from mymodule import stats_word
from collections import Counter
import json
import os

json_dir = os.path.dirname(__file__)
json_file_path = os.path.join(json_dir, '1001S02E09.json')
json_file = open(json_file_path)
jason_data = json.load(json_file)

text = ""
for poetry in jason_data:
    text += poetry['contents']
word_list = stats_word.stats_text_cn(text, 20)
print(word_list)