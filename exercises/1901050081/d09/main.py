from mymodule import stats_word

import json
with open('/Users/queenieq/Documents/GitHub/selfteaching-python-camp/exercises/1901050081/d09/tang300.json','r',encoding='utf-8') as f:
    data=json.load(f)
    data_words=str(data)
    result=stats_word.stats_text_cn(data_words)
print(result)