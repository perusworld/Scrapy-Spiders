import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class NFLNewsSpider(CrawlSpider):
    name = "nfl-news"
    allowed_domains = ['nfl.com']
    start_urls = [
        "https://www.nfl.com/news/all-news",
    ]
    rules = (
        Rule(LinkExtractor(restrict_xpaths="//a[@class='d3-o-media-object__link d3-o-button']"), follow=True, callback='parse_item'),
    )

    def parse_item(self, response):
        yield {
            'title': response.xpath('normalize-space(//h1[@class="nfl-c-article__title"]/text())').extract(),
            'date': response.xpath('normalize-space(//div[@class="nfl-c-article__dates"]/text())').extract(),
            'url': response.request.url
        }