#!/usr/bin/python3
# Filename: main.py
import stats_word
import json
with open(r'''C:\Users\ZGY\Documents\GitHub\selfteaching-python-camp\19100402\zhengguanya\d09\mymodule\tang300.json''','r+',encoding="utf-8") as f:
    string1 = f.read()

try:
    stats = stats_word.stats_text_cn(string1)
except ValueError:
    print("ValueError: You have an input that is not a string.")
else:
    print(stats)


