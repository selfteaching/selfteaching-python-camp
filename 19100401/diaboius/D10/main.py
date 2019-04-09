from mymodule import stats_word as mk
with open('tang300.json',encoding='UTF-8') as text:
    read_file = text.read()
try:#通过try...except捕获异常
    print("唐诗中使用词频最高的20个词：")
    print(mk.stats_text_ch(read_file,20))
except ValueError as e:
    print(e)


