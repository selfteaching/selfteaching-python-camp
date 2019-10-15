# helloworld
#Day2 配置本地运⾏行行开发环境
Ieam 1
 中英文字符的转换，中文字符会报错
#<<<<<<< master
#Day 3 Hello Python 计算器学习
Item 1 变量命名规则
    1.1 在使用标识符时，需要注意如下规则：
    标识符可以由字母、数字、下画线（_）组成，其中数字不能打头。
    标识符不能是 Python 关键字，但可以包含关键字。
    标识符不能包含空格。

    例如下面变量，有些是合法的，有些是不合法的：
    abc_xyz：合法。
    HelloWorld：合法。
    abc：合法。
    xyz#abc：不合法，标识符中不允许出现“#”号。
    abc1：合法。
    1abc：不合法，标识符不允许数字开头。
Item 2 else 语句
    2.1 每个else语句结束之后需要有：来结束，标准的语句
Item 3 字符串转换成数字
     3.1 输入的为字符串，进行运算需要转换成数字
#Day 4 控制流程
 基本没有看实例代码自己实现了下 
Item 1 break用法
 break 用于完全结束一个循环，跳出循环体。
 
 1.1 while True:

    break
 当循环条件为真时，那么就停止，所以这个指令不返回任何东西。
 1.2 
 num = 0

 while num <= 10:

    if num == 5:

        break

    else:

        print(num)

        num += 1

 在if条件里面，当达到某个条件的时候，就进行停止。

Item 2  程序的逻辑性
  2.1 循环嵌套
   有循环嵌套，例如while ，for 才会进行循环的执行
   同时对于作用的范围非常重要，很强调逻辑性

Item 3 Print
 3.1  print（）#换行
 3.2  print（end="\t"）Tab 键作用

#Day 5 数据容器

Item1
 1.1 lambda 函数用用法：https://www.cnblogs.com/kaishirenshi/p/8611358.
Iteam 2 数据不同的用处
  list-列表[]
  dict-字典，表示映射关系{}
  set- 集合类型，同时剔除重复元素
感受：
    1.代码的逻辑性很关键
    2.多看官网文档
    3.先模仿着写也是可以的
    4.搞清楚不同数据容器用法不同。
   