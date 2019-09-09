from mymodule.stats_word import stats_text_cn
import json
with open("tang300.json","r",encoding="utf-8") as file:
    data = str(json.load(file))
print(stats_text_cn(data,100))