# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import log


class ValidateItemPipeline(object):
    def process_item(self, item, spider):

        # TODO: Not doing any for now.
        log.msg('Validate item.', level=log.DEBUG)

        return item
