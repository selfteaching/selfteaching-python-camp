import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import wordcloud as wc

# 读取训练营期间笔记内容
text = open('readme.txt').read()
bgmask = np.array(Image.open('2.png'))
# 定义云图
wordcloud = wc.WordCloud(width=800,height=300,background_color='white', max_words=500, mask=bgmask, contour_width=3, contour_color='steelblue')
wordcloud.generate(text)
# 绘制云图
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
wordcloud.to_file('d14.png')
#plt.show()
#plt.savefig('d14.png',wid)
