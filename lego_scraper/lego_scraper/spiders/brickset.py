# -*- coding: utf-8 -*-
import scrapy


class BricksetSpider(scrapy.Spider):
    name = 'brickset'
    allowed_domains = ['brickset.com']
    start_urls = ['https://brickset.com/sets/year-2018']

    def parse(self, response):
        pass
