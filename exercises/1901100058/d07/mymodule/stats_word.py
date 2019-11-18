# 1. 封装统计英⽂单词词频的函数

def stats_text_en(text):    
    words=text.split()
    final_words=[]
    symbols=',.*-!'
    for word in words:
        for symbol in symbols:
            word=word.replace(symbol,'')
        if len(word) and word.isascii():
            final_words.append(word)

    counter={}
    word_set=set(final_words)
    for word in word_set:
        counter[word]=final_words.count(word)
    return sorted(counter.items(), key=lambda x:x[1], reverse=True)

# 2 封装统计中⽂汉字字频的函数

def stats_text_cn(text):    
    # words=text.split()
    final_words=[]
    for word in text:
        # unicode的中文字符范围
        if '\u4e00' <= word <= '\u9fff':
            final_words.append(word)
            
    counter={}
    word_set=set(final_words)
    for word in word_set:
        counter[word]=final_words.count(word)
    return sorted(counter.items(), key=lambda x:x[1], reverse=True)



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
There should be one-- and preferably only one --obvious way to do
it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''


text_cn = '''
我猜，作为一个普通人，你肯定不止一次听过一个令人心惊胆颤的词汇：阶层固化。
无论阶层固化是否真的已经存在，无论它是否真的正在逐步形成，它都肯定是令普通人一听就心头一紧的词汇。我不知道别人是怎样的感觉，反正我清楚地记得年轻的自己第一次听到这个词汇的时候那种接下来很久都忧心忡忡的感觉 —— 那不是恐惧，那好像是绝望。
这个词汇是全球很多人的焦虑来源。不是你一个人害怕它，更不是你一个人对它无可奈何。或早或晚，你会得知韩国人和日本人早就接受了他们的社会已然阶层固化的现状，你也会听说连有着各不相同的美国梦的美国人都在不同程度上体会到了阶层固化的正在形成，国内的自媒体就更不用提了，他们喜欢死了这种天然不经修饰就可以引发绝大多数人焦虑的标题…… 讲述这个词汇的文章，无一不是忧心忡忡，无一不是无可奈何，无一不是絮絮叨叨之后毫无任何可行解决方案。
这本书要讲的是普通人摆脱阶层固化的路径 —— 绝对可行，毫无水分，并且全靠你自己。这里所说的普通人，不分国界、不分地域、不分种族、不分性别、不分年龄、不分高矮胖瘦美丑、不分何种性取向…… 关键在于，甚至压根不分智商和学历！换言之，这个解决方案，甚至对在北京跑腿送外卖的小哥都适用……

'''

def stats_text(text):
    #合并英文和中文词频的结果
    return stats_text_en(text) + stats_text_cn(text)



if __name__ == '__main__':
    text_en_results=stats_text_en(text_en)
    print('英⽂单词词频 \n', text_en_results)

    text_cn_results=stats_text_cn(text_cn)
    print('中⽂单词词频 \n', text_cn_results)






 