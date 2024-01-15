import scrapy
from ..items import  QuoteprojectItem
from scrapy import FormRequest
from scrapy.utils.response import open_in_browser


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        "https://quotes.toscrape.com/login"
    ]


    def parse(self, response):
        token = response.xpath("//form/input/@value").extract_first()
        print(token)
        return FormRequest.from_response(response,  formdata={
            'csrf-token': token,
            'username': 'jobanjatt113@gmail.com',
            'password': 'dummy1234'
        }, callback=self.start_scraping)

    def start_scraping(self, response):
        open_in_browser(response)
        items = QuoteprojectItem()  # instance of class

        div_quotes = response.xpath("//div[@class='quote']")

        for quote in div_quotes:
            title = quote.xpath(".//span[@class='text']/text()").extract_first()
            author = quote.xpath(".//small[@class='author']/text()").extract_first()
            tags = quote.xpath(".//a[@class='tag']/text()").extract()
            items['title'] = title
            items['author'] = author
            items['tags'] = tags
            print(items)

            yield items









