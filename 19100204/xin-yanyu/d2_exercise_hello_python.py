#  第一个Python程序
# 自学的第一步
# 第二天的作业
# 向老师、同学问好
# 用列表、遍历打印Python之禅
# 2019.3.22
# --------------
# word变量，问候语
word = "hello world "
# 首字母大写
print(word.title())

# ————以下为Python之禅

print("\n====================")

# import_this为列表
import_this = [">>> import this"]

# 在列表中添加新内容
import_this.append("The Zen of Python, by Tim Peters")
import_this.append("             ")
import_this.append("Beautiful is better than ugly.")
import_this.append("Explicit is better than implicit.")
import_this.append("Simple is better than complex.")
import_this.append("Complex is better than complicated.")
import_this.append("Flat is better than nested.")
import_this.append("Sparse is better than dense.")
import_this.append("Readability counts.")
import_this.append("Special cases aren't special enough to break the rules.")
import_this.append("Although practicality beats purity.")
import_this.append("Errors should never pass silently.")
import_this.append("Unless explicitly silenced.")
import_this.append("In the face of ambiguity, refuse the temptation to guess.")
import_this.append("There should be one-- and preferably only one --obvious way to do it.")
import_this.append("Although that way may not be obvious at first unless you're Dutch.")
import_this.append("Now is better than never.")
import_this.append("Although never is often better than *right* now.")
import_this.append("If the implementation is hard to explain, it's a bad idea.")
import_this.append("If the implementation is easy to explain, it may be a good idea.")
import_this.append("Namespaces are one honking great idea -- let's do more of those!")

# 遍历列表打印
for  the_python in import_this:
  print(the_python)
