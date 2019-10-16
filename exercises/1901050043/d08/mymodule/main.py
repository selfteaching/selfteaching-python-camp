import stats_word
text=123456
result=stats_word.stats_text(text)
print(result)
import stats_word
try:
    print(stats_word.stats_text(text))
except ValueError as error:
    print(error)





