from os import path
from mymodule import stats_word
import requests
import pyquery
import logging
from wxpy import *
import matplotlib.pyplot as plt

#获取当前路径 
cwd=path.abspath(path.dirname(__file__))
#设置中文字体
plt.rcParams['font.sans-serif']=['SimHei']
#黑体： SimHei
#微软雅黑： Microsoft YaHei
#微软正黑体： Microsoft JhengHei
#新宋体 ： NSimSun
#新细明体 ： PMingLiU
#细明体 ： MingLiU
#标楷体 ： DFKai-SB
#仿宋 ： FangSong
#楷体 ： KaiTi
#仿宋_GB2312： FangSong_GB2312
#楷体_GB2312： KaiTi_GB2312
#隶书：LiSu
#幼圆：YouYuan
#华文细黑：STXihei
#华文楷体：STKaiti
#华文宋体：STSong
#华文中宋：STZhongsong
#华文仿宋：STFangsong
#方正舒体：FZShuTi
#方正姚体：FZYaoti
#华文彩云：STCaiyun
#华文琥珀：STHupo
#华文隶书：STLiti
#华文行楷：STXingkai
#华文新魏：STXinwei
logging.basicConfig(format='file:%(filename)s|line:%(lineno)d|message:%(message)s',level=logging.DEBUG)

# 提取微信公众号正⽂
def get_article(url):
    r = requests.get(url)
    document = pyquery.PyQuery(r.text)
    return document('#js_content').text()

#生成图片
def generate_image(data,image_path):
    labels=[v[0] for v in data]#列表推倒式，取 data 列表里每个元素的 第一个值 和 第二个值[48,49行]
    widths=[v[1]for v in data]
    ypos=range(len(data))#在给定的间隔返回均匀间隔的值
    fig,ax=plt.subplots()#绘制图片
    ax.barh(ypos,widths)#绘制二维水平直方图
    ax.set_yticks(ypos)
    ax.set_yticklabels(labels)
    ax.invert_yaxis()  #labels read top-to-bottom
    ax.set_ylabel('关键字')
    ax.set_xlabel('词频')
    ax.set_title('词频统计')
    fig.savefig(image_path,bbox_inches='tight')
    

def main():
    bot=Bot()
    friends = bot.friends()

    @bot.register(friends,SHARING)
    def handler(msg):    
        try:        
            logging.info('sharing url - %s',msg.url)
            article=get_article(msg.url)
            result=stats_word.stats_text_cn(article,20)
            image_path=path.join(cwd,'stats.png')
            generate_image(result,image_path)#生成图片
            msg.reply_image(image_path)
        except Exception as e:
            logging.exception(e)
    embed()

def test():
    article=get_article('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
    result=stats_word.stats_text_cn(article,100)
    image_path=path.join(cwd,'stats.png')
    generate_image(result,image_path)#生成图片

if __name__ == '__main__':
    main()
    #test()



        
    




