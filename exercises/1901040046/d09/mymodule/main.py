from mymodule import stats_word
with open('tang300.json') as tan:
    read_file = tan.read()
tan.closed

try:
    print("字数最频繁前100统计如下："，stats_word.stats_text(read_file,100))
except ValueError as w:
    print(w)