# 1. 统计英文单词词频
# 2. 统计中文汉字字频

text = '''
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

text1 = '''
自学 Python 训练营
入门训练营
基本介绍
所谓"自学"，就是"自己一个人（默默地）学" —— 这恰恰是绝大多数人一生学习失败的最根本原因。

训练营由 "新生大学" 联合 "糖果" 发起，针对基础相对薄弱，想要自学 Python 的人组织的训练营。

训练营期间由 教研组 规划学习路线、提供学习素材，学员 通过阅读、实践、交流等方式自学为主，遇到确实无法完成的难题会有专业的 编程教练 帮助解答，辅导员 会在整个过程中鼓励、推动，帮助学员完成整个训练。
'''

# 统计英文单词词频的函数
def stats_text_en(text_en):  
    t = text_en.replace(',',' ').replace('.',' ').replace('--',' ').replace('*',' ').replace('!',' ')   
    # 将非英文字符替换为空格

    t = t.lower()   # 把大写转换为小写
    t = t.split()   # 以空格，把字符串内单词拆分为列表

    d1 = {}  # 定义字典

    for i in t :    # 循环遍历列表中的单词
        d1.setdefault(i,t.count(i))  #   返回列表中单词出现的次数

    d2 = sorted(d1.items(), key=lambda x:x[1], reverse=True)
    # 按照出现次数从大到小输出所有的单词及出现的次数,降序排列
    # key=lambda 元素: 元素[字段索引] ，此处 ，对第二个字段进行排序

    return d2 #   输出最终结果

# 统计中文汉字字频的函数
def stats_text_cn(text_cn):  
    d1 = {}  # 定义字典
    my_list = []  #定义列表

    # 清洗字符串，只保留汉字
    for s in text_cn: 
        if '\u4e00' <= s <= '\u9fff':   # 中文字符范围
            my_list.append(s)   # 把整理后的汉字，添加到列表中
          # d1[s]=text_cn.count(s) 简单的方法，统计中文汉字词频

    # 用字典统计每个汉字出现的个数     
    for char in my_list:
        if char in d1.keys():   # 判断一个汉字是否存在，keys表示（键）
            d1[char] = d1[char] + 1  # 计数
        else:
            d1[char] = 1    
                   
    d2 = sorted(d1.items(), key=lambda x:x[1], reverse=True)
    # 按照出现次数从大到小输出所有的单词及出现的次数,降序排列
    # key=lambda 元素: 元素[字段索引] ，此处 ，对第二个字段词频进行排序
    return d2 #   输出最终结果



print("* 统计英文单词词频 *")
print(stats_text_en(text))  # 输出英文单词词频

print('*'*50)

print("* 统计中文汉字字频 *")
print(stats_text_cn(text1))  # 输出中文汉字字频



