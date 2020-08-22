# Scrapy settings for maoyan project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'maoyan'

SPIDER_MODULES = ['maoyan.spiders']
NEWSPIDER_MODULE = 'maoyan.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36hi'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
#LOG_LEVEL = 'ERROR'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
RANDOMIZE_DOWNLOAD_DELAY = True
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': '__mta=176608922.1597632903839.1597988935851.1597989041725.54; uuid_n_v=v1; uuid=0B849BF0E03511EABADBF5D4F95847E7CCA4DD73CBDB44599E704D9CBB3B4CC1; _lxsdk_cuid=173fa57775bc8-098fb41f4d3c05-31657301-1fa400-173fa57775bc8; _lxsdk=0B849BF0E03511EABADBF5D4F95847E7CCA4DD73CBDB44599E704D9CBB3B4CC1; mojo-uuid=cd8d1354e7b864ff6d9c87fbe9a24c56; _csrf=71bb420d086a3d4e0ee0078415a835910d55e0db3003192d2359a8d2b1ed9905; mojo-session-id={"id":"563df98e7dea1a2ba74add4dcff5e5be","time":1598019740474}; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1597817974,1597921463,1597967186,1598019740; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; mojo-trace-id=7; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1598019753; __mta=176608922.1597632903839.1597989041725.1598019753327.55; _lxsdk_s=17411662396-4e4-c80-92e%7C%7C10',
    'Referer': 'https://maoyan.com/films?showType=3'
}
# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'maoyan.middlewares.MaoyanSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'maoyan.middlewares.MaoyanDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'maoyan.pipelines.MaoyanPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
