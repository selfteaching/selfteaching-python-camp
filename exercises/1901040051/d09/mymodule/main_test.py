import json
import sys
sys.path.append("c:")
import stats_word

  

# try:

#     result = stats_word.stats_text(text)

#     print(result) 

# except ValueError as ve:

#     print(type(ve))

#     print(ve)

with open("mymodule/tang300.json", "r", encoding="utf-8") as file:

    read_data = file.read() 

try:

    result = stats_word.stats_text_cn(read_data)

    print(result)

except ValueError as e:

    print(e)