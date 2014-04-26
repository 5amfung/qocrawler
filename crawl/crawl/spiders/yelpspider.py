# Yelp spider.

from scrapy.selector import Selector
from scrapy.spider import Spider
from crawl import items


class YelpSpider(Spider):
    name = 'testyelp'
    allowed_domains = ['yelp.com']
    start_urls = (
        'http://www.yelp.com/biz/nopa-san-francisco',
        'http://www.yelp.com/biz/foreign-cinema-san-francisco',
        'http://www.yelp.com/biz/frances-san-francisco',
        'http://www.yelp.com/biz/state-bird-provisions-san-francisco',
        'http://www.yelp.com/biz/frascati-san-francisco',
        'http://www.yelp.com/biz/stones-throw-san-francisco-2',
        'http://www.yelp.com/biz/lazy-bear-san-francisco',
        'http://www.yelp.com/biz/gary-danko-san-francisco',
    )

    def parse(self, response):
        sel = Selector(response)
        review = items.ReviewItem()
        review['name'] = trim(sel.css('.biz-page-title::text').extract())
        review['title'] = trim(sel.xpath('//title/text()').extract())
        return review


def trim(lst):
    """Trim and return the first element of a list.  Otherwise, return an empty string."""
    return lst[0].strip() if lst else ''
