def stats_text_en():    # 创建函数
    """Count the english words in the text"""    # 注释
    import d5_exercise_stats_text    # 封装




# 参考宋同学的范本
text = '''                       
The Zen of Python, by Tim Peters
美丽 is better than 丑陋.
清楚 is better than 含糊.
简单 is better than 复杂.
复杂 is better than 难懂.
单一 is better than 嵌套.
稀疏 is better than 稠密.
可读性计数.
Special cases aren't special enough to 打破规则.
即使练习会使得不再纯粹.
但错误不应该用沉默来掩盖.
Unless explicitly silenced.
面对起义，拒绝猜的诱惑.
有且只有一个办法.
Although that way may not be obvious at first unless you're Dutch.
尝试总比从未试过要强.
Although never is often better than *right* now.
如果执行很难被解释，那将是一个很糟的想法.
如果执行很容易解释，这会是一个好点子.
Namespaces are one honking great idea -- 让我们继续为之努力!
'''

countcn={}    # 初始化一个词典

def stats_text_cn(checkcn):    # 定义检索中文函数
    """Count the chinese in the text"""    # 注释
    for i in checkcn:
        if u'\u4e00' <= i <= u'\u9fff':    # 中文字符的正则表达式
            countcn[i] = checkcn.count(i)
    return countcn
    
stats_text_cn(text)    #调用函数

countcn = sorted(countcn.items(), key=lambda item:item[1], reverse=True)    # 方便阅读美观排序
        
print(countcn)     # 输出