import re
from collections import Counter

def stats_text_en(text):
    if isinstance(text, str):    
        list1 = []    
        text_list = re.split(r'[\s,.!\-*]', text)
        for i in text_list:        
            if not u'\u4e00' <= i <= u'\u9fff': 
                list1.append(i)
        return Counter(list1).most_common()    
    else:
        raise ValueError("This is not a string!")


def stats_text_cn(checkstr, top_n=None):
    if isinstance(checkstr, str):
        cndic = {}
        for i in checkstr:        
            if u'\u4e00' <= i <= u'\u9fff':   
                cndic[i] = checkstr.count(i)   
        return Counter(cndic).most_common(top_n)
    else:
        raise ValueError("This is not a string!")


def stats_text(text_an):
    if isinstance(text_an, str):
        str1 = {}
        str1["en"] =stats_text_en(text_an)
        print("""---以下是英文字符输出结果---""")
        print(str1["en"])
        str1["cn"] =stats_text_cn(text_an)
        print("""---以下是中文字符输出结果---""")
        print(str1["cn"])
        return str1
    else:
        raise ValueError("This is not a string!")



text_an = '''
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


stats_text(text_an)


with open("tang300.json", 'r', encoding='utf-8') as file_object:
    contents = file_object.read()
    # print(contents)

result = stats_text_cn(contents, top_n=100)
print("""---唐诗300首中词频最高的前100个字---""")
print(result)

