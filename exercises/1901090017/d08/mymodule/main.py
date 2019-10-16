import stats_word
import traceback

def test_traceback():
    try:
        stats_word.stats_text(kkk)
    except Exception as e:
        print('test_trackback =>',e)
        print(traceback.format_exc())

# def test_logger():
    # try:
        # stats_word.stats_text(1)
    # except Exception as e:
        # print('test_logger =>', e)
        # logger.exception(e)

if __name__ == "__main__":
    test_traceback()