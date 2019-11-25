import stats_word

with open('D:\\文档\\Pythonlernen-ss01\\selfteaching-python-camp\\exercises\\1901050193\\d09\\mymodule\\tang300.json',mode='r', encoding='UTF-8') as f:
    text = f.read()

try:
    stats_word.stats_text(text,100)
except ValueError:
    print('非字符串，请重新输入')