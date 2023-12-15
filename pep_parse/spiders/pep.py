import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import BASE_DIR, RESULTS


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = [f'https://{domain}/' for domain in allowed_domains]
    (BASE_DIR / RESULTS).mkdir(exist_ok=True)

    def parse(self, response):
        for tag in response.css(
            '#numerical-index tr:not(:first-child) a::attr(href)'
        ).getall():
            yield response.follow(
                tag, self.parse_pep
            )

    def parse_pep(self, response):
        number, name = response.css(
            'head > title::text'
        ).get().split('|')[0].split(' – ')
        yield PepParseItem(
            number=number.replace('PEP ', ''),
            name=name.strip(),
            status=response.css('dt:contains("Status") + dd abbr::text').get()
        )
