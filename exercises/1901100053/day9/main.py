from mymodule import stats_word
from os import path
import json #ʹ�� json ����ṹ������
import re
import logging


logging.basicConfig(format='file:%(filename)s|line:%(lineno)d|message:%(message)s',level=logging.DEBUG)


def load_file(): 
    '''
    1.
    �����ǳ��õĻ�ȡ�ļ�·���ķ�ʽ��Ҫȷ��tang300.json����ǰ�ļ���ͬһ�ļ����£������ַ�ʽ�ȼ�
    file_path=path.join(path.dirname(path.abspath(__file__)),'./tang300.json')
    '''

    file_path=path.join(path.dirname(path.abspath(__file__)),'tang300.json')#ȷ��tang300.json�뵱ǰ�ļ���ͬһ�ļ���
    print('��ǰ�ļ�·����',__file__,'\n��ȡ�ļ�·��',file_path)
    '''
     2.
    ���ַ�ʽ��ʾtang300.json�ڵ�ǰ�ļ�����һ��Ŀ¼
    file_path=path.join(path.dirname(path.abspath(__file__)),'../tang300.json')
    print(__file__,file_path)

    3.
    ���ַ�ʽ��ʾtang300.json�ڵ�ǰ�ļ�����һ��Ŀ¼��data�ļ�����
    file_path=path.join(path.dirname(path.abspath(__file__)),'../data/tang300.json')
    print(__file__,file_path)
    '''

    with open(file_path,'r',encoding='utf-8')as f:
        return f.read()





def merge_poems(data):
    poems=''
    for item in data:
        poems+=item.get('contents','')
    return poems



def main():
    try:        
        data=load_file()
        logging.info(data[0])
        poems=merge_poems(json.loads(data))
        logging.info('result==> %s ',stats_word.stats_text_cn(poems,100))
    except Exception as e:
        logging.exception(e)



if __name__ == '__main__':
    main()