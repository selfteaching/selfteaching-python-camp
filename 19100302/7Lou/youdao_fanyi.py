import urllib.request
import urllib.parse
import json
import time

def youdao_fanyi():
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    while True:
        content = input("请输入需要翻译的内容：")
        if content == 'q':
            break
        data = {}
        data['i'] = content
        data['from'] = 'AUTO'
        data['to'] = 'AUTO'
        data['smartresult'] = 'dict'
        data['client'] = 'fanyideskweb'
        data['salt'] = '15561241890699'
        data['sign'] = '18494ade5b9d7bddbb15a1e29e5c1ac6'
        data['ts'] = '1556124189069'
        data['bv'] = '437dabe515ba618717ad5e0ed813383c'
        data['doctype'] = 'json'
        data['version'] = 2.1
        data['keyfrom'] = 'fanyi.web'
        data['action'] = 'FY_BY_CLICKBUTTION'
        data = urllib.parse.urlencode(data).encode('utf - 8')

        req = urllib.request.Request(url,data)#修改User-Agent
        req.add_header('Referer','http://fanyi.youdao.com/?keyfrom=dict2.index')
        req.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36')

        response = urllib.request.urlopen(url,data)
        html = response.read().decode('utf - 8')
        json.loads(html)
        target = json.loads(html)
    
        print("翻译结果：{}" .format((target["translateResult"][0][0]['tgt'])))
        time.sleep(5)

