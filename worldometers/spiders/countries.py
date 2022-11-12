import scrapy


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        title=response.xpath("//td/a/text()").getall()
        countries=response.xpath("//td/a/text()").getall()
        yield{
            'title':title,
            'countries':countries
        }
