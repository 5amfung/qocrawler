# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
from scrapy import log


class DedupPipeline(object):
    """Drop duplicate item."""

    def __init__(self):
        self._seen = ()

    def process_item(self, item, spider):
        url = item['page_url']

        if url in self._seen:
            log.msg('Duplicate url: %s' % url, level=log.INFO)
            raise DropItem('Duplicate url: %s' % url)

        log.msg('Add %s' % url, level=log.INFO)
        log.msg(self._seen, level=log.INFO)

        self._seen.add(url)
        return item
