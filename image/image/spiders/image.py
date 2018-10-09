# -*- coding: utf-8 -*-
import scrapy
from image.items import ImageItem
from scrapy.http import Request
import sys
import datetime
from image.emailSender import emailSender  # 导入发信模块ssss

class ImageSpider(scrapy.Spider):
    name = 'image'
    allowed_domains = ['xdcd.com']

    base = 'https://xkcd.com/'
    start_urls = ['https://xkcd.com/1']
    
    def parse(self, response):
    	emailSenderClient = emailSender()
    	#emailSenderClient.sendEmail(['986934994@qq.com'], 'crawl begin') #发送邮件

    	item = ImageItem()
    	item['title'] = ''
    	item['url'] = ''

    	item['title'] = response.xpath('//div[@id="ctitle"]/text()').extract()[0]

    	for urlSelector in response.xpath('//div[@id="comic"]'):
    		urls = urlSelector.xpath('img/@src').extract()
    		
    		if len(urls):
    			item['url'] = 'https:' + urls[0]
    		else:
    			urls = urlSelector.xpath('a/img/@src').extract()
    			if len(urls):
    				item['url'] = 'https:' + urls[0]

    		if item['title'] and item['url']:
    			yield item

    	nextPageSelector = response.xpath('//div[@id="middleContainer"]/ul[@class="comicNav"]')
    	urlStr = nextPageSelector.xpath('li/a/@href').extract()[3]
    	urlArr = urlStr.split('/')
    	#print(response.request.headers['User-Agent'])

    	if len(urlArr) >= 2:
    		nextPageUrl = self.base + str(urlArr[1]) + '/'
    		yield Request(nextPageUrl, callback=self.parse, dont_filter = True)