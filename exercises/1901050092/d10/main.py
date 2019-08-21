from mymodule import stats_word
from os import path

def load_file():

    file_path = path.join(path.dirname(path.abspath(__file__)), 'tang300.json')

    print('当前文件路径：', __file__, '\n读取文件路径：', file_path)

    with open(file_path, 'r', encoding='utf-8') as f:

        return f.read()

text = load_file()
result = stats_word.stats_text_cn(text,10)
print(result)