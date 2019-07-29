import stats_word


text1 = 1

while True:
    try:
        stats_word.stats_text(text1)
        break
    except ValueError:
        print("导入字符非法")
        raise
