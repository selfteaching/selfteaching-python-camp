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

不知道是对是错，不管它是对是错 
我只想和你在一起，一起等太阳出来 
没有水，你是我的水 
没有粮食，我是你的粮食 
我们自始至终相信同一个神 
热爱同一个命运 
因为啊，爱上你 
我身体中有世上最柔软的部分 
我无法想象，你起伏的身体 
是怎样的一个神秘国度 
我爬遍你的全身，像个孩子 
你新鲜、温暖而美丽 
当你的呼吸在我的鼻孔 
我的手在你的发间 
你问：你好吗？ 
我说：我想你。 
'''

from mymodule import stats_word
print('合并词频统计结果： ', stats_word.stats_text(text))