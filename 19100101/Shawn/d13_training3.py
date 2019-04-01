import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

cnfont = fm.FontProperties(fname='/Users/Library/Fonts/s.ttf')


def chartImg(data={}) :
    group_x = list(data.values())
    group_y = list(data.keys())
    fig, ax = plt.subplots()
    # 自定义表格标签及标题样式
    plt.title('词频统计表',color='black',fontproperties = cnfont,fontsize = 16)
    ax.set_xlabel('数量',fontproperties = cnfont, color = 'grey')
    ax.set_ylabel('词语',fontproperties = cnfont, color = 'grey')
    # 绘制图表
    ax.set_yticklabels(group_y,fontproperties = cnfont)
    ax.barh(group_y,group_x)
 
    plt.savefig('chart.png')
    return 'chart.png'