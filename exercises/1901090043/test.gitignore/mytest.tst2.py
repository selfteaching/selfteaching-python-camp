def input_password():
    # 提示用户输入密码
    pwd = input("请输入密码：")
    # 判读密码长度大于等于8，返回用户输入的密码
    if len(pwd) >= 8:
        return pwd
    # 如果小于8，则抛出异常
    print("主动抛出异常")
    # 创建异常对象
    ex = Exception("密码长度不够")
    # 抛出异常对象
    raise ex
# 提示用户输入密码
try:
    print(input_password())
except Exception as result:
    print(result)
