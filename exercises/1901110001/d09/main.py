from mymodule import stats_word
import traceback
import logging
from os import path
import re
import json

logging.basicConfig(format="file:%(filename)s|line:%(lineno)d|message:%(message)s",level=logging.DEBUG)

def test1():
    file_path = path.join(path.dirname(path.abspath(__file__)), "tang300.json")
    with open(file_path,"r", encoding="utf-8") as f:
        return f.read()

def test2(x):
    y = ""
    for item in x:
        y += item.get("contents","")
    return y

def test3():
    try:
        x = test1()
        logging.info(x[0])
        y = test2(json.loads(x))
        logging.info("result => %s", stats_word.stats_text_cn(y,100))
    except Exception as e:
        logging.exception(e)

if __name__ == "__main__":
    test3()