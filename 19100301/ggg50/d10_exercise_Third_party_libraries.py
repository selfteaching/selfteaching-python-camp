from mymodule import stats_word_day10
from os import path
import json

# use os module to get path of tang300.json
path_file = path.join(path.dirname(path.realpath(__file__)), "tang300.json")

with open(path_file, "r", encoding='utf-8') as f:
    tang_object = json.load(f)

text_tang = ""

for tang in tang_object:
    if "contents" in tang:
        text_tang = text_tang + tang["contents"]

# input text and define output word numbers
stats_word_day10.stats_text_cn(text_tang, 20)


