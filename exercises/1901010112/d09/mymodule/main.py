import stats_word
import json

with open(r'G:\GitHub\selfteaching-python-camp\exercises\1901010112\d09\mymodule\tang300.json', 'rb') as f:
    text_new = f.read()
    text_new_str = text_new.decode(encoding='utf-8')
    print(type(text_new_str))
    try:
        print(stats_word.stats_text_cn(text_new_str))
    except ValueError:
        print('Oops!  That was no str text.  Pls try again...') 