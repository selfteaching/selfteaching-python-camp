from mymodule import stats_word


sample_text =11111

try:
    result = stats_word.stats_text(sample_text)
except TypeError:
        print("输入的参数类型不对，请输入字符串。")
except AttributeError:
    print("切片语法错误")


