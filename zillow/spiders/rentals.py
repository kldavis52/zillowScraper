# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy.loader import ItemLoader
from ..utils import URL, cookie_parser, parse_new_url
from ..items import ZillowItem
from scrapy.exceptions import CloseSpider

class RentalsSpider(scrapy.Spider):
    name = 'rentals'
    allowed_domains = ['www.zillow.com']
    
    def start_requests(self):
        #URL = start_URL()
        yield scrapy.Request(
            url=URL,
            callback=self.parse,
            cookies=cookie_parser(),
            meta={
                'currentPage': 1
            }
        )

    def parse(self, response):
        current_page = response.request.meta['currentPage']
        json_resp = json.loads(response.body)
        rentals = json_resp.get('searchResults').get('listResults')

        if rentals is None:
            raise CloseSpider("No rentals available in this city")

        for rental in rentals:
            loader = ItemLoader(item=ZillowItem())
            loader.add_value('_id', rental.get('zpid'))
            loader.add_value('detail_url', rental.get('detailUrl'))
            loader.add_value('status_text', rental.get('statusText'))
            loader.add_value('price', rental.get('price'))
            loader.add_value('building_name', rental.get('buildingName'))
            loader.add_value('address', rental.get('address'))
            loader.add_value('beds', rental.get('beds'))
            loader.add_value('baths', rental.get('baths'))
            loader.add_value('area', rental.get('area'))
            loader.add_value('latitude', rental.get('latLong').get('latitude'))
            loader.add_value('longitude', rental.get('latLong').get('longitude'))
            loader.add_value('units', rental.get('units'))
            loader.add_value('variable_data', rental.get('variableData'))
            if (rental.get('hdpData')):
                #loader.add_value('zpid', rental.get('hdpData').get('homeInfo').get('zpid'))
                loader.add_value('street_address', rental.get('hdpData').get('homeInfo').get('streetAddress'))
                loader.add_value('zipcode', rental.get('hdpData').get('homeInfo').get('zipcode'))
                loader.add_value('city', rental.get('hdpData').get('homeInfo').get('city'))
                loader.add_value('state', rental.get('hdpData').get('homeInfo').get('state'))
                loader.add_value('hdpPrice', rental.get('hdpData').get('homeInfo').get('price'))
                loader.add_value('bedrooms', rental.get('hdpData').get('homeInfo').get('bedrooms'))
                loader.add_value('bathrooms', rental.get('hdpData').get('homeInfo').get('bathrooms'))
                loader.add_value('year_built', rental.get('hdpData').get('homeInfo').get('yearBuilt'))
                loader.add_value('home_type', rental.get('hdpData').get('homeInfo').get('homeType'))
                loader.add_value('days_on_zillow', rental.get('hdpData').get('homeInfo').get('daysonZillow'))
                loader.add_value('brokerId', rental.get('hdpData').get('homeInfo').get('brokerId'))
                loader.add_value('broker_phone', rental.get('hdpData').get('homeInfo').get('contactPhone'))
                
            yield loader.load_item()

        total_pages = json_resp.get('searchList').get('totalPages')
        if current_page <= total_pages:
            current_page += 1
            yield scrapy.Request(
                url=parse_new_url(URL, page_number=current_page),
                callback=self.parse,
                cookies=cookie_parser(),
                meta={
                    'currentPage': current_page
                }
            )