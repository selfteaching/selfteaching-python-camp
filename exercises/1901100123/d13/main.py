from os import path
import requests
import pyquery
import matplotlib.pyplot as plt
import logging
from wxpy import *
from mymodule import stats_word
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple matplotlib numpy


cwd=path.abspath(path.dirname(__file__))  #获取当前文件所在的文件夹
plt.rcParams['font.sans-serif'] ='SimHei'  #设置中文字体

logging.basicConfig(format='file:%(filename)s|line:%(lineno)d|message:%(message)s',level=logging.DEBUG)  #初始化 logging
  

def get_article(url):
    r=requests.get(url)  #request 请求提取网页正文
    document = pyquery.PyQuery(r.text)     # pyquery 提取正文
    return document('#js_content').text()    # 提取微信公众号正文伪代码

    #生成图片
def generate_image(data,image_path): #data是定义的函数中的参数 也是用
    labels=[v[0]for v in data]  #必须是中括号！！
    widths=[v[1] for v in data]
    ypos=range(len(data))  #获取y轴上 会出现的元素
    fig,ax=plt.subplots()  #初始化一个图表
    ax.barh(ypos,widths)  #初始化一个横向的图标
    ax.set_yticks(ypos)  #设置y坐标
    ax.set_yticklabels(labels)  #设置y坐标上的标签
    ax.invert_yaxis()   # invert 表示默认设置 从小到大
    ax.set_ylabel('关键字')  #设置y轴标签
    ax.set_xlabel('词频')
    ax.set_title('词频统计')
    fig.savefig(image_path,bbox_inches='tight')  #保存生成的图片


def main():   #main函数
    bot = Bot()  # 初始化 用bot函数
    friends= bot.friends()  #接收所有朋友发给我的信息

    @bot.register(friends, SHARING)  #装饰器？  register函数, 每当收到朋友分享的信息，就会处理
    def handler(msg):   
        try:    # try-except  做一个包围，捕获可能的异常 和  logging+exception 捕获异常
            logging.info('sharing url = %s',msg.url)  #此处 表示 打印分享的url
            article = get_article(msg.url)   #获取正文
            result=stats_word.stats_text_cn(article,20)  #分词
            image_path=path.join(cwd,'stats.png')
            generate_image(result,image_path)
            msg.reply_image(image_path)  #用调用reply的方法，回复刚才分词统计的结果，结果转换为str类型
        except Exception as e:
            logging.exception(e)

    embed()  # 调用embed的方法，让程序不直接退出，一直运行程序。而不会因为发生了一次就停止了程序

def test():
    article=get_article('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
    result=stats_word.stats_text_cn(article,20)
    image_path=path.join(cwd,'stats.png')
    generate_image(result,image_path)



if __name__ == "__main__":
    main()
    #test()
