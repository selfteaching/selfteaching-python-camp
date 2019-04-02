import stats_word

import typing
import sys
import json
import os
import re,argparse,collections
import jieba

def main():  
    #test = 1111111   
    # try:
    #     stats_word.stats_text(test)
    # except ValueError as error :
    #     print('输入值：',test)
    #     print('错误信息：',error)
    #     return False
    # finally:
    #     print('请再输入！')
    # print('p',os.getcwd())
    
    #获取tang300.json的路径
    tangfile = os.getcwd()+'\\' + 'tang300.json' 
    #读取文件
    #words = re.findall(r'\w+', open(tangfile,'r',encoding='UTF-8').read().lower())
    #print(collections.Counter(words).most_common(100))
    content = open(tangfile, 'rb').read()

    tags = jieba.analyse.extract_tags(content, topK=20)

    print(",".join(tags))

if __name__ == '__main__':
    main()