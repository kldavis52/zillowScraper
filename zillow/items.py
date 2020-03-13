# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst

class ZillowItem(scrapy.Item):
    _id = scrapy.Field(
        output_processor = TakeFirst()
    )

    detail_url = scrapy.Field(
        output_processor = TakeFirst()
    )

    status_text = scrapy.Field(
        output_processor = TakeFirst()
    )

    price = scrapy.Field(
        output_processor = TakeFirst()
    )

    building_name = scrapy.Field(
        output_processor = TakeFirst()
    )

    address = scrapy.Field(
        output_processor = TakeFirst()
    )

    beds = scrapy.Field(
        output_processor = TakeFirst()
    )

    baths = scrapy.Field(
        output_processor = TakeFirst()
    )

    area = scrapy.Field(
        output_processor = TakeFirst()
    )

    zpid = scrapy.Field(
        output_processor = TakeFirst()
    )

    street_address = scrapy.Field(
        output_processor = TakeFirst()
    )

    zipcode = scrapy.Field(
        output_processor = TakeFirst()
    )

    city = scrapy.Field(
        output_processor = TakeFirst()
    )

    state = scrapy.Field(
        output_processor = TakeFirst()
    )

    hdpPrice = scrapy.Field(
        output_processor = TakeFirst()
    )

    bedrooms = scrapy.Field(
        output_processor = TakeFirst()
    )

    bathrooms = scrapy.Field(
        output_processor = TakeFirst()
    )

    year_built = scrapy.Field(
        output_processor = TakeFirst()
    )

    home_type = scrapy.Field(
        output_processor = TakeFirst()
    )

    days_on_zillow = scrapy.Field(
        output_processor = TakeFirst()
    )

    brokerId = scrapy.Field(
        output_processor = TakeFirst()
    )

    broker_phone = scrapy.Field(
        output_processor = TakeFirst()
    )

    latitude = scrapy.Field(
        output_processor = TakeFirst()
    )

    longitude = scrapy.Field(
        output_processor = TakeFirst()
    )

    units = scrapy.Field()

    variable_data = scrapy.Field()

