text_en = '''
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

 
from  collections import Counter
	
def stats_text_en(text_en,count):
        if not isinstance(text_en,str):
                raise ValueError('This is not str')
        n = text_en.replace(',','').replace('.','').replace('\n','').replace('*','')\
        .replace('!','').replace('--','')#删除掉无用的符号
        cnt=Counter()
        my_list=''
        for s in n:
                if s.isascii():
                        my_list+=s
        n=my_list.lower()
        n=n.split()
        for word in n:
                cnt[word] +=1
        return Counter(cnt).most_common(count)
   

text_cn='''关于996，现在这是国内的一个很热门的话题，很多企业都有这个问题。我个人认为，能做996是一种巨大的福气，很多公司、很多人想996都没有机会。如果你年轻的时候不996，你什么时候可以996？
你一辈子没有996，你觉得你就很骄傲了？这个世界上，我们每一个人都希望成功，都希望美好生活，都希望被尊重，我请问大家，你不付出超越别人的努力和时间，你怎么能够实现你想要的成功？
我不要说996，到今天为止，我肯定是12x12以上。这世界上996的人很多，每天工作12小时、13小时的人很多，比我们辛苦、比我们努力、比我们聪明的人很多，
并不是所有做996的人都有这个机会真正做一些有价值、有意义并且还能够有成就感的事。所以今天中国BAT这些公司能够996，我认为是我们这些人修来的福报。你去想一下没有工作的人，
你去想一下公司明天可能要关门的人，你去想想下一个季度公司的Revenue在哪里都还不知道的人，你去想想你做了很多努力的程序根本没有人用的人……跟他们比，直到今天，我依然这么觉得，
我很幸运，我没有后悔12x12，我从没有改变过自己这一点。现在很多照片讲当年马云站边位，现在变C位。我在大学已经是学生会主席和杭州市学联主席。你们去看那些照片，我在那个角落位置的时候，
人都是我带出去的，我是他们的大头目。我为什么是大头目？因为我付出的时间比他们多。我除了上课考试以外，做学生会工作花的时间比任何人都多，去学会怎么服务别人，学会怎么样去建立同学之间的关系，
让同学们能够在学校里面做得好一点。只有你付出巨大的代价，有一天才有可能有回报，你不付代价，你是不可能有回报的。
再一个，阿里巴巴是一家什么样的公司？阿里巴巴“让天下没有难做的生意”，这是我们的使命，我们公司很辛苦，我们没有骗过大家，我们没有跟大家讲过公司很舒服。
你以为“让天下没有难做的生意”是忽悠你们？我们是真这么干的。
今天我们拥有这么多资源，我们带着巨大的使命，希望在未来能够让天下没有难做的生意，你不付出可以吗？不可以。所以我们说，加入阿里，你要做好准备一天12个小时，
否则你来阿里干什么？我们不缺8小时上班很舒服的人。今天我们要招一些8小时上班，每天坐在一个好的办公室，条件很好，食堂也不错，出去荣誉感也不错，这样的人满大街能找到。
但是我们需要的是什么？我们问你来这个公司到底想做什么？是改变自己、帮助别人、实现使命。
阿里早年也加班，但是我们加什么班？加学习的班，我们8小时工作以后，最主要晚上是复盘、学习。我们今天做错了什么、什么事情应该修复，我们应该互相怎么学习。
我们8小时以外的两个小时、三个小时是学习、提升，而不是去加班。
我希望阿里人热爱你做的工作，如果你不热爱，哪怕8个小时你都嫌很长，如果你热爱，其实12个小时不算太长。
如果你8个小时工作都不快乐，你做的这个事情就没有意义，你也不舒服。你干吗呢，8小时不知道干嘛，没有意义，所以即使你不996，你也不知道干嘛。
这就是生活，你选择了一个中国今天排名第一的公司，第一是要付出代价的。中国最少有五千万家企业，你不选其他的，选择了这家公司，这个当然不一样了。
我昨天回到家1点钟了。为什么？我自己选择的路，没有什么抱怨，不抱怨，这是我的选择。大家来了阿里，既然选择了，与其让自己痛苦，不如你的996做得更舒服一点，你工作十年，可以抵人家工作二十年，就这么回事。
加入阿里巴巴，我们到底给人家带去的是什么，回报是什么？这是我这段时间想得最多的。
我认为到阿里来不是为了高工资，不是因为有股票，不是因为我们有很好的工作环境，不是因为年终奖，不是因为这些东西。这些很重要，我们都是上有老、下有小，都有老婆孩子，我们必须照顾他们。
如果你这个家都不能照顾好，不能给他们美好的生活、良好的教育，照顾父母的身体健康，那就是错误的生活。但是我最希望考虑的，是你在阿里待十年，我们怎么样把你变成一个不同的人。
一年内发生变化，三年内发生变化，你回去，你爸妈发现这个孩子变了，你老婆发现我老公怎么变得有理想了、变得有想法了、变得开始专注工作了，你的孩子觉得爸爸妈妈跟人家就是不一样。
这是我们所希望的阿里人个人的成长，这个成长不是职位做得多大，而是你对问题的看法，你遇上困难的态度，你对人生的态度。
所有加入阿里的人，三年以后就不一样，五年以后就不一样。十年以后的阿里人，去任何地方，我们都放心。我们肯定要练出这个本事，但是这十年你要练出来，那就是要付出超越常人的代价。
否则你来干什么？我把这些也说得很透，有点难听，但是就这么一个道理。我们不忽悠大家，哎呀来吧，条件很好，我们现在不需要忽悠，以前也没有忽悠，今天根本不需要忽悠了。
我今天这么觉得，阿里巴巴做了不起的事情。我们做的事情，能够对社会有真正的价值，让老百姓买到更好的东西，享受美好的生活。
商业是最大的公益，创造就业、创造税收，没有商业的税收，没有经济的发展，哪来的高铁、哪来的高速公路？我们为社会的进步做了贡献，我们让阿里的每个人成长，我们创造了无数的就业。
阿里有福报，我们这些人解决了自己的温饱，有自己很好的收入，自己的公司不用太担心盈利，我们还可以为别人去干点事，这是很大的福气。
其实公益是帮自己，慈善可能是帮别人为主。我自己确实深以为傲，我们今天很多阿里巴巴的人，只是很多人没有公开，他们都有做很多的公益，我也特别希望所有的阿里人，
你要么参加整个阿里巴巴集团内部无数的公益组织，要么参加阿里巴巴的公益基金会。
很多人只是想给爸爸妈妈买一个车、买个房，这很重要，但是我想你们应该有这个理想，在阿里的工作10年、15年，有一天可以建立一个自己的公益基金，
可以做一些愿意做的事情，能够帮助你的孩子更有福报，帮助你自己有福报，不是一件很好的事情吗？这就需要996。
'''
def stats_text_cn(text_cn,count):
        if not isinstance(text_cn,str):
                raise ValueError('This is not str')
        cnt=Counter()
        for i in text_cn:
                if u'\u4e00'<=i<=u'\u9fff':
                        cnt[i]+=1
        
        return Counter(cnt).most_common(count)


#day7，生成模块
#定义函数
def stats_text(text,count):
        """for 	both English & Chinese
        """
        if not isinstance(text,str):
                raise ValueError('This is not str')
        print(stats_text_en(text,count))
        print(stats_text_cn(text,count))


