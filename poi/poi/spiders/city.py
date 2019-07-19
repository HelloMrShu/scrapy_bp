# -*- coding: utf-8 -*-
import scrapy
from poi.items import CityItem


class CitySpider(scrapy.Spider):
    name = 'city'
    allowed_domains = ['www.poilist.cn']
    start_urls = ['http://www.poilist.cn/cities-list/%E7%BE%8E%E9%A3%9F/']
    custom_settings = {
        'ITEM_PIPELINES': {'poi.pipelines.CityPipeline': 300}
    }

    def parse(self, response):
        lis = response.xpath('//ul[@class="city-list"]/li/a/text()').extract()
        for li in lis:
            item = CityItem()
            item['name'] = li
            item['level'] = 1
            yield item
