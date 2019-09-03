# this script is to install and use the Other Library
import stats_word as s
import requests
from pyquery import PyQuery as pq
import yagmail

if __name__ == "__main__":
    # get the text online
    response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
    document = pq(response.text)
    content = document('#js_content').text()

    try:
        result = s.stats_text(content)[0].most_common(100)
        text_out = ''
        for key in result:
            # print(key[0])
            text_out += ' ' + key[0]
        # print(text_out)
    except Exception as e:
        print(e)
    
    # use email to send the result
    username = 'tsuishihhao@163.com'
    passwd = '######'
    mail = yagmail.SMTP(
        user = username,
        password = passwd,
        host = 'smtp.163.com',
        smtp_ssl = True)#
    mail.send(
        # to='pythoncamp@163.com',# use list if more than one receiver
        to='tsuishihhao@163.com',
        subject='自学训练营 7群 ShihaoCui',
        contents = text_out)
    print('发送成功')