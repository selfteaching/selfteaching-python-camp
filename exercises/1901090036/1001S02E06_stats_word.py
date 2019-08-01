#！/usr/bin/python
#-*-coding:UTF-8 -*-
#统计封装英文单词词频的函数，接受字符串，词频降序排列数组
import collections #导入collections模块，用于计数
import re #引入正则表达式，以便操作字串符，import放在最上方

def stats_text_en(text): #定义函数
     pattern=re.compile("[A-Z]*[a-z]+")
     x=text.replace('.','').replace('!','').replace(',','') #去掉标点符号
     y=x.split() #将字符串转换成列表
     m=collections.Counter(y) #counter是dict子类，是个集合，计算存储为值
     return(m) #此函数所定义所嵌套的代码
a='The Zen of Python,by Tim Peters, Beautiful is better than ugly. Simple is better than complex!Complex is better than complicated,Flat is better than nested.Readability counts.Now is better than never.' 
print(stats_text_en(a))


#统计封装中文汉字字频的函数

def stats_text_cn(text): #定义函数
     pattern1=re.compile("[\u4E00-\u9FA5]")
     for y in text:
          y=text.split()
     m=collections.Counter(y)
     return(m)
a='信 息 高 速 公 路 的 崛 起， 知 识 经 济 的 到 来， 虚 拟 现 实 的 出 现， 人 们 才 意 识 到 他 是 对 的， 他 所 谓 的 意 识 延 伸 就 是 赛 博 空 间， 地 球 村 真 的 已 经 到 来！媒 体 是 人 体 的 延 伸，媒 体 就 是 信 息，媒 体 有 冷 热 之 分，强 调 获 得 讯 息 的 方 式 比 讯 息 内 容 本 身 更 来 得 重 要，更 有 影 响 力。并 提 出 传 播 科 技 不 仅 可 以 引 起 人 类 感 官 能 力 变 化 更 可 以 促 进 社 会 结  构 的 变 化 ，引 发 对 于 媒 介 科 技 的 研 究'
print(stats_text_cn(a))