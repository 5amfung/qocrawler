# Yelp spider.

from datetime import datetime

from crawl.items import YelpReview
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.spiders import CrawlSpider
from scrapy.contrib.spiders import Rule
from scrapy.selector import Selector


# Allowed domain when extracting links from pages.
_ALLOWED_DOMAINS = ('www.yelp.com',)


class YelpSpider(CrawlSpider):
    """A spider to crawl recursively starting from URLs specified in start_urls.

    Set CLOSESPIDER_PAGECOUNT in settings.py to limit maximum.
    """
    name = 'testcrawl'
    allowed_domains = _ALLOWED_DOMAINS

    start_urls = (
        'http://www.yelp.com/biz/nopa-san-francisco',
    )

    # Rules for following links.
    rules = (
        # Pagination section of a restaurant review.
        Rule(
            SgmlLinkExtractor(
                allow=(
                    # www.yelp.com/biz/nopa-san-francisco
                    r'www.yelp.com/biz/[\w-]+$',

                    # www.yelp.com/biz/nopa-san-francisco?start=40
                    r'www.yelp.com/biz/.+\?start=\d+$',
                ),
                deny=(
                    # No need to crawl first page again.  Starting page has implicit start=0.
                    # www.yelp.com/biz/nopa-san-francisco?start=0
                    r'www.yelp.com/biz/.+\?start=0$',
                ),
                restrict_xpaths=(
                    # Pagination section.
                    '//ul[contains(@class, "pagination-links")]',

                    # Related business section.
                    '//div[contains(@class, "related-business")]',
                ),
                allow_domains=_ALLOWED_DOMAINS
            ),
            callback='parse_review',
            follow=True
        ),
    )

    # Selectors for restaurant info.
    _item_selectors = {
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

    # Selectors for reviews.
    _review_selectors = {
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

    def parse_review(self, response):
        sel = Selector(response)
        loader = ItemLoader(item=YelpReview(), selector=sel)
        loader.add_value('crawl_date', '%s' % datetime.utcnow())
        loader.add_value('page_url', response.url)

        # Loop over all the fields we need to extract.
        for field, selector in self._item_selectors.iteritems():
            loader.add_xpath(field, selector)

        reviews = []
        master_review = loader.load_item()
        review_selectors = sel.xpath('//div[contains(@class, "review")][@itemprop="review"]')

        for rev_sel in review_selectors:
            review_loader = ItemLoader(item=master_review.copy(), selector=rev_sel)

            for field, selector in self._review_selectors.iteritems():
                review_loader.add_xpath(field, selector)

            reviews.append(review_loader.load_item())

        return reviews
