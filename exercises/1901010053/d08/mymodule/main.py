
import stats_word
text3=234
#stats_word.stats_text_cn(text3)   #验证参数检查功能是否生效

try:
   stats_word.stats_text_cn(text3)
except ValueError:
   print("Error:文本为非字符串")
