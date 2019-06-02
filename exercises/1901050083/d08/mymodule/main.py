import stats_word

text=123

try:
    print(stats_word.stats_text(text))
except ValueError as fnf_error:
        print(fnf_error)
