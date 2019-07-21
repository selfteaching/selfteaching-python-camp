from collections import Counter
import jieba
import matplotlib.pyplot as plt
import requests
from pyquery import PyQuery
from matplotlib.font_manager import FontProperties
from wxpy import embed, Bot


def get_chinese_font():
    return FontProperties(fname='/System/Library/Fonts/PingFang.ttc')


def clean_ip_list(words):  # 清理掉空格 标点符号
    i = 0
    while i < len(words):
        words[i] = words[i].strip('*-.')
        if words[i] == '':  # 清洗完成之后若为空元素‘’，则删除元素
            words.remove('')
        else:
            i = i + 1
    return words


def clean_len_less_2(words):  # 去掉词语长度小于2的
    i = 0
    while i < len(words):
        if len(words[i]) < 2:
            words.remove(words[i])
        else:
            i = i + 1
    return words


def count_word(s, count):  # 定义检索中文函数
    if isinstance(s, str):
        # regex = re.compile("(?x)(?: [\w -]+ | [\x80 -\xff]{3} )")
        words = jieba.lcut(s)
        # 去除非中文词语
        words = clean_ip_list(words)
        # 去掉非中文
        words = clean_not_cn(words)
        # 去除词语长度小于2的
        words = clean_len_less_2(words)
        # 用Counter对数组按照value值排序
        words = Counter(words)
        # 找出频率最多的前count名
        words = words.most_common(count)
        print(words)
    else:
        raise ValueError("is not str")
    return words


def clean_not_cn(words):  # 去除非中文词语
    i = 0
    while i < len(words):
        b = False  # 非中文词语
        for char in words[i]:
            if char <= '\u4e00' or char >= '\u9fff':  # 如果是中文
                b = True
                break
        if b:
            words.remove(words[i])
        else:
            i = i + 1
    return words


def request_data(url):  # 获取数据
    r = requests.get(url)
    if 200 == r.status_code:
        document = PyQuery(r.text)
        result = document('#js_content').text()
        return result
    return ""


def show_plot(xs, ys):  # 显示柱状图
    plt.rcdefaults()
    fig, ax = plt.subplots()
    ax.barh(ys, xs, 0.8, align='center', color='green')
    ax.set_yticklabels(ys, fontproperties=get_chinese_font())
    ax.set_xlabel('出现次数', fontproperties=get_chinese_font())
    ax.set_title('文章前20名词频统计结果图', fontproperties=get_chinese_font())
    plt.savefig('char.png')
# plt.show()


def count_article(url, count):
    s = request_data(url)
    words = count_word(s, count)
    x_s = []
    y_s = []
    for word in words:
        x_s.append(word[1])
        y_s.append(word[0])
    show_plot(x_s, y_s)


bot = Bot()


# 消息接收监听器
@bot.register()
def print_others(msg):
    # 输出监听到的消息
    print(msg)
    if msg.type == 'Sharing':
        count_article(msg.url)


embed()

if __name__ == '__main__':
    count_article('https://mp.weixin.qq.com/s/7Z8unW7Gsu0cf1hAwvjAxw', 20)
