#统计封装英文单词词频的函数，接受字符串，词频降序排列数组

def stats_text_en(text): #定义函数
     x=text.replace('.','').replace('!','').replace(',','') #去掉标点符号
     y=x.split() #将字符串转换成列表
     import collections #导入collections模块
     m=collections.Counter(y) #counter是dict子类，是个集合，计算存储为值
     return(m) #此函数所定义所嵌套的代码
a='The Zen of Python,by Tim Peters, Beautiful is better than ugly. Simple is better than complex!' 
print(stats_text_en(a))


#统计封装中文汉字字频的函数

def stats_text_cn(text): #定义函数
    x=text.replace('，','').replace('。','').replace('-','') #去掉标点符号
    y=x.split() #将字符串转换为列表
    import collections # collections 提供了可变类型序列
    m=collections.Counter(y) #counter 是一个计数器，方便计数，元素像字典键（key）一样存储，计数器对象是字典
    return(m)
a='信 息 高 速 公 路 的 崛 起， 知 识 经 济 的 到 来， 虚 拟 现 实 的 出 现， 人 们 才 意 识 到 他 是 对 的， 他 所 谓 的 意 识 延 伸 就 是 赛 博 空 间， 地 球 村 真 的 已 经 到 来！'
print(stats_text_cn(a))