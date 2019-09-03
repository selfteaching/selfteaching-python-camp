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
text2 = '''
从明天起，做一个幸福的人
喂马、劈柴、周游世界
从明天起，关心粮食和蔬菜
我有一所房子，面朝大海，春暖花开
从明天起，和每一个亲人通信
告诉他们我的幸福
那幸福的闪电告诉我的
我将告诉每一个人
给每一条河每一座山取一个温暖的名字
陌生人，我也为你祝福
愿你有一个灿烂的前程
愿你有情人终成眷属
愿你在尘世获得幸福
我只愿面朝大海，春暖花开
'''


def stats_text_en(text):
    text = text.replace(',','').replace('.','').replace('--','').replace('*','').replace('!','')#讲非英文字符转化为空
    text = text.lower()#将所有英文字符改为小写
    text = text.split()#以空格拆分独立的单词
    dir1 = {}
    for i in text: #将字符转换为字典
        count = text.count(i)
        r1 = {i:count}
        dir1.update(r1)
    print(dir1)

    dir2 = sorted(dir1.items(),key = lambda x:x[1],reverse = True)
    print(dir2)




stats_text_en(text1)



def stats_text_cn(text):
    text = text.replace('\n','').replace('，','').replace('、','')#删掉换行符，逗号，顿号
    b1 = {} 
    for i in text: #由字符生成字典
        b1.update({i: text.count(i)})
    print(b1)

    b2 = sorted(b1.items(),key = lambda x:x[1],reverse = True)
    print(b2)


stats_text_cn(text2)
