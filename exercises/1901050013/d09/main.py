from mymodule.stats_word import stats_text_cn
with open(r"c:/Users/Administrator.SKY-20160827RZT/Desktop/自学编程/selfteaching-python-camp/exercises/1901050013/d09/tang300.json", encoding='UTF-8') as f:
    text = f.read()  
try:
    stats_text_cn(text)
    print(stats_text_cn(text))
except ValueError:
    print("The text is not a string. Please input a string.")
