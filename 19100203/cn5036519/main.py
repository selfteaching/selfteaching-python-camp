from mymodule import stats_word
import json
  
try:
    result = stats_word.stats_text("dfj", 899)
    print(result) 
except ValueError as ve:
    print(type(ve))
    print(ve)
    # print(ve.args)


# day09作业
with open("tang300.json", "r", encoding="utf-8") as file:
    read_data = file.read() 
try:
    result = stats_word.stats_text_cn_v2(read_data, 100)
    print(result)
except ValueError as e:
    print(e)


# day10作业
with open("tang300.json", "r", encoding="utf-8") as file:
    read_data = file.read() 
try:
    result = stats_word.stats_text_cn_v3(read_data, 20)
    print(result)
except ValueError as e:
    print(e)
