# # 储存档案
# file=open ("data.txe",mode="w",encoding="utf-8") # 开启
# file.write("Hello File\n python") # 操作
# file.close() #关闭
with open("data.txt",mode="w",encoding="utf-8") as file:
    file.write("5\n3")
# 读取档案
# 把档案中的数字资料，一行一行的读取出来，并计算综合
sum=0

with open("data.txt",mode="r",encoding="utf-8") as file:
    for line in file: # 一行一行的读取
        sum+=int(line)
    print(sum)

