from mymodule import stats_word
from os import path
import json
import logging
logging.basicConfig(
    format='file:%(filename)s|line:%(lineno)d|message:%(message)s',level=logging.DEBUG
)
# 读取文件内容
def load_file():
    # 获取文件路径
    # print(path.abspath(__file__))
    # print(path.dirname(path.abspath(__file__)))
    file_path = path.join(path.dirname(path.abspath(__file__)),'tang300.json')
    # file_path = path.join(path.dirname(path.abspath(__file__)),'./tang300.json') 
    with open(file_path,'r',encoding='utf-8') as f:
        return f.read()
    f.close()
# 从json文件中获取contents值
def merge_poems(data):
    poems=''
    for item in data:
        poems += item.get('contents','')
    return poems
def main():
    try:
        data = load_file()
        logging.info(data[0])
        poems = merge_poems(json.loads(data))
        logging.info('统计结果：：%s',stats_word.stats_text_cn(poems,20))
        # print(stats_word.stats_text_cn(poems,20))
    except Exception as e:
        logging.exception(e)

if __name__ == '__main__':
    main()

