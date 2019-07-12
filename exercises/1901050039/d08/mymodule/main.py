#调用模块
import stats_word

#输入测试文本
text = 3.14

#参数类型检查
try:
    a = stats_word.stats_text(text)
    print(a)
except ValueError:
    print('Error:参数格式不对，请更换为文本')