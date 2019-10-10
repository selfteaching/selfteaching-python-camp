import traceback
import requests
from mymodule import stats_word
from pyquery import PyQuery
from wxpy import *


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

def main():
  try:
    bot = Bot()
    my_friend = bot.my_friends()

    @bot.register(my_friend,SHARING)
    def auto_reply(msg):
      response = requests.get(msg.url)
      document = PyQuery(response.text)
      content = document('#js_content').text()
      result = stats_word.stats_text_cn(content,10)
      return result

  except Exception as e:
    logging.exception(e)


if __name__ == '__main__':
#  test_traceback()
#  test_logger()
#  print(stats_word.stats_text(text))
  main()


