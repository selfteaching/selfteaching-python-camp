from stats_word import stats_text

print("统计结果如上所示：")
while True:
    try:
        x = input("Please enter a text: ")
        stats_text(x)
        break
    except ValueError:
        print("Error:参数不正确，请重新输入文本")

