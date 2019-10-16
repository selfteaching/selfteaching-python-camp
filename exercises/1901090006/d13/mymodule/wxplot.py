import matplotlib.pyplot as plt
import numpy as np
import os
import matplotlib as mpl

def plot(x,y):
	plt.rcdefaults()
	fig, ax = plt.subplots()

	# 添加中文字体
	plt.rcParams['font.sans-serif']=['simhei'] 
	plt.rcParams['font.family']='sans-serif'
	plt.rcParams['axes.unicode_minus'] = False

	# 绘制图表
	y_pos = np.arange(len(y))

	ax.barh(y_pos, x, align='center')
	ax.set_yticks(y_pos)
	ax.set_yticklabels(y)
	ax.invert_yaxis()  # labels read top-to-bottom
	ax.set_xlabel('Frequency')
	ax.set_title('词语统计')

	img_name = 'word_frenquency_chart.jpg'
	plt.savefig(img_name)
	img_path = os.path.abspath(img_name)

	# plt.show()

	return img_path




if __name__ == '__main__':
	word_list = [('大傻',8),('二傻',3),('三宝',5),('四眼',6)]
	x,y = [],[]
	for w in word_list:
		x.append(w[1]) # 词语y轴
		y.append(w[0]) # 频率x轴
	print(x,y)
	plot(x,y)
	# print(get_font())

