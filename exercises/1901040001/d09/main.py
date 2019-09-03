#从mymodule文件夹中调用stats_word.py
from mymodule import stats_word
import json
if __name__ == "__main__":
    with open(r'C:\Users\xiacongcong\Documents\GitHub\selfteaching-python-camp\exercises\1901040001\d09\tang300.json', 'rb') as f:
        text = f.read()
    text = text.decode(encoding='utf-8')
    try:
        stats_word.stats_text(text)
    except ValueError:
        print('The input is a non-string, please enter a string.')
