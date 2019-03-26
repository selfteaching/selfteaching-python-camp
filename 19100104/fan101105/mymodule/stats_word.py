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
'''处理英文文本,按照单词出现次数,输出从大到小排序结果'''
def stats_txt_en(text):#处理英文文本,按照单词出现次数,输出从大到小排序结果
    if type(text) == str:#添加字符串类型检查
        text=text.replace(',',' ').replace('.',' ').replace('--',' ').replace('!',' ').replace('*',' ') #替换所有标点符号为空格
        text=text.lower()  #统一成小写
        text=text.split()  #切割字符串
        dicta={}
        for i in text:
            count=text.count(i)
            x1={i:count}
            dicta.update(x1)
        dictb=sorted(dicta.items(),key=lambda x:x[1],reverse=True) #按照单词出现次数，从大到小排序
        print(dictb)
    else:
        raise ValueError('不是字符串，请重新输入！')

stats_txt_en(text)

text1 = '''
此开卷第一回也。作者自云：曾历过一番梦幻之后，故将真事隐去，而借
通灵说此《石头记》一书也，故曰“甄士隐”云云。但书中所记何事何人?自己又
云：“今风尘碌碌，一事无成，忽念及当日所有之女子：一一细考较去，觉其行止
见识皆出我之上。我堂堂须眉诚不若彼裙钗，我实愧则有馀，悔又无益，大无可如
何之日也。当此日，欲将已往所赖天恩祖德，锦衣纨之时，饫甘餍肥之日，背父
兄教育之恩，负师友规训之德，以致今日一技无成、半生潦倒之罪，编述一集，以
告天下；知我之负罪固多，然闺阁中历历有人，万不可因我之不肖，自护己短，一
并使其泯灭也。所以蓬牖茅椽，绳床瓦灶，并不足妨我襟怀；况那晨风夕月，阶柳
庭花，更觉得润人笔墨。我虽不学无文，又何妨用假语村言敷演出来?亦可使闺阁
昭传。复可破一时之闷，醒同人之目，不亦宜乎？”故曰“贾雨村”云云。更于篇
中间用“梦”“幻”等字，却是此书本旨，兼寓提醒阅者之意。
　　看官你道此书从何而起?说来虽近荒唐，细玩颇有趣味。却说那女娲氏炼石补
天之时，于大荒山无稽崖炼成高十二丈、见方二十四丈大的顽石三万六千五百零一
块。那娲皇只用了三万六千五百块，单单剩下一块未用，弃在青埂峰下。谁知此石
自经锻炼之后，灵性已通，自去自来，可大可小。因见众石俱得补天，独自己无才
不得入选，遂自怨自愧，日夜悲哀。一日正当嗟悼之际，俄见一僧一道远远而来，
生得骨格不凡，丰神迥异，来到这青埂峰下，席地坐谈。见着这块鲜莹明洁的石头，
且又缩成扇坠一般，甚属可爱。那僧托于掌上，笑道：“形体倒也是个灵物了，只
是没有实在的好处。须得再镌上几个字，使人人见了便知你是件奇物，然后携你到
那昌明隆盛之邦、诗礼簪缨之族、花柳繁华地、温柔富贵乡那里去走一遭。”石头
听了大喜，因问：“不知可镌何字?携到何方?望乞明示。”那僧笑道：“你且莫问，
日后自然明白。”说毕，便袖了，同那道人飘然而去，竟不知投向何方。
　　又不知过了几世几劫，因有个空空道人访道求仙，从这大荒山无稽崖青埂峰下
经过。忽见一块大石，上面字迹分明，编述历历。空空道人乃从头一看，原来是无
才补天、幻形入世，被那茫茫大士、渺渺真人携入红尘、引登彼岸的一块顽石；上
面叙着堕落之乡、投胎之处，以及家庭琐事、闺阁闲情、诗词谜语，倒还全备。只
是朝代年纪，失落无考。后面又有一偈云：
无才可去补苍天，枉入红尘若许年。
此系身前身后事，倩谁记去作奇传?
'''

'''处理文本,按照汉字出现次数,输出从大到小排序结果'''
def stats_txt_cn(text1):#处理中文文本
    if type(text1) == str:#添加字符串类型检查
        word_lst = []
        word_dict = {}
        exclude_str = "，。！？、（）【】<>《》=：+-*—“”…" 
        # 添加每一个字到列表中
        for line in text1:
            for char in line:
                word_lst.append(char)
        # 用字典统计每个字出现的个数       
        for char in word_lst:
            if char not in exclude_str:
                if char.strip() not in word_dict: # strip去除各种空白
                    word_dict[char] = 1
                else :
                    word_dict[char] += 1
        lstWords = sorted(word_dict.items(), key=lambda x:x[1],  reverse=True) 
        print(lstWords)

    else:
        raise ValueError('不是字符串，请重新输入！')    
stats_txt_cn(text1)
'''英汉合并词频统计'''

def stats_text(text):
    if type(text) == str:#添加字符串类型检查
        print(stats_txt_en(text))
        print(stats_txt_cn(text))
    else:
        raise ValueError('不是字符串，请重新输入！') 
stats_text(text)