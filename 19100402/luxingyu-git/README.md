* D1 遇到的问题：

1. 从创建hello-world和develop分支，到相互commit,pull request以及merge的操作过程没有问题，
但是在查看两者各自的commit目录的时，发现"merge pull request"只会记录from，所以对你来我往次数表示有点混乱。
不过这个纠结的意义不大，知道哪一个branch有更新，之后pull request到另一个branch就行了。

2. 作业完毕后思考对branch的定义理解不透彻，对以master命名的branch我理解为主干部分，其他分支的更新（此处为develop）都应该向master进行pull request，
但作业题中要求从master向develop提交一个pull request，实际应用中是否有必要？我理解为很少会在主干branch上直接做修改吧。同样这个问题也仅限于时候想想，意义不大。。

3. 关于fork和clone，在进行第5部分作业的时候，等到本地文件夹包括README.md和d1_exercise_helloworld.txt文件都建立完毕后，从Github桌面版向作业库进行posh的时候告知权限问题。
才发现fork完原始作业库后，竟然clone的不是fork库。其实这个问题本应该在第4题中就会遇到，但是那个时候顺利进行没有在意这个问题，也许本来就错了，只是hello-world的原始库就是自己建的所以没有提示权限问题。

4. fork后的库之后不等于和原始库同步，这个问题是在查找班级目录时遇到，原因是fork动作早于源库中班级目录的建立。

---

* D2 学习小结：

1. Anaconda软件的安装是之前就根据笑来老师《自学是门手艺》上的关于*Jupyterlab 的安装与配置*一文顺利完成。
2. 但是在配置VSCOde环境时，无法搜索到官方教程中*Python: Select Interpreter*，这步花了时间最长，最后在issues中查到了问题，搜索**Python:选择解释器**终于找到了，而后又在issues中看到有之前同学讨论这个问题，并按照他们的心得修改了VSCOde中language设置，并重新搜索*Python: Select Interpreter*，统一。
3. 试图用jupyter Lab阅读《自学是门手艺》时，发现Flie路径是定死在C盘，但是自己clone本书的路径在D盘，后搜索issues #106,顺便学到了用cmd修改原始路径的方法（cd /d ~）。
4. 阅读《自学是门手艺》过程中，在*my-notes*文件夹中看到名为**Github进行fork后如何与原仓库同步**markdown文本（C.），从而习得第三种应对源库和fork库更新不同步的方法，另外两种分别是**A.删除fork库重新fork**；**B.在Github中用源库向自己fork库pull request并merge**，个人感觉方法A是万不得已采用，方法B最为方便，而方法C操作过程应该算方法B的cmd代码版本：），顺便接触了下git软件。
5. 当你看到“以下是傻瓜版操作步骤，还细心配了截图，保管你从 0 也能上手”这句话但还是不知道错在那里的时候，经过5,6遍**反复阅读**后终于搞定了。所以最大的收获是践行反复阅读并收获小成功。
