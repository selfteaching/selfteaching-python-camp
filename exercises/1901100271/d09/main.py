from mymodule import stats_word
import traceback

with open("C:\\Users\\noodl\\Desktop\\Github\\selfteaching-python-camp\\exercises\\1901100271\\d09\\tang300.json", encoding='UTF-8') as f:
    data = f.read()


# 定义一个含有try，except的函数
def text1_traceback():
    try:
        print(stats_word.stats_text_cn(data, 100))
    except Exception as e:
        print('text1_traceback =>', e)
        print(traceback.format_exc())
# 通过trackback.format.exc()输出字符串格式'''


if __name__ == "__main__":
    text1_traceback()
