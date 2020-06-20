# -*- coding: utf-8 -*-

# Scrapy settings for fangwu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'fangwu'

SPIDER_MODULES = ['fangwu.spiders']
NEWSPIDER_MODULE = 'fangwu.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'fangwu (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

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
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'fangwu.middlewares.FangwuSpiderMiddleware': 543,
#}

# 需要使用代理ip的打开
DOWNLOADER_MIDDLEWARES = {
   'fangwu.middlewares.FangwuDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}
LOG_FILE = "fangwu.log"
LOG_LEVEL = "DEBUG"
# LOG_LEVEL = "WARNING"

DOWNLOAD_DELAY = 1

COOKIES_ENABLED = False

FEED_EXPORT_ENCODING = 'utf-8'
# 支持随机下载延迟
RANDOMIZE_DOWNLOAD_DELAY = True
# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'fangwu.pipelines.FangwuPipeline': 300,
}

proxyUser = "590788499532566528"
proxyPass = "3R4gvRpx"
proxyHost = "http-dynamic.xiaoxiangdaili.com"
proxyPort = "10030"

proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
    "host": proxyHost,
    "port": proxyPort,
    "user": proxyUser,
    "pass": proxyPass,
}