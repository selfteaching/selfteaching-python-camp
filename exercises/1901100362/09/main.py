from mymodule import stats_word
import traceback
import logging
import json
import os

def test_traceback():
  try:
    stats_word.stats_text(text)
  except Exception as e:
    print("trace_back==>",e)
    print(traceback.format_exc())
def test_logger():
  try:
    stats_word.stats_text(text)
  except Exception as e:
    logging.exception(e)


if __name__ == '__main__':
#  test_traceback()
#  test_logger()
#  print(stats_word.stats_text(text))
  filename = 'tang300.json'
  filedir = os.path.dirname(os.path.realpath(__file__))
  with open(filedir+'/'+filename) as f:
    f1 = f.read()
    print(stats_word.stats_text_cn(f1,100))