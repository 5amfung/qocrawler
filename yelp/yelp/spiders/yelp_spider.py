# Spider

from scrapy.selector import Selector
from scrapy.spider import Spider
from yelp import items


class YelpSpider(Spider):
    name = 'yelp'
    allowed_domains = ['yelp.com']
    start_urls = (
        'http://www.yelp.com/biz/nopa-san-francisco'
    )

    def parse(self, response):
        sel = Selector(response)
        entity = items.EntityItem()
        entity['title'] = sel.xpath('//title/text()').extract()
        return entity
