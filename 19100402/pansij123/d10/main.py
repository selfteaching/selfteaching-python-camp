from modules.stats_word import stats_text as st
import json
f = open('tang300.json')
t = json.load(f)
f.close()
# format loaded json file as list of dict

# go through entry of list, pick ```'contents'``` per entry like a dict
it=''
for i in t:
	it+=i['contents']

try:
	s = st(it,21)
	print(s[1:21])

except TypeError:
	print("\nFrom main.py:\tInput should be string if you see an error above")
