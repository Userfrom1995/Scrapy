import json

import scrapy


class BookspiderSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com/']

    custom_settings = {
        'FEEDS': {
            'quotes1.json': {'format': 'json', 'overwrite': True},
        }
    }


    def parse(self, response):
        quotes = response.css('.quote')
        for quote in quotes:
            relative_url = quote.css('.author + a::attr(href)').get()

            author_url = 'https://quotes.toscrape.com/' + relative_url
            yield response.follow(author_url, callback=self.parse_author_page)

        next_page = response.css('li.next a ::attr(href)').get()
        if next_page is not None:
            next_page_url = 'https://quotes.toscrape.com/' + next_page

            yield response.follow(next_page_url, callback=self.parse)

    def parse_author_page(self, response):

        author_title = response.css('.author-title::text').get()
        born_date = response.css('.author-born-date::text').get()
        born_location = response.css('.author-born-location::text').get()
        description = response.css('.author-description::text').get()

        # Clean up description text
        # description = ' '.join(description.split())

        yield {
            'author_title': author_title,
            'born_date': born_date,
            'born_location': born_location,
            'description': description
        }
