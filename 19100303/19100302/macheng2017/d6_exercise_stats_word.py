from collections import OrderedDict
text ='''刚搬到一座陌生的城市周围都是陌生的口音感觉自己是个「外乡人」；上大学住宿舍住不习惯开始想家；过年时回老家，一大家子围坐在一起聊得起劲，你却觉得自己格格不入没什么好说的......说到底，归属感就是个人与外界环境接触时，产生的认同和熟悉的安全感。马斯洛需求层次理论把归属感列在了第三层次，仅次于生理需求和安全需求，是人作为一个具有社会属性的动物基本的情感需求。

归属感主要来自于「身份认同」，你可以从不同的群体中找到自己对应的某个身份，从国家、民族、地域文化、学校、公司等等，小到家庭、一个群聊、粉丝饭圈......其中「家」是最基本的归属感单位，它是与生俱来的，所以最普遍、最传统的归属感来源就是家庭、家人，这也是为什么大多数时候我们遇到危难时会轻易的想要“回家”，说家是“避风港”，还会把其他有归属感的地方称作“有家的感觉”。

但现在，人们对「家」的定义正在发生改变。电影《小偷家族》提供了一种假设，几个男女老少并无血缘关系却过得像一家人，从原生家庭中跑出来孤立无援的他们为彼此提供了一个正常家庭应该有的支持和关爱。影片提出的核心问题是，当人们跟血亲的原生家庭「走丢了」的时候，「家」的归属感去哪里找。

故乡的归属感也在变弱，比如一些从小在大城市长大的「飘二代」——他们的爸妈从各自老家来到大城市打拼生活并留了下来，对他们来说，「故乡」到底是户口上的籍贯老家，还是从小长大待惯了的这座城市？'''

 
text2 = '''
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
Namespaces are one honking great idea -- let's do more of those!'''

def stats_text_cn (text):
    strList = []
    strDict = {}
    for i in text:
        strList.append(i)
    strDict = dict.fromkeys(strList, 0)
    for i in strList:
        strDict[i] = strList.count(i)
    sorted_x = dict(sorted(strDict.items(), key=lambda kv: kv[1], reverse = True))
    print(sorted_x)

def stats_text_en (text):

    strDict = {}
    strList = text.split()
    for i in range(len(strList)):
        strList[i] = strList[i].strip(',-*!.')
        # strList.append(i)
    strDict = dict.fromkeys(strList, 0)
    for i in strList:
        strDict[i] = strList.count(i)
    sorted_x = dict(sorted(strDict.items(), key=lambda kv: kv[1], reverse = True))
    print(sorted_x)

stats_text_cn(text)
stats_text_en(text2)