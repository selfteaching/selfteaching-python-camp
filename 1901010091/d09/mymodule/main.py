import json
file_path='/Users/YY/Documents/GitHub/selfteaching-python-camp/1901010091/d09/mymodule/tang300.json'
with open(file_path) as f:
    js=json.load(f)
tt=[str(i) for i in js]
text=''.join(tt)
    
count=100

import stats_word
try:
    stats_word.stats_text(text,count)
except ValueError:
    print("文本为非字符串")


