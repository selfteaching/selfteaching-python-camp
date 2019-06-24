import sys, os

import stats_word

import requests

from pyquery import PyQuery

# 下载微信公众号文章
def download_article(url):

	# 下载微信公众号文章
	response = requests.get(url)

	assert response.status_code == 200, 'error: cant download article'

	# 解析文章，提取正文
	document = PyQuery(response.text)
	content = document('#js_content').text()
	
	return content