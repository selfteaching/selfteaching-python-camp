#!/usr/bin/python3
# Filename: main.py
string1 = '''The Zen of Python, by Tim Peters
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
安徽，简称“皖”，是中华人民共和国省级行政区。省会合肥。
位于中国华东，安徽界于东经114°54′-119°37′，北纬29°41′-34°38′之间，东连江苏、浙江，西接河南、湖北， 南邻江西，北靠山东，安徽省总面积14.01万平方千米。
安徽省居中靠东，沿江通海，有八百里的沿江城市群和皖江经济带，内拥长江水道，外承沿海地区经济辐射。地势由平原、丘陵、山地构成；地跨淮河、长江、钱塘江三大水系。
安徽省地处暖温带与亚热带过渡地区。淮河以北属暖温带半湿润季风气候，淮河以南为亚热带湿润季风气候。
安徽省是长三角的重要组成部分，处于全国经济发展的战略要冲和国内几大经济板块的对接地带，经济、文化和长江三角洲其他地区有着历史和天然的联系。
安徽文化发展源远流长，由徽州文化、淮河文化、皖江文化、庐州文化四个文化圈组成。截至2017年底，安徽省下辖16个省辖市，7个县级市，54个县，44个市辖区。
截至2018年末，安徽省常住人口6323.6万人，实现地区生产总值30006.8亿元，第一产业增加值2638亿元；第二产业增加值13842.1亿元；第三产业增加值13526.7亿元.
安徽省平原、台地（岗地）、丘陵、山地等类型齐全，可将全省分成淮河平原区、江淮台地丘陵区、皖西丘陵山地区、沿江平原区、皖南丘陵山地五个地貌区，
分别占全省面积的30.48%、17.56%、9.99%、24.91%和16.70%。安徽有天目－白际、黄山和九华山，三大山脉之间为新安江、水阳江、青弋江谷地，地势由山地核心向谷地渐次下降，
分别由中山、低山、丘陵、台地和平原组成层状地貌格局。山地多呈北东向和近东西向展布，其中最高峰为黄山莲花峰海拔1873米。山间大小盆地镶嵌其间，其中以休歙盆地为最大。''' 
 

import stats_word

try:
    stats = stats_word.stats_text_cn(string1)
except ValueError:
    print("ValueError: You have an input that is not a string.")
else:
    print(stats)

try:
    stats = stats_word.stats_text_en(string1)
except ValueError:
    print("ValueError: You have an input that is not a string.")
else:
    print(stats)
