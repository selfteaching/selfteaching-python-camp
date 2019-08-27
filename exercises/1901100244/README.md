# Python 自学训练营 010 期 沈璜 日志

**学员信息**

- 姓名：沈璜
- 学号：1901100244
- 系统：Windows 10 version 1903 (64-bit)
- 职业：新闻学在读硕士研究生
- 简介：以前当过 10 年高中教师，因为觉得已经遇到了职业天花板，就参加了国家统招硕士研究生考试，读了全日制的硕士研究生，还有 1 年毕业，现在正在硕士论文写作阶段。关注笑来老师十多年了，对老师思考后的结论深表认同，故而借这个机会学习一下 Python。希望学完之后应用在论文写作等场景里。

**目录**

- [Python 自学训练营 010 期 沈璜 日志](#python-%e8%87%aa%e5%ad%a6%e8%ae%ad%e7%bb%83%e8%90%a5-010-%e6%9c%9f-%e6%b2%88%e7%92%9c-%e6%97%a5%e5%bf%97)
  - [DAY 00](#day-00)
    - [1. 学习内容](#1-%e5%ad%a6%e4%b9%a0%e5%86%85%e5%ae%b9)
    - [2. 学习用时](#2-%e5%ad%a6%e4%b9%a0%e7%94%a8%e6%97%b6)
    - [3. 收获总结](#3-%e6%94%b6%e8%8e%b7%e6%80%bb%e7%bb%93)
    - [4. 遇到的难点与问题](#4-%e9%81%87%e5%88%b0%e7%9a%84%e9%9a%be%e7%82%b9%e4%b8%8e%e9%97%ae%e9%a2%98)
      - [4.1 网络环境](#41-%e7%bd%91%e7%bb%9c%e7%8e%af%e5%a2%83)
      - [4.2 手册话语](#42-%e6%89%8b%e5%86%8c%e8%af%9d%e8%af%ad)
      - [总结](#%e6%80%bb%e7%bb%93)
  - [DAY 01](#day-01)
    - [1. 学习内容](#1-%e5%ad%a6%e4%b9%a0%e5%86%85%e5%ae%b9-1)
    - [2. 学习用时](#2-%e5%ad%a6%e4%b9%a0%e7%94%a8%e6%97%b6-1)
    - [3. 收获总结](#3-%e6%94%b6%e8%8e%b7%e6%80%bb%e7%bb%93-1)
    - [4. 遇到的难点与问题](#4-%e9%81%87%e5%88%b0%e7%9a%84%e9%9a%be%e7%82%b9%e4%b8%8e%e9%97%ae%e9%a2%98-1)
      - [4.1 “任务2.3 在 develop 分支中创建一个名为 develop.txt 的文件，提交一个 commit”](#41-%e4%bb%bb%e5%8a%a123-%e5%9c%a8-develop-%e5%88%86%e6%94%af%e4%b8%ad%e5%88%9b%e5%bb%ba%e4%b8%80%e4%b8%aa%e5%90%8d%e4%b8%ba-developtxt-%e7%9a%84%e6%96%87%e4%bb%b6%e6%8f%90%e4%ba%a4%e4%b8%80%e4%b8%aa-commit)
      - [4.2 “任务2.4 从 develop 提交一个 Pull Request 到 master 分支，并将其合并(merge)”](#42-%e4%bb%bb%e5%8a%a124-%e4%bb%8e-develop-%e6%8f%90%e4%ba%a4%e4%b8%80%e4%b8%aa-pull-request-%e5%88%b0-master-%e5%88%86%e6%94%af%e5%b9%b6%e5%b0%86%e5%85%b6%e5%90%88%e5%b9%b6merge)
      - [4.3 “任务3 在 GitHub 的仓库中提交 Issue”](#43-%e4%bb%bb%e5%8a%a13-%e5%9c%a8-github-%e7%9a%84%e4%bb%93%e5%ba%93%e4%b8%ad%e6%8f%90%e4%ba%a4-issue)
      - [4.4 “任务4.2 通过 下载地址 安装 Github Desktop 桌面客户端，完成后登录自己的账户”](#44-%e4%bb%bb%e5%8a%a142-%e9%80%9a%e8%bf%87-%e4%b8%8b%e8%bd%bd%e5%9c%b0%e5%9d%80-%e5%ae%89%e8%a3%85-github-desktop-%e6%a1%8c%e9%9d%a2%e5%ae%a2%e6%88%b7%e7%ab%af%e5%ae%8c%e6%88%90%e5%90%8e%e7%99%bb%e5%bd%95%e8%87%aa%e5%b7%b1%e7%9a%84%e8%b4%a6%e6%88%b7)
      - [4.5 “任务4.4 在本地电脑的 hello-world 仓库中创建一个名为 local.txt 的文本文件”](#45-%e4%bb%bb%e5%8a%a144-%e5%9c%a8%e6%9c%ac%e5%9c%b0%e7%94%b5%e8%84%91%e7%9a%84-hello-world-%e4%bb%93%e5%ba%93%e4%b8%ad%e5%88%9b%e5%bb%ba%e4%b8%80%e4%b8%aa%e5%90%8d%e4%b8%ba-localtxt-%e7%9a%84%e6%96%87%e6%9c%ac%e6%96%87%e4%bb%b6)
      - [4.6 “任务4.5 通过 Github Desktop 将本地仓库新增的文本文件提交为一个 commit”](#46-%e4%bb%bb%e5%8a%a145-%e9%80%9a%e8%bf%87-github-desktop-%e5%b0%86%e6%9c%ac%e5%9c%b0%e4%bb%93%e5%ba%93%e6%96%b0%e5%a2%9e%e7%9a%84%e6%96%87%e6%9c%ac%e6%96%87%e4%bb%b6%e6%8f%90%e4%ba%a4%e4%b8%ba%e4%b8%80%e4%b8%aa-commit)
      - [4.7 “任务5.3 通过 Github Desktop 将自己账户下 fork 的作业仓库 clone 到本地电脑”](#47-%e4%bb%bb%e5%8a%a153-%e9%80%9a%e8%bf%87-github-desktop-%e5%b0%86%e8%87%aa%e5%b7%b1%e8%b4%a6%e6%88%b7%e4%b8%8b-fork-%e7%9a%84%e4%bd%9c%e4%b8%9a%e4%bb%93%e5%ba%93-clone-%e5%88%b0%e6%9c%ac%e5%9c%b0%e7%94%b5%e8%84%91)
      - [4.8 “任务5.8 回到 Github 自己账户下的作业仓库页面，向远程公用作业仓库的 master 分支发起 Pull Request，在提交的 Pull Request 的标题（title）中填写自己所在的钉钉群名，如示例：【032901】自学训练营 DAY1 ，并在评论（comment）中 @自己的助教（请向助教索要他的 Github 用户名）提醒他检查作业”](#48-%e4%bb%bb%e5%8a%a158-%e5%9b%9e%e5%88%b0-github-%e8%87%aa%e5%b7%b1%e8%b4%a6%e6%88%b7%e4%b8%8b%e7%9a%84%e4%bd%9c%e4%b8%9a%e4%bb%93%e5%ba%93%e9%a1%b5%e9%9d%a2%e5%90%91%e8%bf%9c%e7%a8%8b%e5%85%ac%e7%94%a8%e4%bd%9c%e4%b8%9a%e4%bb%93%e5%ba%93%e7%9a%84-master-%e5%88%86%e6%94%af%e5%8f%91%e8%b5%b7-pull-request%e5%9c%a8%e6%8f%90%e4%ba%a4%e7%9a%84-pull-request-%e7%9a%84%e6%a0%87%e9%a2%98title%e4%b8%ad%e5%a1%ab%e5%86%99%e8%87%aa%e5%b7%b1%e6%89%80%e5%9c%a8%e7%9a%84%e9%92%89%e9%92%89%e7%be%a4%e5%90%8d%e5%a6%82%e7%a4%ba%e4%be%8b032901%e8%87%aa%e5%ad%a6%e8%ae%ad%e7%bb%83%e8%90%a5-day1-%e5%b9%b6%e5%9c%a8%e8%af%84%e8%ae%bacomment%e4%b8%ad-%e8%87%aa%e5%b7%b1%e7%9a%84%e5%8a%a9%e6%95%99%e8%af%b7%e5%90%91%e5%8a%a9%e6%95%99%e7%b4%a2%e8%a6%81%e4%bb%96%e7%9a%84-github-%e7%94%a8%e6%88%b7%e5%90%8d%e6%8f%90%e9%86%92%e4%bb%96%e6%a3%80%e6%9f%a5%e4%bd%9c%e4%b8%9a)
      - [总结](#%e6%80%bb%e7%bb%93-1)
  - [DAY 02](#day-02)
    - [1. 学习内容](#1-%e5%ad%a6%e4%b9%a0%e5%86%85%e5%ae%b9-2)
    - [2. 学习用时](#2-%e5%ad%a6%e4%b9%a0%e7%94%a8%e6%97%b6-2)
    - [3. 收获总结](#3-%e6%94%b6%e8%8e%b7%e6%80%bb%e7%bb%93-2)
    - [4. 遇到的难点与问题](#4-%e9%81%87%e5%88%b0%e7%9a%84%e9%9a%be%e7%82%b9%e4%b8%8e%e9%97%ae%e9%a2%98-2)
      - [4.1 Anaconda 的版本选择](#41-anaconda-%e7%9a%84%e7%89%88%e6%9c%ac%e9%80%89%e6%8b%a9)
      - [4.2 PATH 的设置](#42-path-%e7%9a%84%e8%ae%be%e7%bd%ae)
      - [4.3 VS Code 的配置](#43-vs-code-%e7%9a%84%e9%85%8d%e7%bd%ae)
      - [4.4 “Hello, World!”程序](#44-hello-world%e7%a8%8b%e5%ba%8f)
      - [4.5 JupyterLab 的配置](#45-jupyterlab-%e7%9a%84%e9%85%8d%e7%bd%ae)
      - [4.6 JupyterLab 系统服务配置](#46-jupyterlab-%e7%b3%bb%e7%bb%9f%e6%9c%8d%e5%8a%a1%e9%85%8d%e7%bd%ae)
      - [4.7 把 JupyterLab 设置为桌面应用](#47-%e6%8a%8a-jupyterlab-%e8%ae%be%e7%bd%ae%e4%b8%ba%e6%a1%8c%e9%9d%a2%e5%ba%94%e7%94%a8)
      - [4.8 闲话](#48-%e9%97%b2%e8%af%9d)
      - [总结](#%e6%80%bb%e7%bb%93-2)
  - [DAY 03](#day-03)
    - [1. 学习内容](#1-%e5%ad%a6%e4%b9%a0%e5%86%85%e5%ae%b9-3)
    - [2. 学习用时](#2-%e5%ad%a6%e4%b9%a0%e7%94%a8%e6%97%b6-3)
    - [3. 收获总结](#3-%e6%94%b6%e8%8e%b7%e6%80%bb%e7%bb%93-3)
    - [4. 遇到的难点与问题](#4-%e9%81%87%e5%88%b0%e7%9a%84%e9%9a%be%e7%82%b9%e4%b8%8e%e9%97%ae%e9%a2%98-3)
      - [4.1 看完参考资料后找不到入手点](#41-%e7%9c%8b%e5%ae%8c%e5%8f%82%e8%80%83%e8%b5%84%e6%96%99%e5%90%8e%e6%89%be%e4%b8%8d%e5%88%b0%e5%85%a5%e6%89%8b%e7%82%b9)
      - [4.2 通过搜索完成任务后感觉路数不对](#42-%e9%80%9a%e8%bf%87%e6%90%9c%e7%b4%a2%e5%ae%8c%e6%88%90%e4%bb%bb%e5%8a%a1%e5%90%8e%e6%84%9f%e8%a7%89%e8%b7%af%e6%95%b0%e4%b8%8d%e5%af%b9)
      - [4.3 通过搜索找到理想方法后逐步完善](#43-%e9%80%9a%e8%bf%87%e6%90%9c%e7%b4%a2%e6%89%be%e5%88%b0%e7%90%86%e6%83%b3%e6%96%b9%e6%b3%95%e5%90%8e%e9%80%90%e6%ad%a5%e5%ae%8c%e5%96%84)
      - [总结](#%e6%80%bb%e7%bb%93-3)
  - [DAY 04](#day-04)
    - [1. 学习内容](#1-%e5%ad%a6%e4%b9%a0%e5%86%85%e5%ae%b9-4)
    - [2. 学习用时](#2-%e5%ad%a6%e4%b9%a0%e7%94%a8%e6%97%b6-4)
    - [3. 收获总结](#3-%e6%94%b6%e8%8e%b7%e6%80%bb%e7%bb%93-4)
    - [4. 遇到的难点与问题](#4-%e9%81%87%e5%88%b0%e7%9a%84%e9%9a%be%e7%82%b9%e4%b8%8e%e9%97%ae%e9%a2%98-4)
      - [4.1 去除多余的输出](#41-%e5%8e%bb%e9%99%a4%e5%a4%9a%e4%bd%99%e7%9a%84%e8%be%93%e5%87%ba)
      - [4.2 不同的输出形式](#42-%e4%b8%8d%e5%90%8c%e7%9a%84%e8%be%93%e5%87%ba%e5%bd%a2%e5%bc%8f)
      - [4.3 不同的循环方式](#43-%e4%b8%8d%e5%90%8c%e7%9a%84%e5%be%aa%e7%8e%af%e6%96%b9%e5%bc%8f)
      - [总结](#%e6%80%bb%e7%bb%93-4)
  - [DAY 05](#day-05)
    - [1. 学习内容](#1-%e5%ad%a6%e4%b9%a0%e5%86%85%e5%ae%b9-5)
    - [2. 学习用时](#2-%e5%ad%a6%e4%b9%a0%e7%94%a8%e6%97%b6-5)
    - [3. 收获总结](#3-%e6%94%b6%e8%8e%b7%e6%80%bb%e7%bb%93-5)
    - [4. 遇到的难点与问题](#4-%e9%81%87%e5%88%b0%e7%9a%84%e9%9a%be%e7%82%b9%e4%b8%8e%e9%97%ae%e9%a2%98-5)
      - [4.1 字符串样本的形式](#41-%e5%ad%97%e7%ac%a6%e4%b8%b2%e6%a0%b7%e6%9c%ac%e7%9a%84%e5%bd%a2%e5%bc%8f)
      - [4.2 英文分词](#42-%e8%8b%b1%e6%96%87%e5%88%86%e8%af%8d)
      - [4.3 正则表达式](#43-%e6%ad%a3%e5%88%99%e8%a1%a8%e8%be%be%e5%bc%8f)
      - [4.4 字典的统计和排序](#44-%e5%ad%97%e5%85%b8%e7%9a%84%e7%bb%9f%e8%ae%a1%e5%92%8c%e6%8e%92%e5%ba%8f)
      - [4.5 切片的使用](#45-%e5%88%87%e7%89%87%e7%9a%84%e4%bd%bf%e7%94%a8)
      - [4.6 不同类型的转换](#46-%e4%b8%8d%e5%90%8c%e7%b1%bb%e5%9e%8b%e7%9a%84%e8%bd%ac%e6%8d%a2)
      - [总结](#%e6%80%bb%e7%bb%93-5)
  - [DAY 06](#day-06)
    - [1. 学习内容](#1-%e5%ad%a6%e4%b9%a0%e5%86%85%e5%ae%b9-6)
    - [2. 学习用时](#2-%e5%ad%a6%e4%b9%a0%e7%94%a8%e6%97%b6-6)
    - [3. 收获总结](#3-%e6%94%b6%e8%8e%b7%e6%80%bb%e7%bb%93-6)
    - [4. 遇到的难点与问题](#4-%e9%81%87%e5%88%b0%e7%9a%84%e9%9a%be%e7%82%b9%e4%b8%8e%e9%97%ae%e9%a2%98-6)
      - [4.1 函数的定义和使用](#41-%e5%87%bd%e6%95%b0%e7%9a%84%e5%ae%9a%e4%b9%89%e5%92%8c%e4%bd%bf%e7%94%a8)
      - [4.2 加载模块语句的使用](#42-%e5%8a%a0%e8%bd%bd%e6%a8%a1%e5%9d%97%e8%af%ad%e5%8f%a5%e7%9a%84%e4%bd%bf%e7%94%a8)
      - [4.3 自然语言工具包（NLTK）的使用](#43-%e8%87%aa%e7%84%b6%e8%af%ad%e8%a8%80%e5%b7%a5%e5%85%b7%e5%8c%85nltk%e7%9a%84%e4%bd%bf%e7%94%a8)
      - [4.4 逻辑运算符的使用](#44-%e9%80%bb%e8%be%91%e8%bf%90%e7%ae%97%e7%ac%a6%e7%9a%84%e4%bd%bf%e7%94%a8)
      - [4.5 汉字的匹配方法](#45-%e6%b1%89%e5%ad%97%e7%9a%84%e5%8c%b9%e9%85%8d%e6%96%b9%e6%b3%95)
      - [总结](#%e6%80%bb%e7%bb%93-6)

------

## DAY 00

### 1. 学习内容

前期准备

### 2. 学习用时

2 小时

### 3. 收获总结

1. 明确了“自学是一种社交行为”；
2. 认识到入门营的目的：先完整地做完一轮任务，不求甚解；
3. 要尝试通过多种途径进行学习，包括但不限于：课程文档、官方文档、搜索引擎、课程教练、训练营同学；
4. 不要认为“没什么可谈的”，事实上，学习过程中出的很多问题都并不复杂，觉得需要问就问，觉得可以答就答，不必在意“露怯”；
5. 教学相长，自己可能晃过了别人掉的坑，别人也可能跳过了自己掉的坑，相互帮助，学习效果才会更好。

### 4. 遇到的难点与问题

#### 4.1 网络环境

正常访问 GitHub 和 Google 是个难点，不过班里没有人聊这个（可能是不方便聊），不知都是怎么搞定的，推测应该是八仙过海了。

由于自己主要用的是飞机/火箭，多少关注了些机场相关的信息，这里就提一个评测站好了：
毒药机场简介
<https://duyaoss.com/>

#### 4.2 手册话语

手册当中有大量不甚规范的表达，比如——

- 标点
  > 所谓"自学"，就是"自己一个人（默默地）学"
  - *其中引号有误*
- 名词
  > 可以通过 google 翻译或找到翻译件
  > 文字排版请使用 markdown 语法
  > Github issue 区 是很好的交流场所
  - *其中 Google、Markdown、GitHub 的拼写不规范*
- 病句
  > 训练营由 "新生大学" 发起，针对基础相对薄弱，想要自学 Python 的人组织的训练营。
  > 教研组由李笑来担任组长，帮大家形成以开放的互联网为师，习得自学这门手艺。
  - *这两句话都有成分残缺或赘余的问题*

还有很多同类情况，就不一一列举了。

这类问题在阅读时会给人“磕磕绊绊”的感觉，或许很多人并不在意这些细节，但这些细节会从一个侧面体现出主办方的水平，故而也不应轻慢。

#### 总结

- [x] 科学上网问题已解决
- [ ] 文字问题应整体编修（本条后文不列）

------

## DAY 01

### 1. 学习内容

GitHub 的基本使用

### 2. 学习用时

4 小时

### 3. 收获总结

1. 明确了使用 Git 和 GitHub 的目的——Git 用于版本控制，GitHub 用于网络协作；
2. 掌握了拉取请求（Pull Request）相关的操作；
3. 了解了 GitHub 的工作流程。

### 4. 遇到的难点与问题

#### 4.1 “任务2.3 在 develop 分支中创建一个名为 develop.txt 的文件，提交一个 commit”

1. 创建文件的操作方式在“参考资料1”中没有；
2. 新手在尝试创建 develop.txt 时可能会漏掉“.txt”，应予强调；
3. 底部“Commit changes”区的提交信息（a commit message）比较重要，不填写或仅依靠默认内容有可能导致无法提交，造成困扰，应予强调；
4. “提交一个 commit”表意不明，“commit”本身含义即为“提交”，这一词原本还没有名词词性（GitHub 直接把它当名词用了），故原文的写法令人难以理解，考虑上下文及用例（make a commit、add commits，参见 <https://guides.github.com/introduction/flow/> ），可改为：==填写相关说明（在页面底部），并提交新文件（Commit new file）==，或者：==填写相关说明（在页面底部），并创建一个提交（commit）==；

#### 4.2 “任务2.4 从 develop 提交一个 Pull Request 到 master 分支，并将其合并(merge)”

1. “develop”写为“==develop 分支==”比较好，避免误解；
2. 拉取请求（Pull Request）是 GitHub 协作的核心操作之一，但这个词理解起来颇费思量，简单的解释可以是“请求代码合并”、“请求对方拉你的代码”（ 参见 <https://www.zhihu.com/question/21682976> ），比较详尽的解释建议参考 GitHub 官方的说明网页（ <https://guides.github.com/introduction/flow/> ）；
3. “(merge)”写为“==（Merge）==”比较好，与页面一致。

#### 4.3 “任务3 在 GitHub 的仓库中提交 Issue”

Issue 的位置与“参考资料2”中的截图不一致，应是 GitHub 改版导致的，寻觅了一小会儿。

#### 4.4 “任务4.2 通过 下载地址 安装 Github Desktop 桌面客户端，完成后登录自己的账户”

1. “GitHub Desktop”已经有“桌面”的含义，再说“桌面客户端”有语意重复之嫌，或写为“==GitHub Desktop 客户端==”即可；
2. GitHub Desktop 登录后如果没有克隆任何仓库到本地的话，主菜单出不来，很难找到登出的地方（我错误地登录了一个旧账号，故需要登出），Google 后了解到，可以通过按快捷键 `Ctrl` + `,` 进入 Options 完成登出操作。

#### 4.5 “任务4.4 在本地电脑的 hello-world 仓库中创建一个名为 local.txt 的文本文件”

1. “文本文件”或应写为“==文本文档==”，与 Windows 的表述一致。
2. 为了避免建立扩展名错误的文件（如`local.txt.txt`），应将文件资源管理器设置为显示文件扩展名（【查看】→勾选【文件扩展名】）

#### 4.6 “任务4.5 通过 Github Desktop 将本地仓库新增的文本文件提交为一个 commit”

“提交一个 commit”和“提交为一个 commit”有什么区别？两种表述法都很不清晰，建议改写，或可写为：==填写相关说明（在软件左下角），并提交（Commit to **master**）==。

#### 4.7 “任务5.3 通过 Github Desktop 将自己账户下 fork 的作业仓库 clone 到本地电脑”

1. 这一步耗时甚久，大约 180 MB 的文件，下载速度只有 10~20 KB/s，前后花了约两个小时，手册应该对这种情况予以提醒；
2. Google 了一下，知道了出现这种情况的实际原因—— GitHub 相关的一些域名被限制了（如 <http://github.global.ssl.fastly.net>）；
3. 不同人给了不同的解决方案，如：改 hosts，利用开源中国提供的代码仓库（码云 Gitee）转移，给 GitHub Desktop 设置代理；
4. 个人认为相对彻底的解决方案应该是 GitHub Desktop 整体走代理，方法有两种，一是开 VPN，二是配置 GitHub Desktop；
5. 考虑眼下的实际情况，VPN 不算靠谱，所以就只能配置 GitHub Desktop 了，试验发现，GitHub Desktop 不从系统设置中取代理服务器，用修改配置文件的方法才能设置代理
6. Windows 版 GitHub Desktop 设置代理的方法如下：  
   i. 用文本编辑器打开<code>C:\Users\\<<em>UserName</em>>\\.gitconfig</code> 
   文件，注意 <code><<em>UserName</em>></code> 要换成自己的账户，直接搜索“`.gitconfig`”也可以，这个文件只有扩展名，开头就是一个“.”，别弄错了；  
   ii. 在文件末尾添加代理信息，SOCKS5 代理类似这样：
   ```
    [http]
        proxy = socks5://127.0.0.1:7891
    [https]
        proxy = socks5://127.0.0.1:7891
    ```
    HTTP 代理类似这样：
    ```
    [http]
        proxy = http://127.0.0.1:7890
    [https]
        proxy = http://127.0.0.1:7890
    ```
    其中`127.0.0.1`是本机地址，`7891`和`7890`都是端口号，`proxy`前面有一个制表符（Tab），注意，这里的代理地址仅为范例，以具体情况为准。
7. macOS 版 GitHub Desktop 的 `.gitconfig` 文件在 `~/`，可以在终端（Terminal）用 Vim 打开文件并编辑，步骤为：  
   i. 在终端（Terminal）输入 `vi ~/.gitconfig` 并回车；  
   ii. 按`i`键进入插入（insert）编辑模式；  
   iii. 在文件末尾添加代理信息，格式和 Windows 的一样；  
   iv. 按`ESC`键退出插入编辑模式，输入`:wq`，回车保存。  
   我没有 macOS，所以并没有测试这样操作是否可行，仅供参考。另外，这部分参考了：<https://www.jianshu.com/p/5e74b1042b70>。
8. 对比  
   i. 设置前  
   ![GitHub_Desktop_设置代理前](https://raw.githubusercontent.com/shen-huang/img/master/2019-08/GitHub_proxy_0.png)  
   ii. 设置后  
   ![GitHub_Desktop_设置代理后](https://raw.githubusercontent.com/shen-huang/img/master/2019-08/GitHub_proxy_1.png)

#### 4.8 “任务5.8 回到 Github 自己账户下的作业仓库页面，向远程公用作业仓库的 master 分支发起 Pull Request，在提交的 Pull Request 的标题（title）中填写自己所在的钉钉群名，如示例：【032901】自学训练营 DAY1 ，并在评论（comment）中 @自己的助教（请向助教索要他的 Github 用户名）提醒他检查作业”

1. 标题要求和示例不一致，应为“==填写自己的学号、钉钉群名、日期序号，如：【032901】自学训练营 DAY1==”；
2. 助教的 GitHub 用户名在开营的时候就给出比较好，写在钉钉的名字上也可以，不然写评论的时候临时问可能会有不便。

#### 总结

- [x] 搞清楚“拉取请求（Pull Request，简称 PR）”的目的和意义
- [x] GitHub Desktop 进入 Option 的方法
- [x] GitHub Desktop 代理设置

------

## DAY 02

### 1. 学习内容

配置本地运行开发环境

### 2. 学习用时

6 小时

### 3. 收获总结

1. 成功安装了 Anaconda3 及其他软件/程序；
2. 掌握了 VS Code 扩展的安装方法；
3. 配置了使用 VS Code 撰写 Python 程序和 Markdown 文档的相关扩展；
4. 编写了第一个 Python 程序（Hello, World!）；
5. 明确了提交作业的流程；
6. 配置了 JupyterLab。
7. 写日志的时间远多于学习时间，不知怎么评价……

### 4. 遇到的难点与问题

#### 4.1 Anaconda 的版本选择

本次学习特别强调，学习对象是 Python 3.x，不解答任何 Python 2.x 的问题。

这个要求事实上是暗示要安装 Anaconda3，而非 Anaconda2。实际上现在在 Anaconda 官方网站的[下载页面](https://www.anaconda.com/distribution/)上直接下载的 Windows 版安装包就是 Anaconda3，但助教为了方便学员，特别提供了[清华大学开源软件镜像站的 Anaconda 下载页面](https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/?C=M&O=D)，这个页面上有各种版本的 Anaconda，我就多想了些，觉得 Anaconda 官方网站应该也有类似的下载页面，又回忆起 2015 年的 XcodeGhost 事件，认为从安全的角度考虑，能用官方下载就不用第三方下载，就算用第三方，下载后也要想办法和官方提供的包进行 MD5 对照检查。在这种思路的引导下，我找到了 Anaconda 官方网站的所有版本下载页面（<https://repo.anaconda.com/archive/>），这里有各种版本及其 MD5，我就从这个页面下载了最靠上的 64 位 Windows 版安装包，下载的时候完全没有意识到这是个 Anaconda2 的包。

下载完成后我就一股脑完成了安装，安装界面上的 Python 2.7 也没有警示到我，直到有同学在学习群里贴安装截图询问的时候，我才发觉不对——为什么他的截图上显示的是“Anaconda3”，而我这里是“Anaconda2”？有什么区别？

快速 Google 了一下我就明白了，我弄错安装包了，而且更无奈的是，Anaconda2 和 Anaconda3 没法共存，所以我能做的就是——卸载 Anaconda2，另装 Anaconda3。好在我发现得早，没做更多的设置，也就没有太多的返工。

另外，我在搜索的过程中，发现了另一个 Python 3.x 强于 Python 2.7 的地方：多语言支持，简单说，就是中文支持更好。我觉得就这一条也值得用 Python 3.x。

#### 4.2 PATH 的设置

PATH 指的是“环境变量”，很多人都没听说过这个东西，所以也值得一记。

设置环境变量的目的，是让某个位置的程序在任何位置都能运行。

举例来说，装好 Anaconda3 后，随带的 Python 所在的路径是 <code>C:\Users\\<<em>UserName</em>>\\Anaconda3\python.exe</code>，在没有设置环境变量的情况下，Python 只能在这个文件夹下运行，在其他位置运行——比如 GitHub Desktop 管理的 `hello-world` 文件夹 <code>C:\Users\\<<em>UserName</em>>\\Documents\GitHub\hello-world\\</code> ——的时候，需要输入完整的路径才可以。也就是说，运行一下“Hello, World!”程序，就需要在其所在的文件夹输入这样的指令：
<pre>
<code>C:\Users\<<em>UserName</em>>\Anaconda3\python.exe hello-world.py</code>
</pre>
这显然相当麻烦。
如果把 Python 所在的位置加入了环境变量，同样的工作，只需要这样输入就行了：
<pre>
<code>python hello-world.py</code>
</pre>
影响其实还不仅如此，不设置环境变量的话，很多程序自动化的功能，都会因为找不到需要的文件失效，所以设置环境变量是必不可少的一步。

Anaconda3 在安装的时候对此有所提示——  
![Anaconda3_PATH提示](https://raw.githubusercontent.com/shen-huang/img/master/2019-08/Anaconda3_PATH.png)  
不过按照安装包的说法，是不建议使用上面这个复选框的，我就选择了安装完成后手动设置。

设置的方法是：  
i. 依次打开【控制面板】-【系统和安全】-【系统】-【高级系统设置】-【环境变量(<u>N</u>)...】  
ii. 在【系统变量(<u>S</u>)】区域双击【Path】  
iii. 使用右侧的【新建(<u>N</u>)】按钮添加如下几行
<pre>
<code>C:\Users\<<em>UserName</em>>\Anaconda3
C:\Users\<<em>UserName</em>>\Anaconda3\Scripts
C:\Users\<<em>UserName</em>>\Anaconda3\Lib
C:\Users\<<em>UserName</em>>\Anaconda3\Library\bin
C:\Users\<<em>UserName</em>>\Anaconda3\Library\mingw-w64\bin</code>
</pre>
注意此处的 <code><<em>UserName</em>></code> 需要更换为自己的账户。如果修改了默认安装的文件夹，那就按实际文件夹位置填写，要对应包含这几个位置，不要有错漏。

#### 4.3 VS Code 的配置

学习手册为这一部分给出的参考文档 [VS Code 官方配置 Python 环境教程](https://code.visualstudio.com/docs/python/environments)其实不大适用于这一阶段，说重一点，光这一篇教程就足以劝退不少新人了。

其实如果按手册前文的要求，通过 Anaconda Navigator (Anaconda3) 安装好了 VS Code，那么 Python 的环境基本已经配置好了，更多的由于环境配置出现的问题，其实应该通过配置系统环境变量（见上文）解决。

个人认为，为了 Python 配置 VS Code 更值得参考的文档是 [VS Code 扩展市场](https://code.visualstudio.com/docs/editor/extension-gallery)的介绍，以及 [VS Code Python 入门教程](https://code.visualstudio.com/docs/python/python-tutorial)。

扩展市场是发挥 VS Code 强大潜力不可或缺的一部分。其实从 Anaconda 装好 VS Code 后，Python 扩展已经默认安装了，故而只说 Python 的话，对这部分也可以不了解。不过如果需要其他功能，如 VS Code 的中文界面、Markdown 支持、颜色/图标等个性化界面配置、快捷键调整等等，都得靠从扩展市场装扩展才行，所以知道怎么操作扩展市场，是用好 VS Code 的重要一环。

如果前面该做的步骤都做完了的话，[入门教程](https://code.visualstudio.com/docs/python/python-tutorial)里[先决条件（Prerequisites）](https://code.visualstudio.com/docs/python/python-tutorial#_prerequisites)那部分可以跳过去，从[在项目（工作区）文件夹中启动VS Code（Start VS Code in a project (workspace) folder）](https://code.visualstudio.com/docs/python/python-tutorial#_start-vs-code-in-a-project-workspace-folder)往下看就行了。

也不用看太细（太细也搞不明白），差不多照猫画虎弄弄就行。

值得记录的几点：  
i. 验证 Python 安装，在命令提示符里输入 `python --version` 就行，会提示现在安装的 Python 版本。入门教程里那个 `py` 开头的命令我怎么都没能成功运行，既然目的已经实现，我也就不纠结它了；  
ii. 项目文件夹用文件资源管理器新建就行，不必纠结于命令行。对于本次学习来说，用 VS Code 菜单上的【文件(F)】-【打开文件夹...】打开昨天创建的作业文件夹就行（如 <code>C:\Users\\<em>UserName</em>\Documents\GitHub\selfteaching-python-camp\exercises\\<em>StudentID</em></code>，其中 <code><<em>UserName</em>></code> 是账户，<code><em>StudentID</em></code> 是学号 ）；
iii. Python 解释器（Python interpreter）也可以跳过去，有问题了再琢磨这部分也不迟；  
iv. [配置并运行调试器（Configure and run the debugger）](https://code.visualstudio.com/docs/python/python-tutorial#_configure-and-run-the-debugger)后面的眼下都可以先不看了，将来有需要再回来查吧。

另外，我为了更好地用 VS Code 写日志，买了本全面讲解 Markdown 的书《了不起的 Markdown》（毕小朋著，北京：电子工业出版社，2019.8）（[CSDN 相关页面](https://blog.csdn.net/wirelessqa/article/category/6865384)、[简书相关页面](https://www.jianshu.com/nb/12797531)、[百度试读页面](https://yuedu.baidu.com/ebook/f2ec7e699a6648d7c1c708a1284ac850ad020418)、[亚马逊电子版购买页面](https://www.amazon.cn/dp/B07W2ZN8TM/ref=sr_1_1?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&keywords=%E4%BA%86%E4%B8%8D%E8%B5%B7%E7%9A%84markdown&qid=1565786132&s=gateway&sr=8-1)、[京东（纸质版）购买页面](https://item.jd.com/12669274.html)），里面有一章专门讲了 VS Code，很值得一读。

#### 4.4 “Hello, World!”程序

学习手册要求通过搜索引擎自行完成“Hello, World!”程序的编写，这其实不难，搜索“Python Hello World”很快就能找到相关介绍，可能造成困扰的是，不少介绍用的是 Python 2.7，和 Python 3.x 的语法并不一样，照着写就可能会出问题，这个只能多看多试了。

上文提到的 [VS Code Python 入门教程](https://code.visualstudio.com/docs/python/python-tutorial)里其实就有编写“Hello, World!”程序的逐步说明，所以如果认真过了一遍入门教程，这一步也就完成了。

需要注意的几个点：  
i. 括号（“()”）  
一定要是半角英文括号，成对出现；  
ii. 引号  
单引号（'）、双引号（"）、三引号（'''或"""）有区别有联系，应注意识别，参见：<https://blog.csdn.net/woainishifu/article/details/76105667>；  
iii. 如果想写中文的话（比如“你好，世界！”），需要在程序第一行添加<pre><code># -*- coding: UTF-8 -*-</code></pre>
iv. 建议在程序开头用注释的形式写明程序用途，如

```Python
# -*- coding: UTF-8 -*-

# Filename : 1001S02E02_hello_python.py
# author by : @shen-huang

# 输出“Hello World!”</code>
```

“Hello, World!”现在已经可以算是个[模因（meme）](https://zh.wikipedia.org/wiki/%E8%BF%B7%E5%9B%A0)了，任务之外，了解一下它的[相关信息](https://zh.wikipedia.org/wiki/Hello_World)还是蛮有意思的。

#### 4.5 JupyterLab 的配置

在 Anaconda Navigator 中启动 JupyterLab 就坑了我一下，先是无法启动，重启之后成功启动了，打开了默认浏览器，由于我在系统里设置的默认浏览器是 IE（为了控制微信PC版的网页跳转），出来的页面什么都没有，把网址复制到其他浏览器又要提供 Token，Token 我又找不出来，这就卡住了。

好在笑来老师写过一篇《[JupyterLab 的安装与配置](https://github.com/selfteaching/the-craft-of-selfteaching/blob/master/T-appendix.jupyter-installation-and-setup.ipynb)》，从安装 Anaconda 开始讲了 JupyterLab 的配置过程。

可我照着做的时候遇到了网络错误，痛快解决还是要设置代理——  
i. conda 代理  
用文本编辑器打开 <code>C:\Users\\<<em>UserName</em>>\\.condarc</code> 文件（<code><<em>UserName</em>></code> 是自己的账户），在结尾添加代理，如
<pre>
<code>proxy_servers:
    http: http://127.0.0.1:7890
    https: http://127.0.0.1:7890</code>
</pre>
注意 Anaconda 只能用 HTTP 代理。  
另可参见：  
[How to enable proxy servers with anaconda python?](https://stackoverflow.com/questions/29267646/how-to-enable-proxy-servers-with-anaconda-python)  
ii. pip 代理  
在账户文件夹（<code>C:\Users\\<<em>UserName</em>></code>）下新建文件夹“`pip`”，在其中新建文本文档“`pip.ini`”（注意扩展名），用文本编辑器将文档打开，在其中填写相关设置，如
<pre>
<code>[global]
trusted-host = pypi.python.org
               pypi.org
               files.pythonhosted.org
proxy = http://127.0.0.1:7890</code>
</pre>
其中 `trusted-host` 是可信任的安装路径，如果不是很在意的话，也可以使用中国大陆地区的镜像位置（如 `pypi.douban.com`、`mirrors.aliyun.com` 等），速度也会快不少，使用中国大陆镜像的话，`proxy` 的设置也可以不用做的。  
另可参见：  
[How to use pip on windows behind an authenticating proxy?](https://stackoverflow.com/questions/9698557/how-to-use-pip-on-windows-behind-an-authenticating-proxy)  
[pip 添加 trusted host](https://blog.csdn.net/helinbin/article/details/56834323)  
[linux 设置 pip 镜像 Pip Warning：–trusted-host 问题解决方案](https://www.cnblogs.com/yudar/p/4657511.html)

调试 JupyterLab 配置文件（`jupyter_notebook_config.py`）的时候又卡住很久。

笑来老师给了4个可选的配置，分别是
```
#c.NotebookApp.token = ''
#c.NotebookApp.open_browser = False
#c.NotebookApp.notebook_dir = '~/'
#c.NotebookApp.default_url = '/tree'
```
要启用某一项，把对应行首的`#`号去掉就行了。

第1项没有问题，我只在自己的计算机上用 JupyterLab，没有安全问题，启用这一项即可。

第2项设置的是启动 JupyterLab 的时候是否打开浏览器，我一时间没弄明白这是什么意思，就把它启用了，造成的效果就是从 Anaconda Navigator 里启动 JupyterLab 时进度条走完就没反应了，从 Anaconda Prompt 里输入 `jupyter notebook list` 可以看到服务已经启动，而且还没法用 `jupyter notebook stop` 命令终止服务。我来回试了数次才反映过来，直接在浏览器里访问 `http://localhost:8888` 就能看到  JupyterLab 了，如果要关闭的话，通过菜单【File】-【Shut Down】即可。  
笑来老师提到了一个使用习惯：把一个平时不怎么用的浏览器专门用在 JupyterLab 上，那如果想要在 Anaconda Navigator 里启动 JupyterLab 时直接跳出特定浏览器要怎么办呢？还是要靠修改 `jupyter_notebook_config.py` 文件。  
i. 首先保证 `c.NotebookApp.open_browser = False` 没有启用，就是行首有`#`号；  
ii. 在任意位置（尾部即可）添加要使用的特定浏览器

```python
import webbrowser
webbrowser.register('Kinza', None, webbrowser.GenericBrowser(r'C:\Users\<UserName>\AppData\Local\Kinza\Application\kinza.exe'))
c.NotebookApp.browser = 'Kinza'
```

其中`'Kinza'`是浏览器的名字，`'C:\Users\<UserName>\AppData\Local\Kinza\Application\kinza.exe'`是浏览器可执行文件的位置，注意前面有一个 `r` 字符，表示后面的字符串不转义。很多文档不用 `r` 而用 `u`，实践证明，如果路径是全英文的，那还是用 `r` 比较好，用 `u` 可能会报错。

第3项用于设置 JupyterLab 可访问的根目录，如果 JupyterLab 是从 Anaconda Navigator 启动的话，这一目录实际上是 `.jupyter` 文件夹所在的位置，这就又平添了几分麻烦。  
我所用的一台计算机，配置的是固态硬盘+机械硬盘，我根据日常的习惯，把系统装在了固态硬盘（盘符为 `C`）上，又把账户下的默认文件夹（桌面、文档、图片、视频、音乐、下载等）移动到了机械硬盘（盘符为 `D`）上。这一设置导致 Anaconda 和 GitHub 文件夹默认都装在了 D 盘，而 `.jupyter` 文件夹默认在 C 盘生成，JupyterLab 启动之后看不到 GitHub 文件夹。  
笑来老师建议把这一项设置成 `'~/'`，但这一设置在 Windows 上不适用，我摸索了一阵子，把它设置成了 `'D:\\'` 才成功打开 GitHub 文件夹里的《自学是门手艺》。

第4项用于切换 JupyterLab 和 Jupyter Notebook，我没用过 Jupyter Notebook，也没什么可怀旧的，就没启用这一项。

#### 4.6 JupyterLab 系统服务配置

如果想要将来用 JupyterLab 方便一点，不必每次都从 Anaconda Navigator 启动，还是把 JupyterLab 配置成系统服务比较好。macOS 的配置方法笑来老师写了，Windows 的配置方法如下。

1. **获取创建服务的应用程序 instsrv.exe 和 srvany.exe**  
   instsrv.exe 和 srvany.exe 是 Windows Server 2003 Resource Kit Tools 工具集中的两个程序，配合使用可以将任何 EXE 程序作为 Windows 服务运行。  
   下载地址为：<https://www.microsoft.com/en-us/download/details.aspx?id=17657>。  
   instsrv.exe 和 srvany.exe 可以在安装后的安装文件夹找到，也可以用 7-Zip 等软件直接解开安装包得到。  
   为方便使用，建议将这两个文件放到 `C:\Windows\System32\` 文件夹和 `C:\Windows\SysWOW64\` 文件夹下。
2. **创建 JupyterLab 运行项**  
   如上文所说，JupyterLab 的具体设置是依赖 `jupyter_notebook_config.py` 文件的，为了方便启动，将其复制到 `jupyter.exe` 所在的文件夹 <code>C:\Users\\<<em>UserName</em>>\\Anaconda3\Scripts\\</code> 下，然后创建文本文档，命名为“`jl.cmd`”，在其中写入启动 JupyterLab 的指令

   ```Batchfile
   jupyter lab jupyter_notebook_config.py
   ```

   并保存退出。

3. **创建服务**  
   以管理员身份运行命令提示符，输入

   ```PowerShell
   instsrv.exe JupyterLab C:\WINDOWS\System32\srvany.exe
   ```

4. **完成服务设置**  
   打开注册表编辑器（【开始】-【运行】-【`Regedit`】），定位到：

   ```text
   计算机\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\JupyterLab
   ```

   在其中新建一个字符串值“`DisplayName`”，设置为“`JupyterLab 服务`”，这是对本服务的描述，可填写方便辨别的内容，也可省略。  
   在其中新建一个项，名为“`Parameters`”，再在其中建立 `Application`、`AppDirectory`、`AppParameters` 三个字符串值。  
   `Application` 的值为作为服务运行的程序，这里设置为 
   <code>C:\\\\Users\\\\<<em>UserName</em>>\\\\Anaconda3\\\\Scripts\\\\jl.cmd</code>  
   `AppDirectory` 的值为作为服务运行的程序所在的文件夹位置，这里设置为 <code>C:\\\\Users\\\\<<em>UserName</em>>\\\\Anaconda3\\\\Scripts</code>  
   `AppParameters` 的值为作为服务运行的程序启动时的参数，这里暂不设置。  
   注意 <code><<em>UserName</em>></code> 要换成自己的账户名，所有的反斜杠都是两个。
   ![JupyterLab服务_注册表设置](https://raw.githubusercontent.com/shen-huang/img/master/2019-08/JupyterLab_Server_0.png)
5. **启动服务**  
   打开服务（【开始】-【Windows 管理工具】-【服务】），可找到其中 JupyterLab 项，将其启动类型设置为“自动”，再启动这个服务，以后就可以不通过 Anaconda，直接在浏览器里访问 <http://localhost:8888/lab?> 来使用 JupyterLab 了。
   ![JupyterLab服务](https://raw.githubusercontent.com/shen-huang/img/master/2019-08/JupyterLab_Server_1.png)

注意，服务和进程并不完全关联，启动服务会启动 JupyterLab 进程，但停止服务并不会终止进程，要彻底退出，需要在停止服务后再在管理员身份的命令提示符中运行 `TASKKILL /F /IM jupyter.exe /T` 杀掉进程。如果在停止服务前杀掉了进程，还需要再停止服务，才能重新启动服务。

参见：  
[windows服务注册](https://www.jianshu.com/p/77a0f0660a2d)  
[使用instsrv.exe+srvany.exe将应用程序安装为windows服务](https://blog.51cto.com/qingmu/1248649)  
[Windows下安装Jupyter，作为后台服务运行](https://zhuanlan.zhihu.com/p/35956723)

#### 4.7 把 JupyterLab 设置为桌面应用

一直靠用浏览器访问 <http://localhost:8888/lab?> 来使用 JupyterLab 也有些不便，一方面不直观，另一方面浏览器的分页、地址栏、收藏夹也会占掉不少空间，可以通过使用 Chrome 应用模式启动一个很像桌面应用的 JupyterLab。

简单的方法是在命令提示符里运行：

```PowerShell
"C:\Users\<UserName>\AppData\Local\Google\Chrome\Application\chrome.exe" --app=http://localhost:8888/lab?
```

然后就会出现这样的一个 JupyterLab：
![JupyterLab桌面应用](https://raw.githubusercontent.com/shen-huang/img/master/2019-08/JupyterLab_App.png)

更优雅的形式，是给这行命令建一个快捷方式：  
在合适的位置（如开始菜单的 Anaconda3 (64-bit) 文件夹里）新建一个快捷方式，对象位置填写为  
<code>"C:\Users\\<<em>UserName</em>>\\AppData\Local\Google\Chrome\Application\chrome.exe" --app=http://localhost:8888/lab?</code>  
快捷方式的名称填写为  
`JupyterLab`  
点击“完成(<u>F</u>)”即可。

如果觉得默认的图标不好看，可以更改，JupyterLab 的图标可以在这里下载：<https://github.com/jupyterlab/jupyterlab_app/tree/master/dist-resources>

把这个快捷方式固定到任务栏上点击打开，会另外弹出一个图标运行 JupyterLab，此时在之前快捷方式的图标上点击右键，选择“从任务栏取消固定”，再把新弹出的图标固定到任务栏，在上面点击右键，再在弹出菜单中的浏览器程序图标上点击右键，选择“属性”，把目标修改为”
<code>"C:\Users\\<<em>UserName</em>>\\AppData\Local\Google\Chrome\Application\chrome.exe" --app=http://localhost:8888/lab?</code>“，点击“更改图标(<u>C</u>)”以修改图标，在“常规”选项卡中更改名称为“JupyterLab”，最后点击“确认”就可以了。改完可能不会当即生效，等一等就行。

其实把 JupyterLab 设置为桌面应用并不一定要用 Chrome，基于 Chromium 的浏览器都可以，由于 Chrome 我很常用，就另外装了个不常用的浏览器“[Kinza](https://www.kinza.jp/en/)”来做这件事，其他可选项可参见：<https://zh.wikipedia.org/wiki/Chromium>。

我在这一步也犯了不少傻，先是用了批处理文件，为了不跳命令提示符窗口又用了 VBS，为了固定到任务栏上好看又把 VBS 转成了 EXE，结果发现点击任务栏上的图标后会弹出另一个图标运行 JupyterLab，合不起消不掉，相当尴尬，最后才想起来直接设置快捷方式就行了，真是……汗。

其他参考资料：  
[在应用模式下启动Google Chrome](http://www.kbase101.com/question/46225.html)  
[这样能将网站添加到Win10任务栏](https://www.pconline.com.cn/win10/988/9882805.html)  
[在 Windows 上安装和配置 Jupyter Lab 作为桌面级应用程序](https://blog.csdn.net/weixin_37641832/article/details/94437445#_Chrome__41)  

#### 4.8 闲话

Python、Anaconda、Jupyter 这些名字其实都有不少讲究，了解一下不失为一件趣事。

Python 的名称来自于著名的英国BBC电视喜剧《蒙提·派森的飞行马戏团》（*Monty Python's Flying Circus*），Python 的创始人吉多·范罗苏姆很喜欢这套电视剧，就用其中的“Python”做了程序的名字。另外，“Python”还有巨蟒的含义，故而其徽标设计为了两条缠绕的蛇。

Anaconda 的含义则是一种南美洲热带无毒大蛇“森蚺（rán）”，其作为一个 Python 发行版，使用了一个关系很紧密的名字。Anaconda 的徽标设计与名字一致，是一条头尾相接的蛇。

Jupyter 从 IPython 衍生而来，现在的名字来源于其支持的核心编程语言 Julia、Python、R，是取了三个名字中的字母拼成的，另外“Jupyter”与“Jupiter”谐音，“Jupiter”则有“木星”的含义，这一名字还暗含了对伽利略记录木星卫星发现的笔记本的致敬。Jupyter 的徽标是木星及其卫星的抽象表达，同时还暗指了三个核心编程语言。

另可参见：  
[维基百科的 Python 页面](https://en.wikipedia.org/wiki/Project_Jupyter)  
[维基百科的 Monty Python 页面](https://en.wikipedia.org/wiki/Monty_Python)  
[谁设计了Python的徽标？](https://www.quora.com/Who-designed-Pythons-logo)  
[维基百科的 Anaconda 页面](https://en.wikipedia.org/wiki/Anaconda_(Python_distribution))  
[Anaconda needs a new logo](https://99designs.com/logo-design/contests/anaconda-needs-logo-240255)  
[维基百科的 Project Jupyter 页面](https://en.wikipedia.org/wiki/Project_Jupyter)  
[维基百科的 IPython 页面](https://en.wikipedia.org/wiki/IPython)  
[维基百科的伽利略·伽利莱页面](https://zh.wikipedia.org/wiki/%E4%BC%BD%E5%88%A9%E7%95%A5%C2%B7%E4%BC%BD%E5%88%A9%E8%8E%B1)  
[维基百科的《星际信使》页面](https://zh.wikipedia.org/wiki/%E6%98%9F%E9%9A%9B%E4%BF%A1%E4%BD%BF)  
[清华大学开源软件镜像站新闻页](https://mirrors.tuna.tsinghua.edu.cn/news/)  
[意大利书商伪造伽利略著作以假乱真，藏书圈风声鹤唳](http://zhishifenzi.com/depth/humanity/4520.html)

#### 总结

- [x] 学习 Python 需要的环境配置
- [x] Python 程序的撰写、调试方法
- [x] JupyterLab 的配置

------

## DAY 03

### 1. 学习内容

使用 Python 编写计算器

### 2. 学习用时

5 小时

### 3. 收获总结

1. 对 Python 可实现的功能大致有了些了解；
2. 了解了获取键盘输入信息的方法；
3. 了解了定义函数的方法；
4. 了解了用 if...elif...else 函数控制流程的方法；
5. 知道了用 while 函数控制流程的方法；
6. 知道了 print 函数格式化的方法；
7. 知道了 eval 函数的用法；
8. 知道了 try...except 函数的用法。

### 4. 遇到的难点与问题

#### 4.1 看完参考资料后找不到入手点

看完手册给的参考资料后，我感觉一头雾水，似乎该知道的都写了，但又不知道怎么完成作业。

最主要的问题是：计算器是 Python 内置的功能，还要怎么实现？难道说“输入 `Python` 启动 Python 解释器，输入要计算的算式后回车”就算完成任务了？但这怎么用 .py 文件实现呢？

#### 4.2 通过搜索完成任务后感觉路数不对

我试着 Google 了一下“Python Calculator”和“Python 计算器”，发现了大量的方案，有相对简单的，也有相对复杂的。

本着先易后难的原则，我参考了《[Python Program to Make a Simple Calculator](https://www.programiz.com/python-programming/examples/calculator)》、《[如何在Python 3中做一个简单的计算器程序](https://www.howtoing.com/how-to-make-a-simple-calculator-program-in-python-3)》、《[Python 简单计算器实现](https://www.runoob.com/python3/python3-calculator.html)》等文章，做了第一个版本，实现了：通过 3 次键盘输入，分别获取两个数字和运算符，然后输出运算结果，另外，在除数为 0 的时候，提示错误。

我把这个版本交给教练后，教练表示这样就算完成任务了，但我觉得路数不大对，主要的原因是：操作不直观、和最初的想法距离较大。

#### 4.3 通过搜索找到理想方法后逐步完善

我在 ZingpLiu 的《[Python实现计算器](https://www.cnblogs.com/zingp/p/8666214.html)》一文中读到了这样一句话：

> 前几天有个面试题目：计算字符串"1 + (5 - 2) * 3"，结果为10，不能用`eval()`。

这个“**不能用`eval()`**”引起了我的注意，我就去查了一下 `eval()` 是什么，从 [Python eval() 函数](https://www.runoob.com/python/python-func-eval.html)的介绍页面了解到，`eval()` 就是把其中的表达式直接给 Python 解释器并输出计算结果，这其实就是我之前想找的方法。

`eval()` 加上 `input()` 和 `print()`，一行代码就可以实现计算器了：

```Python
print(eval(input()))
```

我问了一下教练，这样算不算完成任务，教练告诉我也算，“任务不是目的，目的是学习知识”。

不过我觉得，这样完成任务，简洁是简洁了，但还是有些遗憾，比如：

 1. 每次运行只能计算一次，输出结果后就退出了；
 2. 如果输入了错误的内容，会报错直接退出；
 3. 显示的形式不太美观。
 4. 可能有安全隐患。

第一个问题。我一开始参考了上面提到了《[如何在Python 3中做一个简单的计算器程序](https://www.howtoing.com/how-to-make-a-simple-calculator-program-in-python-3)》一文，另外加了个函数 `again()` 专门用于在计算完成后询问是否要计算其他算式，输入 `Y` 就重新开始计算，输入 `N` 就退出。试了几次后觉得这样太繁琐了——每次计算完都得另外按个字母，简洁的方法应该是，计算完直接开始下一次计算，给某个特定输入就退出。  
我又看了一遍文档，注意到了 `while`，搜索之后从《[Python While 循环语句](https://www.runoob.com/python/python-while-loop.html)》知道了，用 `while 1:` 可以实现无限循环，结合 `if` 和 `break` 就可以实现输入某个特定字母后退出。

第二个问题。我在手册给出的《[X分钟速成Y，其中 Y=python3](https://learnxinyminutes.com/docs/zh-cn/python3-cn/)》一文中找到了 `try/except` 块的介绍，又通过参考《[Python 异常处理](https://www.runoob.com/python/python-exceptions.html)》一文，外加试错，找了 3 个特定的错误情况，设定输出错误提示并重新开始循环，避免了意外的报错退出。

第三个问题。我通过调整 `print()` 函数的格式化做了优化。

第四个问题。由于 `eval()` 是直接把其中的字符串当作输入值传给解释器了，这就可能遇到某些别有用心的人构造特别的输入，从这里入手访问甚至读写网站的文件，这一安全隐患通常是靠限制 `eval()` 可接受的内容来避免的。我在这里通过 `import` 引入了 `math` 模块，再用其构造了字典，继而约束了 `eval()` 可接受的输入。

#### 总结

- [x] 编写了一个简单的计算器
- [x] 用不同方式完成了任务
- [x] 通过逐步尝试优化代码

------

## DAY 04

### 1. 学习内容

打印两种形式的九九乘法表

### 2. 学习用时

4 小时

### 3. 收获总结

1. 了解了条件判断（`if...elif...else`）语句的用法；
2. 了解了循环（`for...in`、`while`、`break`、`continue`）语句的搭配和使用；
3. 了解了生成数字序列的方法（使用 `range()` 函数）；
4. 巩固了格式化输出（`print()` 函数）的方法。

### 4. 遇到的难点与问题

#### 4.1 去除多余的输出

通过两层循环嵌套输出大九九并不困难，但在这个基础上去掉一半输出小九九就稍有难度了。

我个人是通过做一次条件判断，只输出一数小于或等于另一数的情况完成了任务。

任务的第二部分要求去掉九九表的偶数行，这个困扰了我一阵子。

判断是不是偶数行不难，求余（“`%`”）就行了，加个 `if` 判断一下再输出就可以完成任务。

但任务要求用 `while` 循环来实现。

开始我就只用 `while` 加了一个判断，运行的时候发现会导致无限循环，又看了看文档，明白得配合 `break` 用，但 `while` 和 `break` 具体加在哪里颇费了一番思量。来回试验了好久，甚至手绘了流程图，我才实现了需要的输出。

#### 4.2 不同的输出形式

任务中的要求输出是这样的——  

![九九乘法表（原始）](https://raw.githubusercontent.com/shen-huang/img/master/2019-08/9x9_Table_0.png)

但这个输出有几个不尽如人意的地方：

1. 对齐不正，第 4 行和第 5 行的空隙由于进位歪了；
2. 符号不当，乘号应该写作“×”，使用星号（*）替代是不得已而为之，不应当作正式用法；
3. 顺序不佳，习惯中的九九表应该是小数在前大数在后，此处颠倒了。

这几个问题的解决方法倒很简单：

1. 把 `print()` 函数的结尾符设置为制表符即可（不知为什么教程里特意写了这么一句但示意输出却用的是 3 个空格）；
2. 把 `print()` 里的“*”改成“×”即可；
3. 把 `print()` 里的变量顺序调整一下即可。

除此之外，我还试了一下另一个方向的九九表——

![九九乘法表（转向）](https://raw.githubusercontent.com/shen-huang/img/master/2019-08/9x9_Table_1.png)

这是常见的九九表的转置，也是最初的大九九去掉另外一半的效果，不过这么排版对对齐有进一步的要求，也算是额外的练习了。

#### 4.3 不同的循环方式

除了原本的要求外，我还试验了其他完成任务的方式，如：

- 用变量控制 `range()` 函数的右边界以省略两数大小判断；
- 把循环区间设定为 `[1, 3, 5, 7, 9]` 以省略 `while` 循环；
- 用 `if` 替代 `while` 实现判断；
- 用 `if...continue` 替代 `while...break` 实现判断。

算是把不同的循环方式都练习了几遍。

#### 总结

- [x] 输出了不同形式的九九表
- [x] 改善了原始的输出形式
- [x] 用不同方式完成了任务
- [x] 通过逐步尝试优化代码

------

## DAY 05

### 1. 学习内容

字符串的基本处理，词频统计，数组操作，进制转换

### 2. 学习用时

6 小时

### 3. 收获总结

1. 了解了字符串相关的替换、删除、大小写转换等工作的方法；
2. 了解了由字符串分词生成列表的方法；
3. 了解了列表的排序方法；
4. 了解了字典的生成和排序方法；
5. 明确了列表、元组、字典的联系和区别；
6. 了解了切片的使用方法；
7. 了解了数字类型和字符串类型的转换方法；
8. 了解了由列表拼接字符串的方法；
9. 了解了十进制数到二进制数、八进制数、十六进制数的转换方法。

### 4. 遇到的难点与问题

和第 3 天一样，看完手册给的参考资料后感觉信息量太大，依靠了多次 Google 才完成了任务。

#### 4.1 字符串样本的形式

任务手册中给出的字符串样本是著名的《Python 之禅》（*The Zen of Python*），其最早由蒂姆·彼得斯（Tim Peters）在 Python 邮件列表中发表，它包含了影响 Python 编程语言设计的 19 条程序编写原则。

《Python 之禅》被内置到了 Python 的 `this` 模块中，只需要运行 `import this` 就会被输出。

但手册中所呈现的字符串样本又与内置的内容有所区别，表现在：

- 开头多了一个空行；
- 标题和正文间多了一个空行；
- 有错别字（“ambiguity”写成了“ambxiguity”）；
- 结尾多了一个空行。

另外，原始的文本由于种种原因，使用了“打字机风格”，具体表现在：

- 单引号（‘、’）和撇号（’）使用了直引号（'）进行替代；
  <!-- 单引号：single quotation mark；撇号：apostrophe。-->
- 破折号（—）使用了两个连字符（--）进行替代；
- 强调使用了成对星号（*）进行表达。

原始文本还有令人纠结的一点，就是破折号左右的空格。破折号左右要不要留空格是个见仁见智的问题，但至少应当全文一致，可原始文本的三个破折号用法各异，这就难以解释了。

这些问题虽然从完成任务的角度来说无需关心，但从排版的角度来说，足够让人产生如鲠在喉的感觉，况且 Python 3.x 默认使用的编码已经是 Unicode，完全可以在文本上解决引号、破折号等问题。

本着这样的想法，我在原始文本的基础上，考虑了排版规则，结合[维基百科的 The Zen of Python 页面](https://en.wikipedia.org/wiki/Zen_of_Python)的内容，生成了作为练习使用的字符串文本。

此外，我顺着《Python 之禅》找到了[一系列的《Python 增强提案》（*Python Enhancement Proposals*，缩写为 PEPs）](https://www.python.org/dev/peps/)，这其中的[《Python 编码规范》（*Style Guide for Python Code*，编号为 PEP 8）](https://www.python.org/dev/peps/pep-0008/)应该是学习 Python 编程的必读文本，其他的提案也可以选择性地读一读。

另可参见：  
[维基百科的 Python 之禅页面](https://zh.wikipedia.org/wiki/Python%E4%B9%8B%E7%A6%85)  
[蛇宗三字经（The Zen of Python）](https://note.qidong.name/2018/01/the-zen-of-python/)  
[写在最前面：The Zen of Python](https://zhuanlan.zhihu.com/p/51252175)  
[Python 的众多 PEP 之中，除了 PEP 8，还有哪一些是值得阅读的？](https://www.zhihu.com/question/23484654)  
[维基百科的英文破折号（—）页面](https://en.wikipedia.org/wiki/Dash)  
[别再用「六个点」当省略号了，这些标点都有更规范的输入方式](https://sspai.com/post/45516)  
[中文排版需求](https://www.w3.org/TR/clreq/)  
[Mathematical Alphanumeric Symbols](https://en.wikipedia.org/wiki/Mathematical_Alphanumeric_Symbols)  
[VS Code 写 Python 时的代码错误提醒和自动格式化](https://blog.csdn.net/BNK_along/article/details/84000953)  
[Linting Python in Visual Studio Code](https://code.visualstudio.com/docs/python/linting)

#### 4.2 英文分词

分词是个大问题。

简单的文本，可以通过空格分词，但稍微复杂一点的文本，处理起来就很耗神。

怎么叫“复杂”？包括但不限于：

- 小数（1.25之类）；
- 复杂词形（$10、10% 之类）；
- 缩略语（U.S.A. 之类）；
- 包含连字符的词汇（self-teaching 之类）；
- 特殊符号（...、-- 之类）
- 转义符（\n 之类）。

还好，本次练习要处理的文本，不算太复杂。

不过要完成的目标（去掉文本中包含“ea”的单词），还是对分词有些要求的。举例来说，“idea—let’s”这样的部分，就得把“idea”去掉，别的内容保留，之后还要处理破折号两侧可能出现的多余空格。

简单的分词用 `split()` 函数就行，但本次用作分词的分隔符不只一个，故而选择通过加载正则表达式模块（`re`），通过 `re.split()` 函数完成分词。这里有两个要注意的地方：

- 间隔符表达式如果带括号（(…)），生成的列表里就包括分隔符，反之则不包括；
- 正则表达式字符串建议在前面加上标记 `r`，举例来说，我使用的表达式为 `r'(\s|,|\.|—)'`。

更复杂的分词可以通过加载其他的分词工具完成，具体可以参见《[Python 文本数据分析初学指南](https://datartisan.gitbooks.io/begining-text-mining-with-python/)》的“[4.2 英文分词及词性标注](https://datartisan.gitbooks.io/begining-text-mining-with-python/第4章%20分词与词性标注/4.2%20英文分词及词性标注.html)”部分。

#### 4.3 正则表达式

正则表达式（Regular Expression，常简写为 regex、regexp 或 RE）是计算机科学的一个概念，其使用单个字符串来描述、匹配一系列符合某个句法规则的字符串。[^Wiki_cs_RE]

简单地说，如果需要查找或替换某个具体的字词，使用普通的查找或替换工具就可以了，但如果需要查找或替换的，是符合某些特定规则的字符串，就需要依靠正则表达式了。

快速地了解一下正则表达式，可以阅读[陆超](http://deerchao.net/)编写的《[正则表达式30分钟入门教程](http://deerchao.net/tutorials/regex/regex.htm)》，深入学习，可以参考[杰弗里·弗里德尔（Jeffrey E. F. Friedl）](http://regex.info/)撰写的 500 多页的大部头《[精通正则表达式](https://book.douban.com/subject/2154713/)》和[余晟](https://www.luanxiang.org/blog/)撰写的《[正则指引](https://book.douban.com/subject/30352656/)》，还可以通过使用 [Regester](http://deerchao.net/tools/regester/index.htm) 和 [RegexBuddy](http://www.regexbuddy.com/) 等软件进行练习和测试。

无论如何，正则表达式的语法都很难读写，令人头疼，可为了它能实现的功能，只能认了。

上文已经说过，在 Python 里使用正则表达式需要加载正则表达式模块（`re`），不过在我用的时候遭遇了这么几个问题：

1. **后向引用**  
   我认为包含撇号（’）的单词（如 ’s、’re、don’t 等），应该单独特别处理，而非简单地和它周围的词混在一起。举例来说，“Let’s”应该断成“Let”和“’s”，“don’t”就应该是一个整体。  
   好在要处理的文本只有 3 个撇号，都是断开就行的，我就简化处理了——在撇号之前加空格把它和关联单词分开。  
   完成这个任务需要使用“后向引用”，其默认的表达方式应该是类似“`\1`”、“`\2`”这样的，但我调了数次都报错，又作了一番功课才明白在这里应该用“`\\1`”、“`\\2`”。  
   捎带要提一下的是，VS Code 里的查找/替换功能也可以用正则表达式，但它的后向引用要写成“`$1`”、“`$2`”这种形式。
2. **转义序列**  
   “转义（escape）”是指用多个字符的有序组合来表示原本需要的字符的手段，“转义序列（escape sequence）”则指在转义时使用的有序字符组合。[^Wiki_cs_Escape_Sequence]  
   转义序列通常用作表示那些“无法直接输入”的字符，比如回车符、换行符、制表符等等。  
   在 Python 里，转义序列是用“`\`”开头的一系列字符组合，常用的有：换行符“`\n`”，制表符“`\t`”。  
   但在正则表达式里，也会用到转义序列，正则表达式的转义序列还比 Python 多些，如：空白符“`\s`”，数字“`\d`”，单词边缘“`\b`”等。
   转义序列很有用，可也会带来麻烦，比如要输入 `'C:\new\'` 这个路径的字符串，其中的 `\n` 就会被转义，要避免这一问题，有两种方式：一，使用“`\\`”来表示不需要转义的反斜线（\），也即写为 `'C:\\new\'`，二，使用“`r`”标记告诉 Python 此处不转义，也即写为 `r'C:\new\'`。
   当在 Python 里用正则表达式时，问题就更严重了，因为 Python 本身会处理一层转义，正则表达式又会处理一层转义，故而要向正则表达式里传递一个不转义的“\”，字符串要写成“`'\\\\'`”，这实在是很麻烦，在这种情况下，建议更多地使用“`r`”标记来处理正则表达式。
   Python 官方发布的静态代码检查工具 [Flake8](http://flake8.pycqa.org/en/latest/) 现在已经把所有 Python 不支持的转义序列标记成错误，提示“[invalid escape sequence 'x' (W605)](https://lintlyci.github.io/Flake8Rules/rules/W605.html)”，解决的办法也是在相应字符串加“`r`”标记。  
   除了“`r`”外，字符串可用的标记还有“`u`”、“`f`”等，具体使用可以参见《[*The Python Language Reference*](https://docs.python.org/3/reference/index.html)》的“[2.4.1. String and Bytes literals](https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals)”和“[2.4.3. Formatted string literals](https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals)”部分。
3. **特殊字符**  
   正则表达式里的“`\s`”困惑了我一阵子。我一开始用它来匹配空格了，发现不好用。搜索了一下才明确，“`\s`”可以匹配任意的空白符，包括制表符（`\t`，即`'\u0009'`）、换行符（`\n`，即`'\u000A'`）、回车符（`\r`，即`'\u000D'`）、换页符（`\f`，即`'\u000C'`）、竖向制表符（`\v`，即`'\u000B'`）、半角空格（“ ”，即`'\u0020'`），如果是 Unicode 的正则表达式，`\s` 还可以匹配全角空格（“　”，即`'\u3000'`）。  
   半角空格没有转义序列，要怎么匹配呢？查了好一会儿我才反应过来，直接输入“ ”就可以了……  
   顺便我还了解了一下各种不同编码的转义序列表达法，前面“`\u`”开头的那些字符串，就是 Unicode 编码的转义序列表达法，具体细节可以参见《[JavaScript 转义字符](https://www.cnblogs.com/zhankang/articles/4881314.html)》（[*JavaScript character escape sequences*](https://mathiasbynens.be/notes/javascript-escapes)），《[字符编码笔记：ASCII，Unicode 和 UTF-8](http://www.ruanyifeng.com/blog/2007/10/ascii_unicode_and_utf-8.html)》，《[Unicode 与 JavaScript 详解](http://www.ruanyifeng.com/blog/2014/12/unicode.html)》等文，具体字符的转换可以用站长之家提供的[Unicode编码转换](https://tool.chinaz.com/tools/unicode.aspx)工具。

#### 4.4 字典的统计和排序

生成字典不难，有这么几个值得记录的点：

1. 使用“`not in`”而非“`not...in`”  
   更具体地说，`if w not in text` 和 `if not w in text` 是等价的，但前一种写法更易读。  
   现在 Flake8 会把“`not...in`”标记出来（[E713](https://lintlyci.github.io/Flake8Rules/rules/E713.html)）并给出修改为“`not in`”的建议，同理，“`is not`”和“`not...is`”也有同样的问题（[E714](https://lintlyci.github.io/Flake8Rules/rules/E714.html)）。[PEP 8](https://www.python.org/dev/peps/pep-0008/) 对此也有[说明](https://www.python.org/dev/peps/pep-0008/#programming-recommendations)。另可参考《[Python 中 not 的用法](https://blog.csdn.net/Evan123mg/article/details/50174669)》一文。
2. 字典、元组、列表  
   字典不能直接排序，需要用 `item()` 函数把字典转成一个由元组构成的列表，然后再用 `sorted()` 函数排序。  
   这里可能出现的波折是混淆了 `sort()` 和 `sorted()`。简单说，由字典转成的列表，不能用 `sort()` 排序，只能用 `sorted()` 排序。更多的信息可以参考《[Python 中列表、元组及字典的排序](https://blog.csdn.net/Kyrie001/article/details/82528011)》、《[Python 中方法 sort() 和函数 sorted() 的区别](https://blog.csdn.net/chengxugou001/article/details/79684615)》、《[Python 中排序函数 sort() 和 sorted() 的区别](https://blog.csdn.net/sinat_35512245/article/details/79584196)》等文。
3. lambda 表达式  
   使用 `sorted()` 排序会用到 lambda 表达式，这个稍稍有些不易理解。  
   lambda 表达式定义的是一个“匿名函数”，是为了简化代码而使用的。  
   举例来说，

   ```Python
   lambda x: x[1]
   ```

   和

   ```Python
   def g(x):
      return x[1]
   ```

   的功能是一样的。  
   更进一步说，

   ```Python
   sorted(text, key=lambda x: x[1])
   ```

   和

   ```Python
   def g(x):
      return x[1]


   sorted(text, key=g)
   ```

   的功能也是一样的。  
   显然，在使用 `sorted()` 的时候，lambda 表达式可以实现更简练的代码。不过，lambda 表达式会在一定程度上降低程序的可读性，所以要慎用。  
   什么时候用 lambda 表达式，Goodpy 在《[Python lambda 介绍](https://www.cnblogs.com/evening/archive/2012/03/29/2423554.html)》一文给了些很好的建议：
   > - lambda 并不会带来程序运行效率的提高，只会使代码更简洁。
   >
   > - 如果可以使用 `for...in...if` 来完成的，坚决不用 lambda。
   >
   > - 如果使用 lambda，lambda 内不要包含循环，如果有，我宁愿定义函数来完成，使代码获得可重用性和更好的可读性。

   另可参考：  
   [Python: 使用 lambda 应对各种复杂情况的排序，包括 list 嵌套 dict](https://www.polarxiong.com/archives/Python-使用lambda应对各种复杂情况的排序-包括list嵌套dict.html)  
   [Python `dict()` 函数](https://www.runoob.com/python/python-func-dict.html)

#### 4.5 切片的使用

切片是从字符串、列表、元组中抽取部分内容的操作。它很常用，不过有些地方会让人有些困惑，记录如下。

首先要明确每一个元素的位置编号，以列表 `li = ['A', 'B', 'C', 'D', 'E', 'F', 'G']` 为例——

|列表元素|'A'|'B'|'C'|'D'|'E'|'F'|'G'|
|:-----:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|正序编号|0|1|2|3|4|5|6|
|逆序编号|-7|-6|-5|-4|-3|-2|-1|

注意正序编号是从 0 开始的，逆序编号是从 -1 开始的。

切片的语法是 `list[start:stop:step]`，即 `名称[开始:结束:步伐]`。这其中：

- 步伐可以省略，默认值为“1”；
- 开始和结束的值可以省略，默认值为列表的两端（不是第一个元素和最后一个元素）；
- 开始和结束中间的冒号不可省略；
- 步伐既可以为正值，也可以为负值，正值表示正序取值，负值表示逆序取值；
- 步伐为正值时，开始位置应在结束位置左侧，步伐为负值时，开始位置应在结束位置右侧，否则不会取出任何元素；
- 开始和结束的值既可以用正序编号，也可以用逆序编号，两种编号可以混用；
- 开始位置的元素会取出，结束位置的元素不会取出；
- 所用位置编号可以超出列表的元素位置编号；
- 所有的冒号两侧都没有空格。

还以列表 `li = ['A', 'B', 'C', 'D', 'E', 'F', 'G']` 为例——

|<span style="white-space: nowrap;">行号</span>|<span style="white-space: nowrap;">代码　　　　　</span>|<span style="white-space: nowrap;">结果　　　　　　　　　　　　　　　　　　</span>|<span style="white-space: nowrap;">注释</span>|
|:--:|----|----|----|
|1|`li[:]`|`['A', 'B', 'C', 'D', 'E', 'F', 'G']`|从列表左端取到列表右端，即取了整个列表|
|2|`li[::1]`|`['A', 'B', 'C', 'D', 'E', 'F', 'G']`|从列表左端取到列表右端，步伐为“1”，即取了整个列表|
|3|`li[::2]`|`['A', 'C', 'E', 'G']`|从列表左端取到列表右端，步伐为“2”，即每 2 个元素取 1 个元素，取出第 0、2、4、6 号元素|
|4|`li[::3]`|`['A', 'D', 'G']`|从列表左端取到列表右端，步伐为“3”，即每 3 个元素取 1 个元素，取出第 0、3、6 号元素|
|5|`li[::-1]`|`['G', 'F', 'E', 'D', 'C', 'B', 'A']`|从列表左端取到列表右端，步伐为“-1”，把整个列表逆序|
|6|`li[::-2]`|`['G', 'E', 'C', 'A']`|从列表右端取到列表左端，步伐为“-2”，取出第 -1、-3、-5、-7 号元素|
|7|`li[2:5]`|`['C', 'D', 'E']`|从编号为 2 的元素（含）取到编号为 5 的元素（不含），步伐为默认值“1”，取出第 2、3、4 号元素|
|8|`li[2:5:1]`|`['C', 'D', 'E']`|从编号为 2 的元素（含）取到编号为 5 的元素（不含），步伐为“1”，取出第 2、3、4 号元素|
|9|`li[2:5:-1]`|`[]`|从编号为 2 的元素（含）取到编号为 5 的元素（不含），步伐为“-1”，没有取出元素|
|10|`li[5:2:-1]`|`['F', 'E', 'D']`|从编号为 5 的元素（含）取到编号为 2 的元素（不含），步伐为“-1”，取出第 5、4、3 号元素|
|11|`li[0:6]`|`['A', 'B', 'C', 'D', 'E', 'F']`|从编号为 0 的元素（含）取到编号为 6 的元素（不含），步伐为默认值“1”，取出第 0、1、2、3、4、5 号元素|
|12|`li[0:-1]`|`['A', 'B', 'C', 'D', 'E', 'F']`|从编号为 0 的元素（含）取到编号为 -1 的元素（不含），步伐为默认值“1”，取出第 0、1、2、3、4、5 号元素|
|13|`li[0:]`|`['A', 'B', 'C', 'D', 'E', 'F', 'G']`|从编号为 0 的元素（含）取到列表右端，步伐为默认值“1”，取了整个列表|
|14|`li[0:9]`|`['A', 'B', 'C', 'D', 'E', 'F', 'G']`|从编号为 0 的元素（含）取到编号为 9 的元素（不含），步伐为默认值“1”，由于最大元素编号为 6，取了整个列表|
|15|`li[9:0:-1]`|`['G', 'F', 'E', 'D', 'C', 'B']`|从编号为 9 的元素（含）取到编号为 0 的元素（不含），步伐为默认值“-1”，由于最大元素编号为 6，取出第 6、5、4、3、2、1 号元素|
|16|`li[9:-9:-1]`|`['G', 'F', 'E', 'D', 'C', 'B', 'A']`|从编号为 9 的元素（含）取到编号为 - 的元素（不含），步伐为默认值“-1”，由于最大元素编号为 6，最小元素编号为 -7，取出第 6、5、4、3、2、1、0 号元素|
|17|`li[0::-1]`|`['A']`|从编号为 0 的元素（含）取到列表左端，步伐为“-1”，取出第 0 号元素|
|18|`li[:0:-1]`|`['G', 'F', 'E', 'D', 'C', 'B']`|从列表右侧取到编号为 0 的元素（不含），步伐为“-1”，取出第 -1、-2、-3、-4、-5、-6 号元素|
|19|`li[1:-2:-1]`|`[]`|从编号为 1 的元素（含）取到编号为 -2 的元素（不含），步伐为“-1”，没有取出元素|
|20|`li[-2:1:-1]`|`['F', 'E', 'D', 'C']`|从编号为 -2 的元素（含）取到编号为 1 的元素（不含），步伐为“-1”，取出第 -2、-3、-4、-5 号元素|
|21|`li[0:3:-1]`|`[]`|从编号为 0 的元素（含）取到编号为 3 的元素（不含），步伐为“-1”，没有取出元素|
|22|`li[:3:-1]`|`['G', 'F', 'E']`|从列表右端取到编号为 3 的元素（不含），步伐为“-1”，取出第 -1、-2、-3 号元素|

字符串和元组的操作与列表类似。

要翻转（逆序）一个名为 `li` 的列表有两种途径，一种是用 `li.reverse()`，另一种是用 `li[::-1]`。但要翻转字符串和元组就只能用切片了。这样来看，切片的方法比较通用。

字典不能切片，不过可以用把字典的关键字转成列表，对列表切片，再用查询重新生成字典的方法实现切片，具体的操作可以参考李阳良的《[Python 字典切片](http://liyangliang.me/posts/2012/12/python-dict-slice/)》一文。

另可参考：  
[Python 教程·高级特性·切片](https://www.liaoxuefeng.com/wiki/1016959663602400/1017269965565856)  
[贝斯狸的 Python 之旅——深入切片操作及原理](https://juejin.im/post/5b5a0c316fb9a04fb4016e19)  
[全面深入彻底理解 Python 切片操作](https://blog.csdn.net/xpresslink/article/details/77727507)  
[Python 中 list 的切片细节](https://blog.csdn.net/hengyunabc/article/details/6540157)  
[Python 中的列表（list）切片详解](https://www.cnblogs.com/xuchunlin/p/6045282.html)

#### 4.6 不同类型的转换

由数字构成的列表不能直接拼接成字符串，得把列表的每个元素都转成字符串才行。

类型转换调用相应的函数就能完成，遍历列表的每个元素可以使用 `for...in...if` 语句。

Python 里可用的转换函数有这些：

|<span style="white-space: nowrap;">函数　　　　　　　　　　</span>|说明|
|----|----|
|`int(x[, base])`         |将 `x` 转换为一个整数，**强制类型转换**|
|`long(x[, base])`        |将 `x` 转换为一个长整数|
|`float(x)`               |将 `x` 转换到一个浮点数，**强制类型转换**|
|`complex(real[, imag])`  |创建一个复数|
|`str(x)`                 |将对象 `x` 转换为字符串，**强制类型转换**|
|`repr(x)`                |将对象 `x` 转换为表达式字符串|
|`eval(str)`              |用来计算在字符串中的有效 Python 表达式，并返回一个对象|
|`list(s)`                |将序列 `s` 转换为一个列表，**强制类型转换**|
|`tuple(s)`               |将序列 `s` 转换为一个元组，**强制类型转换**|
|`set(s)`                 |将序列 `s` 转换为一个集合，**强制类型转换**|
|`chr(x)`                 |将一个整数转换为一个字符，Python 3.x 可以用其处理 Unicode 字符了|
|`unichr(x)`              |将一个整数转换为 Unicode 字符，Python 3.x 将其合并进了 chr(x)|
|`ord(str)`               |将一个字符转换为它的整数值|
|`bin(x)`                 |将一个整数转换为一个二进制字符串|
|`oct(x)`                 |将一个整数转换为一个八进制字符串|
|`hex(x)`                 |将一个整数转换为一个十六进制字符串|

这里的 `eval(str)` 在第 3 天做计算器的时候也提到过。`str(x)` 和 `repr(x)` 有联系也有区别，具体可参见叶俊贤的《[Python 中 `str()` 与 `repr()` 函数的区别](https://www.jianshu.com/p/2a41315ca47e)》一文。还有一些数据类型转换的细节，可以参考范桂飓的《[Python基本语法——强制数据类型转换](https://blog.csdn.net/Jmilk/article/details/49720611)》一文和 Davidham 的《[Python 中的强制类型转换](https://www.jianshu.com/p/bc57ad6f35c4)》一文。

其他参考资料：  
《[Python进阶](http://interpy.eastlakeside.com/)》（[*Intermediate Python*](http://book.pythontips.com)），穆罕默德·耶苏布·乌拉·哈立德（[Muhammad Yasoob Ullah Khalid](https://yasoob.me/)）著，刘宇（[@liuyu](https://github.com/liuyu)），老高（[@spawnris](https://github.com/spawnris)），大牙码特（[@suqi](https://github.com/suqi)），明源（[@muxueqz](https://github.com/muxueqz)）等译  
[给非 Python 开发的 Python 快速自学资源整理](http://eastlakeside.com/2017/02/19/python-self-learn/)  
[Python 教程](https://www.liaoxuefeng.com/wiki/1016959663602400)，[廖雪峰](https://www.liaoxuefeng.com/)著

#### 总结

- [x] 巩固了一些英文标点的用法
- [x] 字符串内容的查找、替换、删除
- [x] 字符串的大小写转换
- [x] 英文单词词频统计与输出
- [x] 数组的基础操作
- [x] 不同进制数字的转换

[^Wiki_cs_RE]:参见[维基百科的“正则表达式”页面](https://zh.wikipedia.org/wiki/正则表达式)
[^Wiki_cs_Escape_Sequence]:参见[维基百科的“转义序列”页面](https://zh.wikipedia.org/wiki/转义序列)

------

## DAY 06

### 1. 学习内容

函数的用法

### 2. 学习用时

2 小时

### 3. 收获总结

1. 了解了函数定义的方法
2. 熟悉了加载模块的方法
3. 学习了正则表达式的写法

### 4. 遇到的难点与问题

#### 4.1 函数的定义和使用

定义函数使用这样的语法——

```Python
def function_name(parameters):
    """function’s documentation string"""
    function_suite
    return [expression]
```

其中：

- `function_name` 是函数名，程序用这个名字来调用函数。  
  具体要怎么起这个名字，Python 3.7.4 官方文档《[Python 语言参考](https://docs.python.org/zh-cn/3.7/reference/index.html)》的《[2.3. 标识符和关键字](https://docs.python.org/zh-cn/3.7/reference/lexical_analysis.html#identifiers)》部分给出了使用字符的范围：
  > 在 ASCII 范围内 (U+0001..U+007F)，可用于标识符的字符与 Python 2.x 一致: 大写和小写字母 `A` 至 `Z`，下划线 `_` 以及数字 `0` 至 `9`，但不可以数字打头。

  由于 Python 3.0 引入了 Unicode，所以现在可以用的字符大大增加了，什么 `ǅ`、`ᾮ`、`ๆ`、`ꀕ`、`ↈ`、`𒐝`、`𒐱`、`꜉`、`꜕`、`۵`、`꘨` 等等的都能用。但是，为了通用性，别作妖，应该<span style="color: OrangeRed;">坚持使用ASCII范围内的字符</span>。  
  另外，具体的命名风格《[*PEP 8 — Style Guide for Python Code*](https://www.python.org/dev/peps/pep-0008/)》在《[*Descriptive: Naming Styles*](https://www.python.org/dev/peps/pep-0008/#id36)》部分给出了建议，简单地说，单个大小写字母、单个全大写或全小写单词、用下划线连接的全大写或全小写单词、首字母大写的无间隔单词、第一个单词首字母小写其余单词首字母大写的无间隔单词，这些都可以，用下划线连接的首字母大写单词也行，但是丑陋。  
  此外，《[*PEP 8*](https://www.python.org/dev/peps/pep-0008/)》的《[*Prescriptive: Naming Conventions*](https://www.python.org/dev/peps/pep-0008/#id37)》部分针对变量名、包和模块名、类名、变量类型名、异常名、函数名、方法名、常量名等等做出了详细的约定。《[Python 教程](https://docs.python.org/zh-cn/3/tutorial/index.html)》的《[4.8. 小插曲：编码风格](https://docs.python.org/zh-cn/3/tutorial/controlflow.html#intermezzo-coding-style)》也讲了相关的问题。  
  具体到函数名，应该使用全小写单词，根据需要添加下划线连接。  
  <span style="color: OrangeRed;">一定**不要**用数字开头！一定**不要**用数字开头！一定**不要**用数字开头！</span>
- `parameters` 是参数，通过参数向函数传入变量。  
  要注意的是一定不要将字符`'l'`（小写字母 l），`'O'`（大写字母 O）或`'I'`（大写字母 I）用作单个字符变量名称。因为这些字母可能跟 0 和 1 混淆。`'L'`（大写字母 L）可以使用。
- `"""function’s documentation string"""` 是函数的文档字符串，用作对函数的说明。  
  用三个直双引号（`"""`）标记，可以写多行。写多行的时候，第一行用作标题，然后空一行，第三行开始写其他内容，考虑到第一行开头是“`"""`”，所以缩进按第三行（准确地说，是第一个非空行）的缩进对齐，尾部的。例如：  

  ```Python
  def function_name(parameters):
    """Title"""
    function_suite
    return [expression]
  ```

#### 4.2 加载模块语句的使用

Python 可以把任何一个 `.py` 文件当作模块进行加载，使用的语句是 `import <module_name>` 或者 `from <module_name> import <x>`。

使用 `import` 要注意这么几个问题：

1. `import` 语句的位置  
   `import` 语句一般要放在程序的开头，如果是在某个函数里使用 `import` 语句，也要
2. 啊

#### 4.3 自然语言工具包（NLTK）的使用

#### 4.4 逻辑运算符的使用

#### 4.5 汉字的匹配方法

#### 总结

------
