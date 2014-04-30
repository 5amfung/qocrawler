# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.contrib.loader.processor import TakeFirst
from scrapy.item import Field
from scrapy.item import Item


class YelpReview(Item):
    """Information of a restaurant.

    All fields are string unless specified otherwise.
    """

    # Crawl date.
    crawl_date = Field(output_processor=TakeFirst())

    # URL of the page that we crawled.
    page_url = Field()

    # Name of the restaurant.
    name = Field(output_processor=TakeFirst())

    # Restaurant address.
    address = Field(output_processor=TakeFirst())

    # City
    city = Field(output_processor=TakeFirst())

    # State
    state = Field(output_processor=TakeFirst())

    # Postal code
    postal_code = Field(output_processor=TakeFirst())

    # Phone
    phone = Field(output_processor=TakeFirst())

    # Restaurant website
    website = Field(output_processor=TakeFirst())

    # Restaurant reviews count.
    reviews_count = Field(output_processor=TakeFirst())

    # Restaurant rating.
    rating = Field(output_processor=TakeFirst())

    # Restaurant category.  This could be a string or a list of categories.
    category = Field()

    # Review content.
    review_content = Field(output_processor=TakeFirst())

    # Review content date.
    review_content_date = Field(output_processor=TakeFirst())

    # Reviewer's name.
    reviewer_name = Field(output_processor=TakeFirst())

    # Reviewer's location.
    reviewer_location = Field(output_processor=TakeFirst())

    # Reviewer's friends count.
    reviewer_friends_count = Field(output_processor=TakeFirst())

    # Reviewer's reviews count.
    reviewer_reviews_count = Field(output_processor=TakeFirst())

