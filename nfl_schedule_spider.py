import scrapy

class NFLScheduleSpider(scrapy.Spider):
    name = "nfl"
    start_urls = [
        "http://www.nfl.com/schedules/2008",
        "http://www.nfl.com/schedules/2009",
        "http://www.nfl.com/schedules/2010",
        "http://www.nfl.com/schedules/2011",
        "http://www.nfl.com/schedules/2012",
        "http://www.nfl.com/schedules/2013",
        "http://www.nfl.com/schedules/2014",
        "http://www.nfl.com/schedules/2015",
        "http://www.nfl.com/schedules/2016",
        "http://www.nfl.com/schedules/2017",
        "http://www.nfl.com/schedules/2018",
    ]

    def parse(self, response):
        for game in response.css('div.schedules-list li.schedules-list-matchup'):
            game_content = game.css('div.schedules-list-content')
            yield {
                'gameid': game_content.xpath('@data-gameid').extract_first(),
                'away-abbr': game_content.xpath('@data-away-abbr').extract_first(),
                'home-abbr': game_content.xpath('@data-home-abbr').extract_first(),
                'away-mascot': game_content.xpath('@data-away-mascot').extract_first(),
                'gamestate': game_content.xpath('@data-gamestate').extract_first(),
                'gc-url': game_content.xpath('@data-gc-url').extract_first(),
                'localtime': game_content.xpath('@data-localtime').extract_first(),
                'site': game_content.xpath('@data-site').extract_first(),
            }