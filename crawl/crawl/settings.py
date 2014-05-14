# Scrapy settings for crawl project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

# Add -L DEBUG to command line if you want more verbosity.
LOG_LEVEL = 'INFO'

# Limit number of page crawling for development.  Comment out to remove limit.
CLOSESPIDER_PAGECOUNT = 20

# Enable cache for development.  Disable for production.
HTTPCACHE_ENABLED = True


### Settings belows this line should not require any changes. ###

BOT_NAME = 'Yelp'

SPIDER_MODULES = ['crawl.spiders']
NEWSPIDER_MODULE = 'crawl.spiders'

# Turn off cookies.  We don't want sites to track us.
COOKIES_ENABLED = False

# Random delay from 0.5 and 1.5 * DOWNLOAD_DELAY
RANDOMIZE_DOWNLOAD_DELAY = True
DOWNLOAD_DELAY = 2

# Disable the default user agent middleware and use our own random user agent downloader middleware.
DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
    'crawl.middleware.RandomUserAgentDownloaderMiddleware': 400,
}
USER_AGENT_LIST = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.13+ (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10',
    'Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20120101 Firefox/29.0',
    'Mozilla/5.0 (X11; Linux x86_64; rv:28.0) Gecko/20100101 Firefox/28.0',
]

# Disable redirect.
REDIRECT_ENABLED = False

# Concurrent requests by downloader.
CONCURRENT_REQUESTS = 30

# Max concurrent requests to any single domain.
CONCURRENT_REQUESTS_PER_DOMAIN = 15
