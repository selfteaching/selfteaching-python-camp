#输入测试文本

texten = '''
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

#输入测试文本
textcn = '''
女子从山上客栈的窗口俯视黎明前的坡道。过些时候，从年底到正月这段日子，这条坡道将会被暴风雪埋没。那时赴宴就得穿雪裤、长统胶靴，还得披斗篷，戴头巾呢。到了那时节，积雪会有丈把厚。岛村现在正下这条坡道。不过，他从路旁高高地晾晒着的尿布下面，倒是可以望见县境的山峦，上面的积雪熠熠生辉，显得格外晴朗。绿色的葱还没被雪埋掉。 
村里的孩子正在田间滑雪。 
一走进村里的街道，就听到从屋檐滴落下来的轻轻的滴水声。檐前的小冰柱闪着可爱的亮光。 
一个从浴池回来的女人，仰头望着在屋顶扫雪的汉子说： 
“喂，请你顺便扫一扫我们的屋顶好吗？” 
女人感到有点晃眼，用湿手巾揩了揩额头。她大概是个女侍，趁着滑雪季节早早赶来的。隔壁是一家茶馆，玻璃窗上的彩色画已经陈旧不堪，屋顶也倾斜了。 
一般人家的屋顶都葺上细木板，铺上石子。那些圆圆的石子，只有阳光照到的一面，在雪中露出黑糊糊的表层。那不是潮湿的颜色，而是久经风雪剥蚀，像墨一般黑，一排排低矮的房子静静地伏卧在大地上，给人这样的感觉：家家户户好像那些石子一样。真是一派北国的风光。 
一群孩子将小沟里的冰块抱起来扔在路上，嬉戏打闹。大概是冰块碎裂飞溅起来的时候发出闪光非常有趣吧。站在阳光底下，觉得那些冰块厚得令人难以置信。岛村看了好一阵子。 
一个十三四岁的少女独自靠在石墙上打毛线。她穿着雪裤，还穿着高齿木屐，却没有穿袜子，可以看得见在冻红的赤脚板上长着冻疮。旁边的柴堆上坐着一个约莫三岁的小女孩，心不在焉地拿着毛线团。一根从小女孩这边牵到大女孩那边的灰色旧毛线，发出柔和的光。 
从相隔七八家的一所滑雪板工厂传来刨木的声音。另一边的屋檐下，有五六个艺伎站着聊天。那个女子可能也站在那里。直到今晨，岛村才从客栈女侍那里打听到她的艺名叫驹子。果然，女子一本正经地瞧着他走过来。女子必定满脸通红，佯装若无其事的样子。岛村还没这么想，驹子已经连脖子都涨红了。她本可以背过脸去，却窘得垂下了视线，而且，当他走近时，她慢慢地把脸移向他那边去。 
岛村感到自己的脸颊好像也在发烧，正要疾步走过去，驹子却立刻追赶上来。 
“到这种地方，真难为情啊！” 
“要说难为情，我才难为情呢！你们那么一大堆人，吓得我不敢走过去。你们经常这样吗？” 
“是啊，吃过了午饭常常是这样。” 
“你这样红着脸，嘎达嘎达地追上来，不是更难为情吗？” 
“那倒无所谓。” 
驹子断然说过之后，脸颊又飞红起来，就地停下脚步，攀住路旁的柿子树。
'''

#定义函数
def stats_text_en(text):
    """This is for the article written in English
    """
    if type(text) != str:
        raise ValueError('This is a wrong type')
    else:  #以下是英文词频统计
        t1 = text.split()
        from collections import Counter
        res = Counter(t1)
        d = dict(res)
        d2 = sorted(d.items(),key=lambda a: a[1],reverse=True)
    return d2

#以下是中文词频统计
# #定义函数
def stats_text_cn(text):
    """This is for the article written in Chinese
    """
    if type(text) != str:
        raise ValueError('This is a wrong type')
    else:
        t1 = text.replace(',',' ').replace('/"',' ').replace(':',' ')
        d1 ={}
        for i in t1:
            if u'\u4e00'<= i <= u'\u9fff':  #正则表达式匹配中文，这个应该可以拓展到不同语言了
                d1 .setdefault(i,t1.count(i))
        d2 = sorted(d1.items(),key=lambda a: a[1],reverse=True)
    return d2


#day7的作业，生成模块
#定义函数
def stats_text(text):
    """for both English & Chinese
    """
    if type(text) != str:
        raise ValueError('This is a wrong type')
    return stats_text_cn(text),stats_text_en(text)