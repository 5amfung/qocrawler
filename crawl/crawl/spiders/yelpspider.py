# Yelp spider.

from datetime import datetime

from crawl.items import YelpReview
from scrapy import log
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

    Following is contracts for testing spider.
    @url http://www.yelp.com/biz/nopa-san-francisco
    @returns items 1 40
    @scrapes yelp_biz_id restaurant_name restaurant_category review_content
    """
    name = 'yelp'
    allowed_domains = _ALLOWED_DOMAINS

    start_urls = (
        'http://www.yelp.com/search?find_loc=San+Francisco%2C+CA&cflt=restaurants',
    )

    # Rules for following links.
    rules = (
        # Search results page for San Francisco restaurants.
        Rule(
            # Follow restaurants links in search results page.
            SgmlLinkExtractor(
                allow=(
                    r'/search\?find_loc=San\+Francisco%2C\+CA&cflt=restaurants(&start=\d+)?$',
                ),
                deny=(
                    # No need to follow first page again.  First page has implicit start=0.
                    r'/search\?find_loc=San\+Francisco%2C\+CA&cflt=restaurants&start=0$',
                ),
                restrict_xpaths=(
                    '//div[contains(@class, "search-pagination")]',
                ),
                allow_domains=_ALLOWED_DOMAINS
            ),
            follow=True
        ),

        Rule(
            # Restaurant reviews page.
            SgmlLinkExtractor(
                allow=(
                    # www.yelp.com/biz/nopa-san-francisco
                    # www.yelp.com/biz/nopa-san-francisco?start=40
                    r'/biz/.+?-san-francisco(-[\d]+)?(\?start=\d+)?$',
                ),
                deny=(
                    # No need to follow first page again.  First page has implicit start=0.
                    # www.yelp.com/biz/nopa-san-francisco?start=0
                    r'/biz/.+?-san-francisco(-[\d]+)?\?start=0$',
                ),
                restrict_xpaths=(
                    # Review pagination section in a /biz/{restaurant} page.
                    '//ul[contains(@class, "pagination-links")]',

                    # Related business section in a /biz/{restaurant} page.
                    '//div[contains(@class, "related-business")]',

                    # Search results section in a search results page.
                    '//ul[contains(@class, "search-results")]',
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
        self.log('Parse URL: %s' % response.url, level=log.INFO)

        sel = Selector(response)

        if not self._is_right_category(sel):
            return

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

    @classmethod
    def _is_right_category(cls, selector):
        """Return true if selector finds a specific string that indicates the right category."""
        return (len(selector.re('<span itemprop="title">Restaurants</span>')) or
                len(selector.re('<span itemprop="title">Food</span>')) or
                len(selector.re('<span itemprop="title">Nightlife</span>')))
