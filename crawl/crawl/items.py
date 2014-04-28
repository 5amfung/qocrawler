# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Field
from scrapy.item import Item


class YelpReview(Item):
    """Information of a restaurant.

    All fields are string unless specified otherwise.
    """

    # Crawl date.
    crawl_date = Field()

    # URL of the page that we crawled.
    page_url = Field()

    # Name of the restaurant.
    name = Field()

    # Restaurant address.
    address = Field()
    # City
    locality = Field()
    # State
    region = Field()
    # Postal code
    postal_code = Field()

    # Phone
    phone = Field()

    # Restaurant website
    website = Field()

    # Restaurant reviews count.
    reviews_count = Field()

    # Restaurant rating.
    rating = Field()

    # Restaurant category.  This could be a string or a list of categories.
    category = Field()

    # Review content.
    review_content = Field()

    # Review content date.
    review_content_date = Field()

    # Reviewer's name.
    reviewer_name = Field()

    # Reviewer's location.
    reviewer_location = Field()

    # Reviewer's friends count.
    reviewer_friends_count = Field()

    # Reviewer's reviews count.
    reviewer_reviews_count = Field()

