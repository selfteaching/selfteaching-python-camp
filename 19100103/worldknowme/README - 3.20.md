今天主要掌握：
1、a=float(input('请输入第一个数字:'))，可以利用给input定义赋值且，来让程序识别输入的东西。
2、利用def ---（）定义一个函数/程序，注意：定义完以后，需要运行程序，所以要调用函数---（）

另外今天看了写东西，随笔集一下：
1、在用键盘输入python代码时，尤其是需要输入！@#￥%……&*等需要按住shift+1234567来输入特殊字符的时候，由于是win10系统，很容易将输入法切换成中文输入法，此时就会出现键盘输入失效。所以，要时刻关注输入法状态，避免中文输入法的出现（也可以在Windows系统中设置切换输入法的方式）
2、在vscode中，可以在vscode的TERMINAL中直接运行python，方法如下：在TERMINAL中直接输入python，然后回车，就会出现“>>>”的字符，这样，就可以在terminal输入相关语句来直接执行python命令了，例如直接可以输入2+3，然后回车，就可以得到5。（注：启动vscode后，必须先调用python interpreter：用CTRL+shift+p直接输入，查找python interpreter即可调用）
3、terminal中的Python 用 “enter”来换行，同事enter键也作为enter键来输出结果：
例如输入：
>>> tax=125/100
>>> price=100.50
>>> price*tax
125.625
4、Python 也可以操作字符串（可以使用单引号（'……'），双引号（"……"）都可以。）反斜杠 \ 可以用来转义，例如我像输入'同时担心它被识别成字符串的输入作用，就可以用\'来代表示’
>>> 'doesn\'t'
"doesn't"
5、=是赋值，==才是等于号；.format可以用来格式化字符串：
"{0} be nimble, {0} be quick, {0} jump over the {1}".format("Jack", "candle stick")
# => "Jack be nimble, Jack be quick, Jack jump over the candle stick"
6、
# None，0，空字符串，空列表，空字典都算是False
# 所有其他值都是True
bool(0)  # => False
bool("")  # => False
bool([]) # => False  #序列
bool({}) # => False
7# 用append在列表最后追加元素；# 用pop从列表尾部删除；li[1:]取第1个数字之后的数字；li[:3]取第3个数字之前的数字；del li[2]删除列表/元组中的第二个元素；in判断是否包含；
li.append(1)    # li现在是[1]
li.append(2)    # li现在是[1, 2]
li.append(4)    # li现在是[1, 2, 4]
li.pop()            # li现在是[1, 2]
li[-1]                # => 4   # 取出最后一个元素（倒数第一个元素）
8、# 字典赋值
filled_dict.update({"four":4})
# 用字典表达映射关系
empty_dict = {}
# 初始化的字典
filled_dict = {"one": 1, "two": 2, "three": 3}
9、if语句：if，elif，else

10、自己写的第一个程序：
def jisuanqi():
 print("请您依次输入两个数字，你将得到这两个数字的基本的加减乘除运算的结果")
 a=float(input('请输入第一个数字'))
 b=float(input('请输入第二个数字'))
 print('请通过输入1，2，3，4进行您想要的运算：1、加法  2、减法  3、乘法  4、除法')
 x=int(input('请输入第二个数字'))
 c=a+b
 d=a-b
 e=a*b
 f=a/b
 if x==1:
     print("您的运算结果为",c)
 elif x==2:
     print("您的运算结果为",d)
 elif x==3:
     print("您的运算结果为",e)
 elif x==4:
     print("您的运算结果为",f)
 else:
     print("出错")




 print("另外还可以告诉您：第一个数加上第二个数等于:", c )
 print("另外还可以告诉您：第一个数减去第二个数等于:", d ) 
 print("另外还可以告诉您：第一个数乘以第二个数等于:", e )
 print("另外还可以告诉您：第一个数除以第二个数等于:", f )
jisuanqi()


