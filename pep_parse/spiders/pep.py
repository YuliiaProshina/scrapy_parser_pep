import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        all_peps = response.css('table a[href^="pep-"]::attr(href)')
        for pep_link in all_peps:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        title = response.css('h1.page-title::text').get()
        number, name = title.split(' – ', 1)
        status = response.css('dt:contains("Status") + dd abbr::text').get()
        yield PepParseItem(
            number=number.replace('PEP ', ''),
            name=name,
            status=status,
        )

