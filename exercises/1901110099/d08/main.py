from mymodule import stats_word
import traceback
import logging

logger = logging.getLogger(__name__)

def text_traceback():
    try:
        stats_word.stats_text(1)
    except Exception as e:
        print('text_traceback =>',e)
        print(traceback.format_exc())


def text_logger():
    try:
        stats_word.stats_text(1)
    except Exception as e:
        print('text_logger =>',e)
        logger.exception(e)


if __name__ == "__main__":
    stats_word.stats_text(1)
    text_traceback()
    text_logger()