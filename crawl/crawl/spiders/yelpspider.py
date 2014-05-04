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
    """Class to extract information from a Yelp review."""
    name = 'testyelp'
    allowed_domains = ['yelp.com']
    start_urls = (
        'http://www.yelp.com/biz/nopa-san-francisco?start=40',
    )

    item_selectors = {
        'yelp_biz_id': 'normalize-space(//meta[@name="yelp-biz-id"]/@content)',
        'restaurant_name': 'normalize-space(//h1[contains(@class, "biz-page-title")])',
        'restaurant_address': 'normalize-space(//address/span[@itemprop="streetAddress"])',
        'restaurant_city': 'normalize-space(//address/span[@itemprop="addressLocality"])',
        'restaurant_state': 'normalize-space(//address/span[@itemprop="addressRegion"])',
        'restaurant_postal_code': 'normalize-space(//address/span[@itemprop="postalCode"])',
        'restaurant_phone': 'normalize-space(//span[@class="biz-phone"])',
        'restaurant_website': 'normalize-space(//div[@class="biz-website"]/a/text())',
        'restaurant_reviews_count': 'normalize-space(//span[@itemprop="reviewCount"])',
        'restaurant_rating': ('normalize-space(//div[contains(@class, "biz-main-info")]'
                              '/div/div/div/meta[@itemprop="ratingValue"]/@content)'),
        'restaurant_category': '//div[@class="price-category"]/span/a/text()',
    }

    review_selectors = {
        'review_id': 'normalize-space(@data-review-id)',
        'review_content': './/p[contains(@class, "review_comment")]/text()',
        'review_content_date': 'normalize-space(.//meta[@itemprop="datePublished"]/@content)',
        'reviewer_restaurant_rating': 'normalize-space(.//meta[@itemprop="ratingValue"]/@content)',
        'reviewer_name': 'normalize-space(.//a[@class="user-display-name"]/text())',
        'reviewer_url': 'normalize-space(.//a[@class="user-display-name"]/@href)',
        'reviewer_location': 'normalize-space(.//li[@class="user-location"]/b)',
        'reviewer_friends_count': 'normalize-space(.//li[@class="friend-count"]/span/b)',
        'reviewer_reviews_count': 'normalize-space(.//li[@class="review-count"]/span/b)',
    }

    def parse(self, response):
        sel = Selector(response)
        loader = ItemLoader(item=YelpReview(), selector=sel)
        loader.add_value('crawl_date', '%s' % datetime.utcnow())

        # TODO: Dedup by canonical URL.
        loader.add_value('page_url', response.url)

        # Loop over all the fields we need to extract.
        for field, selector in self.item_selectors.iteritems():
            loader.add_xpath(field, selector)

        reviews = []
        master_review = loader.load_item()
        review_selectors = sel.xpath('//div[contains(@class, "review")][@itemprop="review"]')

        for rev_sel in review_selectors:
            review_loader = ItemLoader(item=master_review.copy(), selector=rev_sel)

            for field, selector in self.review_selectors.iteritems():
                review_loader.add_xpath(field, selector)

            reviews.append(review_loader.load_item())

        return reviews
