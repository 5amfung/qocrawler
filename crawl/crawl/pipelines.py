# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import log


class CrawlPipeline(object):
    def process_item(self, item, spider):
        log.msg('Process item from CrawlPipeline.', level=log.INFO)
        return item
