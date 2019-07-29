import stats_word
import json
with open(r'''C:\\Users\Administrator\Desktop\作业\d09\mymodule\tang300.json''','r+',encoding="utf-8") as f:
    string1 = f.read()

try:
    print('前20的中文词频统计结果：',stats_word.stats_text_ch(text)) 
except:
    print(" that is not a string.")
