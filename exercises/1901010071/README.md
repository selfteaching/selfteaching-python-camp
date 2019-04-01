## DAY1
今天进行了自学营的第一次训练，本来以为自己已经早就熟练掌握了github的创建仓库，提交更改之类的，但是今天发现自己仍然只是知道一部分。参加自学营前参加了刘娟娟的"you can you up,no bb"以为自己闯过了第一关，守关人跟我说你并没通过的时候，我理直气壮的跟他说，我完成了呀。守关人并没有说什么，让我去了第二关，今天才知道我真的是没有通过，人家一看截图，没有分支，没有commit，真是懒得理我。学习真的是切记骄傲啊。

## DAY2
今天在运行hello world程序的时候踩了个莫名其妙的坑，那就是输入print函数括号里面的点符号踩的坑。我开始输入的是esc下面那个`，因为为看着别人好像也是输入的这个，然后程序一直报错，我快疯了，后面换了"才没有报错，最后我才发现是这个'（“不用shift的')。

#### 建立hello_world.py文件的方法有三种：

1.在vscode中可以直接通过点击建立。

2.通过终端建立，在cd 文件夹后，输入
```
touch hello_world.py
````
这个方法在windows中会报告错误，没找到解决方案，我是在电脑上用virtualbox安装了ubuntu系统然后在Ubuntu系统中的终端上实现的。

3.直接在jupyterlab中建立一个hello_world.ipyb文件。

#### 执行hello_world.py的方法有三种：

1.打开终端，cd打开hello_world.py程序所在的文件夹,执行
```
python hello_world.py
```
可以看到输出结果

2.在vscode中右键单击hello_world.py再点击在终端中运行也可以看到输出结果

3.在jupyterlab中直接shift+enter，也可以直接看到输出结果。

## Day3

今天的课程是要编写一个计算器，如果说前两天是带你认识工具的话，今天直接就要你用工具做出一个产品来了。画风不对呀，虽然有说明书，但怎么感觉中间少了n个要学的东西，懵了。

还好我们有“老师”--“谷歌，必应”，大作业仓库，厚着脸皮先看看尖子生是怎么写的，再把别人的计算器“拆了”，自己组装一下。

看了下别人的程序实现，有超级复杂的，调用了tkinter模块，直接输出了一个计算机可视化界面，跟win上的类似；也有超级简单的，只调用了int(),input(),print()函数利用if语句就实现了；也有隔壁的尖子生，直接定义函数实现的。

我照着最简单的方法敲了个最简单的计算器，不仅有“加、减、乘、除法”，我自己加上了“幂、余”都能实现，然后我发现原代码不支持小数计算，翻看了一下函数那章，换了个float()浮点数函数就可以实现小数运算了，代码如下：
```
# float()支持小数运算
# 如果用int()函数的话就只支持输入整数
# input()接收键盘输入

a=float(input('请输入数值1'))  
b=input('请输入运算符号')
c=float(input('请输入数值2'))
if b=="+":
    print(a+c)
elif b=="-":
    print(a-c)
elif b=="*":
    print(a*c)
elif b=="/":
    print(a/c)
elif b=="**":
    print(a**c)
elif b=="%":
    print(a%c)
```

然后我试了试第二种方法，也是可以用的：
```
choice = float(input('请选择运算： \n1.加\n2.减\n3.乘\n4.除\n5.幂\n6.余\n请选择你的算法： '))
num1 = float(input('请输入第一个数： '))
num2 = float(input('请输入第二个数： '))
if choice == 1:
    print('{} + {} = {}'.format(num1, num2 ,num1+num2))
elif choice == 2:
    print('{} - {} = {}'.format(num1, num2 ,num1-num2))
elif choice == 3:
    print('{} *{} = {}'.format(num1, num2 ,num1*num2))
elif choice == 4:
    print('{} / {} = {}'.format(num1, num2 ,num1/num2))
elif choice == 5:
    print('{} ** {} = {}'.format(num1, num2 ,num1**num2))
elif choice == 6:
    print('{} % {} = {}'.format(num1, num2 ,num1%num2))
```
以用带练，多学多用！