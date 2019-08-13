from mymodule import stats_word

with open('tang300.json') as f:
    read_date = f.read()
    print(stats_word.stats_text(read_date))





