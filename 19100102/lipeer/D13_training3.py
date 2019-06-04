将 matplotlib.pyplot 导入为 plt
将 matplotlib.font_manager 导入为 fm

＃设置中文字体
cnfont = fm.FontProperties（fname = '/ Users/wengyadong/Library/Fonts/SimHei.ttf '）

＃定义绘制图标函数并保存为图片
def  chartImg（data = {}）：
    group_x =  list（data.values（））
    group_y =  list（data.keys（））
    fig，ax = plt.subplots（）
    ＃自定义表格标签及标题样式
    plt.title（'词频统计表'，color = ' black '，fontproperties  = cnfont，fontsize  =  16）
    ax.set_xlabel（'数量'，fontproperties  = cnfont，color  =  ' gray '）
    ax.set_ylabel（'词语'，fontproperties  = cnfont，color  =  ' gray '）
    ＃绘制图表
    ax.set_yticklabels（group_y，fontproperties  = cnfont）
    ax.barh（group_y，group_x）
    ＃保存绘制文件
    plt.savefig（' chart.png '）
    返回 “ chart.png ”