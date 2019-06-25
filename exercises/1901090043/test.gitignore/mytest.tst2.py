def temp_convert(var):
    try:
        return int(var)
    except ValueError,0:
        print("参数没有包含数字\n", 0)

# 调用函数
temp_convert("xyz")