
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
