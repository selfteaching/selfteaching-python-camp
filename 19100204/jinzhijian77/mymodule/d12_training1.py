url = 'https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA'
def stats(url):
    import requests
    from pyquery import PyQuery
    import stats_word
    response = requests.get(url)
    document = PyQuery(response.text)
    content = document('#js_content').text()    
    count = 100
    
    contents = stats_word.stats_text(content,count)
    result = contents.__str__()
    return result



