import scrapy
from datetime import datetime

class CTAFremontHSCPSpider(scrapy.Spider):
    name = "cta-fre-hscp"
    start_urls = [
        "https://www.catamilacademy.org/ITAFremontHSCPSchool.html",
    ]

    def to_int(self, txt):
        try:
            return int(txt.strip())
        except:
            return 0

    def normalize_week(self, txt):
        return self.to_int(txt)

    def normalize_date(self, txt):
        try:
            return int(datetime.strptime(txt.strip(),"%m/%d/%Y").strftime("%Y%m%d"))
        except:
            return 0

    def normalize_holiday(self, txt):
        return 'holiday' == txt.strip().lower()

    def normalize_notes(self, txt):
        return txt

    def is_valid(self, txt):
        return 'date' != txt.strip().lower()

    def parse(self, response):
        for week in response.xpath('//p[contains(@id,"Schedule")]/following::table[1]//tr'):
            if self.is_valid(week.xpath('normalize-space(td[2]/text())').get()):
                yield {
                    'week': self.normalize_week(week.xpath('normalize-space(td[1]/text())').get()),
                    'date': self.normalize_date(week.xpath('normalize-space(td[2]/text())').get()),
                    'holiday': self.normalize_holiday(week.xpath('normalize-space(td[1]/text())').get()),
                    'notes': self.normalize_notes(week.xpath('normalize-space(td[3]/text())').get()),
                }