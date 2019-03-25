template = '''
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
def test(text):
    if not isinstance(text, str):
        raise ValueError('The parameter type is not a string')

def stats_text_en(text):
    #封装统计英文词频的函数
    import sys
    sys.path.append(r'D:\我的文档\Documents\GitHub\selfteaching-python-camp\19100103\hono355')
    import d5_exercise_stats_text
    result = d5_exercise_stats_text.sort_en_word(text)
    return result
    print('stats_text_en =>', result)
    

def stats_text_cn(text):
    #封装统计中文词频的函数
    text_cn = "".join(i for i in text if ord(i) >= 256)    #分离出文本中的中文
    text = text_cn
    for i in '*,，。.-!、？！“”""?「」':
        text = text.replace(i,'')#去掉标点等符号

    textlist = []
    for i in text:
        textlist.append(i)#将汉字一个一个分开

    word_dict = {}
    #统计各个汉字出现的次数
    for j in textlist:
        if j not in word_dict:
            word_dict[j] = 1
        else:
            word_dict[j] += 1
    
    sort_cn_word = sorted(word_dict.items(),key=lambda item:item[1],reverse=True)#按汉字出现次数降序排序
    result = sort_cn_word
    print('sort_cn_word => ', result)
    return result


def stats_text(text):
    #调用stats_text_en与stats_text_cn函数，输出合并词频统计结果
    result = stats_text_en(text) + stats_text_cn(text)
    print('stats_text => ', result)
    return result
    
def main():
    stats_text_en(template)
    stats_text_cn(template)
    stats_text(template)

if __name__ == '__main__':
    main()


