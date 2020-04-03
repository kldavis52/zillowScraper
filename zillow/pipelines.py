# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
import dns

class MongodbPipeline(object):
    collection_name = "zillow_rentals"

    def open_spider(self, spider):
        self.client = MongoClient("<ConnectionString>")
        self.db = self.client.zillow

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert(item)
        return item
