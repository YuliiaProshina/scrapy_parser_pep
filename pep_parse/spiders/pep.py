import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        all_peps = response.css('table.pep-zero-table tbody tr')
        for pep in all_peps:
            pep_link = pep.css('a::attr(href)').get()
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
