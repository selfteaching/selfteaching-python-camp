from mymodule.stats_word import stats_text_cn
import json
with open("tang300.json","r",encoding="utf-8") as f:
    data=str(json.load(f))
    x=100
print(stats_text_cn(data,x))