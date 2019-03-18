DAY01
所属班级：001期03班

学习用时：1h30min

收获总结：
1.虽然第一次创建的分支名称为master，但其实无论哪个分支都能成为主分支。可以把master分支的commit合并到develop分支上。

遇到的难点与问题（是否解决）：

1.问题：创建空的helloworld的仓库后，无法先创建分支develop再创建develop.txt。
1.解决：删掉helloworld仓库，重新创建一个有README.md文件的仓库，就可以先创建分支develop再创建develop.txt了。

2.问题：SourceTree的教程是英文的，问题不大，但客户端竟然是中文的，界面也变了，找不到按钮了，不知道拉取/推送哪个对应pull request，不知道合并按钮是merge呢还是干嘛的。在选项中并没有找到语言选项。
2.解决：搜索引擎找到选项中语言选项的位置，之前设置的是“自动”所以一直找“中文”没找到，现在设置为English就行了。

3.问题：第一次用SourceTree客户端Clone仓库到本地，选择了users/Administrator作为目录，没想到没有新建文件夹，直接使用Administrator作为文件目录，该目录下还安装了其他软件，导致大量文件被检索进Unstaged files，电脑卡顿到无法操作。
3.解决：在钉钉群里问教练，关掉软件之后删除.git目录就好了。下一次再Clone仓库的时候记得新建文件夹。