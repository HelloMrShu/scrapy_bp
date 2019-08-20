# -*- coding: utf-8 -*-
import scrapy
from poi.items import CategoryItem
import html


class CategorySpider(scrapy.Spider):
    name = 'category'
    allowed_domains = ['www.poilist.cn']
    start_urls = ['http://www.poilist.cn']
    custom_settings = {
        'ITEM_PIPELINES': {'poi.pipelines.CategoryPipeline': 300}
    }

    def parse(self, response):
        names = response.xpath('//div[@class="caption"]/h4/text()').extract()

        item = CategoryItem()
        for name in names:
            item['name'] = html.unescape(name)
            yield item


