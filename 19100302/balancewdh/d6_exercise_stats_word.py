#英文段落
text1 = '''
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
def stats_text_en(text:"英文段落")->list:
    word_list = text.replace("--", '').replace("*", '').replace('\n', ' ').split(" ")
    dict = {}
    for word in word_list[:]:
        if word == '':
            word_list.remove(word)
        elif word not in dict:
            dict[word] = 1
        else:
            dict[word] = dict.get(word) + 1
    return sorted(dict.items(),key=lambda x:x[1],reverse=True)
# 函数调用
result = stats_text_en(text1)
print(result)

#中文段落
text2 = "那天，顺路闲逛市内一个有名的花鸟市场。我被那一排五颜六色的鹦鹉吸引了。鹦鹉有着鲜艳的羽毛，而且颜色繁丰，红绿相间，美丽得令人不忍离去。“你好！”我逗着鸟儿，鸟儿睁大好奇的眼睛看着我，对我的问话没有回应。“你吃了吗？”我又用一句中国国礼问道。鸟儿只是唧唧叫着，在笼子里上下蹦跳。我问卖鸟的大爷，这鸟怎么不说话？大爷笑笑，说，这得经过调教才能学会。我问，容易教吗？大爷说，鹦鹉喜欢学人话，需多次反复，耐心教，就会。我很想买一只回去试试，可又怕伺候不好，鸟没有教会说人话，人却学成了说鸟话。还是放放，先了解了解，做做功课，找个养过鹦鹉的人拜师，见识见识，再买也不迟。"
def stats_text_cn(text:"中文段落")->list:
    char_list=[]
    for c in text:
        if c in ('“', '”', '。', '!', '？', '一', '，', '！'):
            continue
        else:
            count = text.count(c)
            char_list.append((c, count))
    char_list =list(set(char_list))
    char_list.sort(key=lambda x:x[1], reverse=True)
    return char_list
# 函数调用
result = stats_text_cn(text2)
print(result)