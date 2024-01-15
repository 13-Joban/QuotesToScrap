import scrapy
from .items import  QuoteprojectItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    page_number = 2
    start_urls = [
        "https://quotes.toscrape.com/page/1/"
    ]


    def parse(self, response):
        # f = response.xpath("//div[@class='quote'][1]")  // for first quote

        items = QuoteprojectItem()  # instance of class

        div_quotes = response.xpath("//div[@class='quote']")

        for quote in div_quotes:
            title = quote.xpath(".//span[@class='text']/text()").extract_first()
            author = quote.xpath(".//small[@class='author']/text()").extract_first()
            tags = quote.xpath(".//a[@class='tag']/text()").extract()
            items['title'] = title
            items['author'] = author
            items['tags'] = tags

            yield items
        # next_page = response.xpath("//li[@class='next']/a/@href").extract_first()
        next_page = 'https://quotes.toscrape.com/page/' + str(QuotesSpider.page_number) + '/'
        if QuotesSpider.page_number < 11:
            QuotesSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)





        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)






# ajio men jeans url = https://www.ajio.com/s/clothing-4461-74581?query=%3Arelevance%3Al1l3nestedcategory%3AMen%20-%20Jeans&curated=true&curatedid=clothing-4461-74581&gridColumns=5&segmentIds=
# //div[@class='brand']//strong  for brand name
# //div[@class='nameCls']   for jean name
# //span[@class='price  ']/strong  for price


