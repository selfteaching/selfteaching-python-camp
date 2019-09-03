import stats_word


with open('f:/zixuepython/selfteaching-python-camp/exercises/1901050060/d10/mymodule/tang300.json','r',encoding='UTF-8') as f:
    text = f.read()
f.close()

try:
    print(stats_word.stast_text_cn(text,20))
except ValueError as w:
    print(w)