import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class DemoSpiderSpider(CrawlSpider):
    name = 'demo_spider'
    allowed_domains = ['www.baidu.com']
    start_urls = [
        'https://www.wxapp-union.com/portal.php?mod=list&catid=2&page=1'
    ]

    rules = (
        Rule(
            LinkExtractor(allow=r'.+mod=list&catid=2&page=\d'),
            # callback='parse_item',
            follow=True),
        Rule(LinkExtractor(allow=r'.+article-.+\.html'),
             callback='parse_item',
             follow=False),
    )

    def parse_item(self, response):
        title = response.xpath("//h1[@class='ph']/text()").get()
        print(title)
