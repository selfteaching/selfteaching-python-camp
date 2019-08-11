import matplotlib.pyplot as plt
from mymodule import stats_word
import os
import requests
from pyquery import PyQuery
import getpass
import yagmail
from wxpy import *
import numpy as np



plt.rcdefaults()

def main():

    response = requests.get("https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA")
    document = PyQuery(response.text)
    content = document('#js_content').text()
    outcome = stats_word.stats_text_cn(content,10)

    word = [l[0]for l in outcome]
    nub = [l[1]for l in outcome]
    y_pos = np.arange(len(word))

    
    plt.rcParams['font.sans-serif'] = 'SimHei'
    fig, ax = plt.subplots()
    
    ax.barh(y_pos, nub, align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(word)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Number')#x轴标签
    ax.set_title('The most frequent word')#标题设定
    plt.savefig("fig1.png")


if __name__ == "__main__":
    main()