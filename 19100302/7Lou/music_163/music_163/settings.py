# -*- coding: utf-8 -*-

# Scrapy settings for music_163 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'music_163'

SPIDER_MODULES = ['music_163.spiders']
NEWSPIDER_MODULE = 'music_163.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'music_163 (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'vjuids=26b22afdc.16a3ea24f07.0.cc6c505f5cc33; _ntes_nnid=73306b0e319bb73f00d3f418dce3f58a,1555828985624; ne_analysis_trace_id=1555828985635; s_n_f_l_n3=fafb1f3716aa8daf1555828985648; _ntes_nuid=73306b0e319bb73f00d3f418dce3f58a; vinfo_n_f_l_n3=fafb1f3716aa8daf.1.0.1555828985647.0.1555829310568; vjlast=1555828986.1556291737.13; _iuqxldmzr_=32; WM_TID=u82xoWEahw1BFVEURVMsjdYeDbJFchQi; WM_NI=iZpbl1tON9dPmPzcJY2ngP8TqICbZCH6s6XGfTPZaWLI8OVwDTawXDqOjRP%2F0elHAMlJ6QtWgqGQ2RaFIcw%2FRTU5UaG3N5QL9pqMdiL5rqpvm0dIlBJaaH48jFZ90G4zWDY%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eea3b67bb48782a2e765edb48eb3d84f978a8abbbc63a8919fb6eb5bfcb0a7d7f72af0fea7c3b92aab86c083ef3bb89182dae75caf90b684c953f2b2a9b1bb60b3978d83d9498ceabdd7db4da68ca0bbe45d9097f8b0d57d888caf98db50b391a6b3d325f4bba4a9c447b096fab2f75da5af89b2b15aa39a8784f625928c9bd6d86b85ed82d6d448fbb0bfaee76390ebbe92f37eaff0acaaef4a8abfafa9b734aa9a96dab34df8a699a5dc37e2a3; JSESSIONID-WYYY=10rD49ujxjvdyXtoQWhXFa6dBSAyKdt0dCeXg%2Bxax7SUc0w0xzJAf%2Fja4IcAXT6P%2FCi9DNmjR%5CMjndFpvyMO9SMZr7w8Y7szXYDIZacAq7bDkNzddmCFGEtZ8vHvuNUiRWX4oipeugcGRcP2PpbwcUHfXWbnC2pn5bnhcF0%5CTGzc1r3A%3A1557336619928; MUSIC_U=f4baf91334387fe7513bd57730082b7dfdeb07d266944bae914c50a7e8c7606b4da5a47bf416fc104b9674402ae1e3ca41049cea1c6bb9b6; __remember_me=true; __csrf=1f9a6b375d50ee31e61367bbe544b727',
    'origin': 'https://music.163.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
}

#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'music_163.middlewares.Music163SpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'music_163.middlewares.Music163DownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'music_163.pipelines.Music163Pipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
