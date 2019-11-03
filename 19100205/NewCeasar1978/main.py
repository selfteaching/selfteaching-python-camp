
with open('tang300.json',encoding = 'UTF-8') as f:
    text = f.read()
import mymodule.stats_word
mymodule.stats_word.stats_text_1(text)