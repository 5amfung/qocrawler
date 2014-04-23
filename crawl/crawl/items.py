# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class ReviewItem(Item):
    """A scraped item for restaurant reviews."""

    # URL of the page.
    url = Field

    # Title of the page.
    title = Field

    # Review content
    review_content = Field
