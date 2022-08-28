from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class CTASpider(CrawlSpider):
    name = "cta-spider"
    allowed_domains = ['catamilacademy.org']
    start_urls = [
        "https://www.catamilacademy.org/branches.html",
    ]
    rules = (
        Rule(LinkExtractor(restrict_xpaths="//p[normalize-space()='Branches']/following::blockquote[1]//a"), follow=True, callback='parse_item'),
    )

    def parse_item(self, response):
        yield {
            'schoolName': response.xpath('normalize-space((//p[@class="header_1"])[1]/text())').extract(),
            'location': response.xpath('normalize-space((//p[normalize-space()="Location"]/following::blockquote[1]/text())').extract(),
            'url': response.request.url
        }