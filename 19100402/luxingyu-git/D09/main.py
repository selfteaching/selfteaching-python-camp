from mymodule import stats_word
import json
with open(r'D:\\githubcloneproject\\selfteaching-python-camp\\19100402\\luxingyu-git\D09\\tang300.json','r+',encoding="utf-8") as f:
    text = f.read()
try:
    stats_word.stats_text(text)
except:
    print('ERROR：text类型错误，请输入字符串文本。')