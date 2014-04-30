# Yelp spiders.
#

from datetime import datetime

from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider
from scrapy.contrib.spiders import Rule
from scrapy import log
from scrapy.selector import Selector
from scrapy.spider import Spider
from crawl.items import YelpReview
from crawl.util import extract
from twisted.internet.defer import _DefGen_Return


class TestYelpSpider(Spider):
    name = 'testyelp'
    allowed_domains = ['yelp.com']
    start_urls = (
        'http://www.yelp.com/biz/nopa-san-francisco',
    )

    item_selectors = {
        'name': 'normalize-space(//h1[contains(@class, "biz-page-title")])',
        'address': 'normalize-space(//address/span[@itemprop="streetAddress"])',
        'city': 'normalize-space(//address/span[@itemprop="addressLocality"])',
        'state': 'normalize-space(//address/span[@itemprop="addressRegion"])',
        'postal_code': 'normalize-space(//address/span[@itemprop="postalCode"])',
        'phone': 'normalize-space(//span[@class="biz-phone"])',
        'website': 'normalize-space(//div[@class="biz-website"]/a/text())',
        'reviews_count': 'normalize-space(//span[@itemprop="reviewCount"])',
        'rating': ('normalize-space(//div[contains(@class, "biz-main-info")]'
                   '/div/div/div/meta[@itemprop="ratingValue"]/@content)'),
        'category': '//div[@class="price-category"]/span/a/text()',
    }

    def parse(self, response):
        loader = ItemLoader(item=YelpReview(), response=response)
        loader.add_value('crawl_date', '%s' % datetime.utcnow())
        loader.add_value('page_url', response.url)

        for field, selector in self.item_selectors.iteritems():
            loader.add_xpath(field, selector)

        # TODO: Get reviews.

        return loader.load_item()
