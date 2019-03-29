
Day 1
2019.3.24

姓名：谢嘉锋
所属班级：003期1班
学习用时：4h +
---------------
收获总结：
早些时候就花时间了解了Github，但是一直没有机会真正用起来，今天进一步认识Github，我还比较暂时肤浅地理解它的工作原理：

1）我们的 program 在一个主要的 branch （默认的 master）上，当我们 create 一个（多个） new branch 的时候，不同branch 是相互独立的，在new branch 上的操作并不会影响到master，这样做的好处是，我们可以在 new branch 是“随意操作”不怕影响到 master，等到最终我们觉得修改比较满意，就把这个 new branch merge 到我们放 program 的 master branch 上；

2）在此之外，GitHub 还有一个极度重要的功能，“存储”，每一次 commit 的时候就好像记录了一个版本，以后任何时候我们都可以回到这个commit 发生的状态。

3）clone 是把一个 repository 上的内容复制到自己的本地电脑，这样我们可以在本地更便利高效的操作；而本地与远端的互动通过 push 与 pull 完成，可以在终端或者 GitHub Desktop 上完成；

4）我自己偶尔在使用的时候，一直觉得 GitHub 的这个“存储功能”特别好，数据放在上面特别安全，不用怕误删或者损坏。
不过今天了解使用了 fork 之后，才发现branch 的牛逼又好玩的地方，我们每个人就像一个 branch, 每个人自顾自地各做各的，结果却是一块完成了一个大program~

--------------------

遇到的难点与问题：
1.issue 还需要花点时间了解；
2.像GitHub  这样，每个 commit 都“长期保存”，直接结果会不会是很大的存储负担？这方面暂时还不太明白。

<hr>

2019.3.25

姓名：谢嘉锋
所属班级：003期1班
学习用时：5h +

收获总结：
这次习题，主要在第二个步骤上花了特别多时间看了好久，一直琢磨不透，究竟要怎么个配置法...... 
后面好像有点明白了，在VS Code 里似乎要特别注意 environment，就是选择一个Interpreter， environment 分为三种：Global , Virtual , conda.

Global, 是，我们跑到哪儿都可以用的，但是如果我们什么都在放到Global的话，就会很混乱，所以就有 Virtual;
Virtual, 范围更小，似乎是局限于特定的文件里面；
而 conda , 是专门配置给 python的 environment 

所以第二个题目是为了让我们通过那个文档理解 VS Code 的environment 
进而所需要的操作，“仅仅是”让我们去选择一个 conda environment，因为所谓的“语法检查、代码提示这些辅助开发功能”都是conda environment 自带的 …… 

<hr>


Day 3
2019.3.26

姓名：谢嘉锋
所属班级：003期1班
学习用时：4h +

收获总结：
因为自己在这之前的几个月一直在学习 JavaScript，这几天接触 Python，理解上没太大障碍，主要是输入上各种不习惯。
两者思路上有很多相同的地方，不过表达上的差异非常大

比如：
1.python 中，似乎不需要先申明再定义，用不着“let”之类，而且 statement 结束也不需要“;”

再比如：
2.string 上的差异：
1）在python 中，通过 index 获取 string 中的 character 的时候，index 超过 string 长度的时候，它会报错，而在 JavaScript 中是得到一个“undefined”的结果；
而且在 python 中，这个 index 可以是负数，即从最右边（第一个是-1）算起；

2）slice 上
JS 是 ".slice(1,2)" 
而 Python 表达一样的意思是[1,2]

......
......
......

今天时间安排不当，来不及进一步学习，只能先完成一个简单版的作业 —— 可满足运算需求，没有报错功能

<hr>

Day 4
2019.3.27

姓名：谢嘉锋
所属班级：003期1班
学习用时：4h +

收获总结：

英文文档看的我一脸懵逼，换到中文版，结果是另一种懵逼……

到底什么是”流程控制“呢？
不知道我的理解对不对
一、
Wiki 上的定义是：
“In computer science, control flow is the order in which individual statements, instructions or function calls of an imperative program are excuted or evaluated.”

我的理解，control flow 是指，在 imperative program 中每个单独的 statement、instructions 或者 function calls（函数调用）被执行被评估的顺序。

二、control flow可以分为四种：
1.按顺序运行不同的statement（不需要条件）；
2.按照条件执行 statement，条件自己定：
“符合什么条件就做什么”，
或者“已经不符合条件就结束手头正在做的 ……”
......
3.暂时插入执行一个写在别的地方的 statement；
4.停止程序

三、另，有没有 control flow 可以用来区别 imperative programming language 和 declarative programming language.

imperative programming 所要实现的是，指导 computer 怎么运作来达到目的，所以它需要一个具体的流程；

而在 declarative programming 中，wiki 中说，它要实现的是：
 “What the program must accomplish in terms of the problem domain”
rather then
“How to accomplish it as a sequence of the program language primitives”

我的理解，它更关注的是，它可以做什么，而不是要如何做。
比如，regular expressions(正则表达式)就是属于 declarative languages 。
所以它不需要 control flow 。



<hr>

