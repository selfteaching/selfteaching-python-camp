from mymodule import stats_word

import traceback   #引入trackback模块

text = 1, 2, 3
'''try:
    stats_word.stats_text(text)
except ValueError:
    print("错误：文本为非字符串格式")'''


def text1_traceback():   #定义一个含有try，except的函数
    try:
        stats_word.stats_text(text)
    except Exception as e:
        print('text1_traceback =>', e)
        print(traceback.format_exc())   #通过trackback.format.exc()输出字符串格式


if __name__ == "__main__":
    text1_traceback()

