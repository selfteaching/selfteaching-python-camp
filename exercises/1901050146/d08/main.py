from mymodule import stats_word
import traceback

def text_traceback():
    try:
        stats_word.stats_text_en(1)
    except Exception as e:
        print("text_traceback:",e)
        print(traceback.format_exc())

if __name__ == "__main__":
    stats_word.stats_text_en(1)
    text_traceback()