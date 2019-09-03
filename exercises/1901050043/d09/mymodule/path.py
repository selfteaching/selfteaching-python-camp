from os import path
import json
def load_file():
    file_path =path.join(path.dirname(path.abspath(__file__)),'tang300.json')
    print('当前文件路径：', __file__, '\n读取文件路径：', file_path)