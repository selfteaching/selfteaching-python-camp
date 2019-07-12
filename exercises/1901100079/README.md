# Day1
Github涉及repositories，branches，commits，和pull requests。
一个项目下面可以有多个repositories，每个repositories里面有多个branches。
一个repository默认一个branch——master branch，我们可以在branch这一栏新建第二个branch，新建的2号与主branch完全相同，是平行关系。
此时，在master branch里做的任何修改不会进入2号branch，同理2号branch中的修改也不会进入master。
除非，用pull request将一个branch compare 另一个branch并且merge，这样两个branch的修改或者内容就又完全一致了。
有意思的是，虽然merge了，但是仍可以在每个branch独立更改而不影响被merge into的那个branch。
在本地修改了内容，在GitHub的desktop上相应repository里会显示需要commit修改后的文件，然后要push origin去到网页中。最后仍然需要pull request让相应repository的管理者merge into。
为什么每次pull request都要有一个名字框，既然是compare两个branch而非文件，但是名字框必填一个文件名？这个名字只是compare时注此次行为的一个主题或关键词用的，我认为。

# Day2
今天发现fork的repository并不能与主库实时更新，因此fork只是为了让自己能够对主库进行commit，pull requests，然后贡献绵薄之力的。如果要实时同步，要写代码。
Anaconda很强大，我喜欢它的Anaconda Prompt。在AP中写入python并回车，可以进入python编程模式，通过同时按Ctrl+Z+回车，退出编程模式。还可以直接键入spyder或者jupyter-notebook按回车打开相应程序。
Anaconda里Spyder和Jupyter-Notebook均可以直接编程，界面比VScode美丽简洁。
VScode的配置有些麻烦，先选择interpreter，然后就可以相应变成了。很有意思的是，如果在Anaconda外启动VScode，会报错，主要是conda的环境问题。
我通过先在Windows系统下将运行环境增加了三个路径，分别是Anaconda3、Anaconda3\scripts、Anaconda3\libary\bin。还是报错后，又用Ctrl+，打开设置，搜索terminal，在左下方python里去除activate……的勾选。
说明Anaconda内部提供了跟Windows不一样的运行环境，目前是什么，我不懂，希望以后能知道。
代码print("hello world!") print是一个动作，小括号里是执行该动作的具体内容，用“”应该是为了表明引号内是文字，以文字形式输出。
Jypyterlab也是一个可以编程的网页式的程序，没找到应该怎么进行路径设置，打算再查一下。可以通过拖拽电脑上的文件进入该lab的左侧栏，但是不能是文件夹或压缩包。

# Day3
再次阅读环境相关教程，我理解的是刚安装的VScode是在默认的global这个环境中运行了，长时间，容易堆积很多clusters，影响电脑工作效率，因此要选择一个虚拟或conda环境以便区室化。conda比virtual好在任何电脑上任何conda环境下一个project的不同部分可以选择同类conda环境运行。
我Day2的出错问题要么是终端运行自选环境导致的，要么是在integrated终端不会自动激活环境导致。
默认设置环境，要在Preference: Open User Settings里设。每次打开VScode要重选一次conda环境，可能因为没设为默认。
计算机只会干我们明确说明的事，所以格式很重要，字符、数字、变量要能够区分。
编程无非事拆解一个事情的步骤，分步编程，然后用一些逻辑运算将各部分联系。
一个复杂的计算器设计思路：（1）依据计算的优先级，先剥离括号，即找出最里面的括号，先进行计算；（2）在剥离的第一个括号内先区分乘除并运算，再加减，这样得到的值取代这个括号；（3）依次剥离依次运算。这个过程中需要计算器通过切片方式找最内括号（左括号有多少个之后遇到第一个右括号），用正则表达式把运算符和数字分开，每一镉括号的运算都是一次循环（需要考虑第二次循环可能出现的变化，如++ --因去除括号而在一起的情况）等。
多手打熟悉编程语言，往往出错在于格式不规范。
