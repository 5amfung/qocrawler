# Scrapy settings for crawl project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'crawl'

SPIDER_MODULES = ['crawl.spiders']
NEWSPIDER_MODULE = 'crawl.spiders'

# Turn off cookies.  We don't want sites to track us.
COOKIES_ENABLED = False

# Random delay from 0.5 and 1.5 * DOWNLOAD_DELAY
RANDOMIZE_DOWNLOAD_DELAY = True
DOWNLOAD_DELAY = 1

# Use a real browser like user agent rather than the default scrappy user agent.
USER_AGENT = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) '
              'Chrome/35.0.1916.47 Safari/537.36')