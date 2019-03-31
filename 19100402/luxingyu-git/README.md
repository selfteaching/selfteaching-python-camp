* D1 遇到的问题：
1. 从创建hello-world和develop分支，到相互commit,pull request以及merge的操作过程没有问题，
但是在查看两者各自的commit目录的时，发现"merge pull request"只会记录from，所以对你来我往次数表示有点混乱。
不过这个纠结的意义不大，知道哪一个branch有更新，之后pull request到另一个branch就行了。

2. 作业完毕后思考对branch的定义理解不透彻，对以master命名的branch我理解为主干部分，其他分支的更新（此处为develop）都应该向master进行pull request，
但作业题中要求从master向develop提交一个pull request，实际应用中是否有必要？我理解为很少会在主干branch上直接做修改吧。同样这个问题也仅限于时候想想，意义不大。。

3. 关于fork和clone，在进行第5部分作业的时候，等到本地文件夹包括README.md和d1_exercise_helloworld.txt文件都建立完毕后，从Github桌面版向作业库进行posh的时候告知权限问题。
才发现fork完原始作业库后，竟然clone的不是fork库。其实这个问题本应该在第4题中就会遇到，但是那个时候顺利进行没有在意这个问题，也许本来就错了，只是hello-world的原始库就是自己建的所以没有提示权限问题。

4. fork后的库之后不等于和原始库同步，这个问题是在查找班级目录时遇到，原因是fork在于源库中班级目录的建立。
