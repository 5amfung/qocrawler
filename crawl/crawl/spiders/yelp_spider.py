# Yelp spider.

from scrapy.selector import Selector
from scrapy.spider import Spider
from crawl import items


class YelpSpider(Spider):
    name = 'yelp'
    allowed_domains = ['yelp.com']
    start_urls = (
        'http://www.yelp.com/biz/nopa-san-francisco',
    )

    def parse(self, response):
        sel = Selector(response)
        review = items.ReviewItem()
        review['title'] = sel.xpath('//title/text()').extract()
        return review
