import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

#设置中文字体
cnfont = fm.FontProperties(fname='/Users/Lidong/Library/Fonts/SimHei.ttf')

#定义绘制图表函数并制作为图片
def chartImg(data={}):
    group_x = list(data.values())
    group_y = list(data.keys())
    fig, ax = plt.subplots()


    plt.title('词频统计表',color='black',fontproperties = cnfont,fontsize = 16)
    ax.set_xlabel('出现次数',fontproperties = cnfont, color = 'grey')
    ax.set_ylabel('词',fontproperties = cnfont, color = 'grey')

    '''图表样式'''
    ax.set_yticklabels(group_y,fontproperties = cnfont)
    ax.barh(group_y,group_x)
    # 保存绘制文件
    plt.savefig('chart.png')
    return 'chart.png'