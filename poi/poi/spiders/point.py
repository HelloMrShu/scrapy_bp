# -*- coding: utf-8 -*-
import scrapy
from poi.db.dbhelper import DBHelper
from poi.items import PoiItem
from poi.util import datamap
from poi.util import resolve
from scrapy.http import Request


class PointSpider(scrapy.Spider):
    name = 'point'
    allowed_domains = ['www.poilist.cn']
    start_urls = ['http://www.poilist.cn/poi-list-美食-北京/']
    custom_settings = {
        'ITEM_PIPELINES': {'poi.pipelines.PoiPipeline': 300}
    }
    baseurl = "http://www.poilist.cn/poi-list-"
    url = 'http://www.poilist.cn/poi-list-美食-北京/'

    # 查询分类与城市
    category = (DBHelper()).getcategory()
    categorymap = datamap(category)
    city = (DBHelper()).getcity()
    citymap = datamap(city)
    cityindex = 0
    cateIndex = 0

    def parse(self, response):
        # 解析当前页码和总页码
        page_cur = int(response.xpath('//ul[@class="pagination pagination-sm mar-t5"]/li[@class="active"]/a/text()').extract()[0])
        page_num = int(response.xpath('//ul[@class="pagination pagination-sm mar-t5"]/li[last()]/a/text()').extract()[0])

        zh = resolve(self.url)
        category_cur = zh[0]
        city_cur = zh[1]

        if page_cur < page_num:  # next page
            trs = response.xpath('//tbody/tr')
            item = PoiItem()
            for tr in trs:
                item['name'] = tr.xpath('./td[2]/text()').extract()[0]
                item['province'] = tr.xpath('./td[3]/text()').extract()[0]
                item['city'] = tr.xpath('./td[4]/text()').extract()[0]

                district = tr.xpath('./td[5]/text()').extract()
                item['district'] = district[0] if district else ''

                code = tr.xpath('./td[6]/text()').extract()
                item['code'] = code[0] if code else ''

                phone = tr.xpath('./td[7]/text()').extract()
                item['phone_no'] = phone[0] if phone else ''

                region = tr.xpath('./td[8]/text()').extract()
                item['region'] = region[0] if region else ''

                location = tr.xpath('./td[9]/text()').extract()
                item['location'] = location[0] if location else ''

                cate = tr.xpath('./td[10]/text()').extract()
                item['category'] = cate[0] if cate else ''

                sub = tr.xpath('./td[11]/text()').extract()
                item['sub_category'] = sub[0] if sub else ''

                lon = tr.xpath('./td[12]/text()').extract()
                item['longitude'] = lon[0] if lon else 0

                lat = tr.xpath('./td[13]/text()').extract()
                item['latitude'] = lat[0] if lat else 0
                yield item

            temp = self.baseurl + category_cur + '-' + city_cur + '/'
            suffix = int(page_cur) * 30
            url = temp + str(suffix)
            self.url = url
            yield Request(url, callback=self.parse, dont_filter=True)
        else:
            # next city
            self.cityindex += 1
            if self.cityindex == len(self.citymap):
                # next category
                self.cateIndex += 1
                if self.cateIndex >= len(self.category):
                    exit(0)
                else:
                    category_cur = self.categorymap[self.cateIndex]
                    self.cityindex = 0
            city_cur = self.citymap[self.cityindex]
            url = self.baseurl + category_cur + '-' + city_cur + '/'
            self.url = url
            yield Request(url, callback=self.parse, dont_filter=True)


