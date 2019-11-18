print('hello world')

from mymodule import stats_word
import logging
import jieba
import requests
import pyquery
from wxpy import *
import numpy
import matplotlib.pyplot as plt
from os import path


# 获取当前工作目录
cwd = path.abspath(path.dirname(__file__))
print(cwd)
# image_path=path.join(cwd,'stats.png')


# 定义提取微信公众号正文的函数
def get_article(url):
    r = requests.get(url)
    print(r)
    t =r.text
    #print(t)
    d = pyquery.PyQuery(t)
    #print(d)
    article = d('#js_content').text()
    # print(article )
    return article




def generate_image(data,image_path):
    labels = [i[0] for i in data]
    height = [i[1] for i in data]

    ypos = range(len(data))
    print(ypos)


    plt.rcdefaults()
    fig,ax = plt.subplots()

    # 设置中文字体
    plt.rcParams['font.sans-serif']='SimHei'
    plt.rcParams["axes.unicode_minus"]=False
    
    # 设置坐标轴的样式 ax
    ax.barh(ypos,height)
    ax.set_yticks(ypos)
    ax.set_yticklabels(labels)
    ax.invert_yaxis()
    ax.set_ylabel('关键字')
    ax.set_xlabel('词频')
    ax.set_title('统计词频')

    # 打印当前工作目录
    print(cwd)
    # 将图片保存在当前工作目录下的stats.png文件
    print(image_path)
    fig.savefig(image_path,bbox_inches='tight')

    #plt.show()


# 定义测试程序 
def test():
    article=get_article('https://mp.weixin.qq.com/s?__biz=MzIzMjIxNTc5Nw==&mid=2247517818&idx=6&sn=40ed31d7bcc5ec8c5a444952717cac5e&chksm=e89a83e0dfed0af6daf09a991d546285d2316fa65fcc0bd36e2d300fbf20a51c8064f9cfa740&mpshare=1&scene=23&srcid=0916IRTHO2F9mJnLhcQc2hb9&sharer_sharetime=1568611270839&sharer_shareid=ce38eb1d8a5991abab91df065c7e5d64#rd')
    result = stats_word.stats_text_cn(article,20)
    image_path=path.join(cwd,'stats.png')
    generate_image(result,image_path)


# 定义主程序
def main():
    # 导入模块
    # 初始化机器人，扫码登陆
    bot = Bot()
    friends = bot.friends()

    @bot.register(friends,SHARING)
    def handler(msg):
        try:
            logging.info('sharing url = %s',msg.url)

            #调用自定义函数get_article()
            article=get_article(msg.url)
            #调用from mymodule import stats_word
            result = stats_word.stats_text_cn(article,20)

            #调用自定义函数generate_image()
            image_path=path.join(cwd,'stats.jpg')
            generate_image(result,image_path)

            msg.reply_image(image_path)
        except Exception as e:
            #抛出错误
            logging.exception(e)

    # 进入 Python 命令行、让程序保持运行
    embed()


if __name__ == "__main__":
    #test()
    main()