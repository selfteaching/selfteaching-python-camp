url = 'https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA'

def stats(url):
        import requests
        from pyquery import PyQuery
        import stats_word
        response = requests.get(url)
        document = PyQuery (response.text)
        content = document ('#js_content').text() 
        contents = stats_word.stats_text_cn(content)
        result = contents.__str__()
        return result
