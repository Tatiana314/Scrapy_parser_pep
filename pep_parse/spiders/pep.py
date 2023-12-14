import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        for tag in response.css('#numerical-index tr')[1:]:
            yield response.follow(
                tag.css('a::attr(href)').get(), self.parse_pep
            )

    def parse_pep(self, response):
        title = response.css(
            'head > title::text'
        ).get().split('|')[0].split(' – ')
        yield PepParseItem({
            'number': title[0].replace('PEP ', ''),
            'name': title[1].strip(),
            'status': response.css(
                'dt:contains("Status") + dd'
            ).css('abbr::text').get()
        })
