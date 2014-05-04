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

    # Yelp biz ID.
    yelp_biz_id = Field(output_processor=TakeFirst())

    # Name of the restaurant.
    restaurant_name = Field(output_processor=TakeFirst())

    # Restaurant address.
    restaurant_address = Field(output_processor=TakeFirst())

    # City
    restaurant_city = Field(output_processor=TakeFirst())

    # State
    restaurant_state = Field(output_processor=TakeFirst())

    # Postal code
    restaurant_postal_code = Field(output_processor=TakeFirst())

    # Phone
    restaurant_phone = Field(output_processor=TakeFirst())

    # Restaurant website
    restaurant_website = Field(output_processor=TakeFirst())

    # Restaurant reviews count.
    restaurant_reviews_count = Field(output_processor=TakeFirst())

    # Restaurant rating.
    restaurant_rating = Field(output_processor=TakeFirst())

    # Restaurant category.  This could be a string or a list of categories.
    restaurant_category = Field()

    # Review ID.
    review_id = Field(output_processor=TakeFirst())

    # Review content.  A list of paragraphs.
    review_content = Field()

    # Review content date.
    review_content_date = Field(output_processor=TakeFirst())

    # Reviewer restaurant rating.
    reviewer_restaurant_rating = Field(output_processor=TakeFirst())

    # Reviewer name.
    reviewer_name = Field(output_processor=TakeFirst())

    # Reviewer URL
    reviewer_url = Field(output_processor=TakeFirst())

    # Reviewer location.
    reviewer_location = Field(output_processor=TakeFirst())

    # Reviewer friends count.
    reviewer_friends_count = Field(output_processor=TakeFirst())

    # Reviewer reviews count.
    reviewer_reviews_count = Field(output_processor=TakeFirst())

