# Yelp spiders.
#

from datetime import datetime

from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider
from scrapy.contrib.spiders import Rule
from scrapy import log
from scrapy.selector import Selector
from scrapy.spider import Spider
from crawl.items import YelpReview
from crawl.util import extract


class TestYelpSpider(Spider):
    name = 'testyelp'
    allowed_domains = ['yelp.com']
    start_urls = (
        'http://www.yelp.com/biz/nopa-san-francisco',
    )

    def parse(self, response):
        return YelpReviewExtractor(Selector(response)).build(YelpReview())


class YelpReviewExtractor():
    """A class to build an item."""

    def __init__(self, selector):
        """Constructor.

        Args:
            selector: A Selector object.
        """
        self._selector = selector

    def name_selector(self):
        return self._selector.css('.biz-page-title').xpath('normalize-space(text())')

    def address_selector(self):
        return self._selector.css('.street-address address span[itemprop="streetAddress"]')\
                             .xpath('normalize-space(text())')

    def locality_selector(self):
        return self._selector.css('.street-address address span[itemprop="addressLocality"]')\
                             .xpath('normalize-space(text())')

    def region_selector(self):
        return self._selector.css('.street-address address span[itemprop="addressRegion"]')\
                             .xpath('normalize-space(text())')

    def postal_code_selector(self):
        return self._selector.css('.street-address address span[itemprop="postalCode"]')\
                             .xpath('normalize-space(text())')

    def phone_selector(self):
        return self._selector.css('.biz-phone').xpath('normalize-space(text())')

    def website_selector(self):
        return self._selector.css('.biz-website a').xpath('normalize-space(text())')

    def reviews_count_selector(self):
        return self._selector.css('.biz-main-info .review-count span[itemprop="reviewCount"]')\
                             .xpath('normalize-space(text())')

    def rating_selector(self):
        return self._selector.css('.biz-main-info .biz-rating meta[itemprop="ratingValue"]')\
                             .xpath('normalize-space(@content)')

    def category_selector(self):
        return self._selector.css('.category-str-list a').xpath('normalize-space(text())')

    def _review_content_selector(self):
        return self._selector.css('')

    def _review_content_date_selector(self):
        return self._selector.css('')

    def _reviewer_name_selector(self):
        return self._selector.css('')

    def _reviewer_location_selector(self):
        return self._selector.css('')

    def _reviewer_friends_count_selector(self):
        return self._selector.css('')

    def _review_reviews_count_selector(self):
        return self._selector.css('')

    def build(self, item):
        """Fill item with extracted information from selector.

        Args:
            item: A YelpReview object.

        Returns:
            A YelpReview object.
        """
        keys = item.fields.keys()

        for key in keys:
            func = '%s_selector' % key
            if hasattr(self, func):
                item[key] = extract(getattr(self, func)())
        return item


# class YelpSpider(CrawlSpider):
#     name = 'yelp'
#     allowed_domains = ['yelp.com']
#     start_urls = (
#         'http://www.yelp.com/search?find_loc=san+francisco%2C+ca&cflt=restaurants',
#     )
#     rules = (
#         #Rule(SgmlLinkExtractor(allow=('', ), deny=('', ))),
#         #Rule(SgmlLinkExtractor(allow=('', )), callback='parse_restaurant'),
#     )
#
#     def parse_restaurant(self, response):
#         sel = Selector(response)
#         restaurant = YelpRestaurant()
#
#         return restaurant

