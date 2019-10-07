import scrapy
from scrapy import Selector
from lxml import html
from webscrabing.items import WebscrabingItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://in.hotels.com/search.do?resolved-location=CITY%3A1506246%3AUNKNOWN%3AUNKNOWN&destination-id=1506246&q-destination=New%20York,%20New%20York,%20United%20States%20Of%20America&q-rooms=1&q-room-0-adults=2&q-room-0-children=0'
    ]

    # def parse(self, response):
    # 	hole_page = response.body
    # 	data = html.document_fromstring(hole_page)
    # 	for div in  data.xpath("//div[@id='listings']/ol/li/article/section"):
    # 		yield {
    #             'name': div.xpath("//div/h3/a//text()"),
    #             'address': div.xpath("//div/address/span//text()"),
    #             'rating': div.xpath("//div/div/div/strong//text()"),
    #             'price' : div.xpath("//aside/div/strong//text()")
    #         }


    def parse(self, response):
    	product = WebscrabingItem()
    	for hole_page in response.xpath("//div[@id='listings']/ol/li/article/section").getall():
    		div = Selector(text=hole_page)
    		product['name'] = div.xpath("//div/h3/a//text()").get()
    		product['address'] = div.xpath("//div/address/span//text()").get()
    		product['rating'] = div.xpath("//div/div/div/strong//text()").get()
    		product['price'] = div.xpath("//aside/div/strong//text()").get()
    		yield product
    		# yield {
      #           'name': div.xpath("//div/h3/a//text()").get(),
      #           'address': div.xpath("//div/address/span//text()").get(),
      #           'rating': div.xpath("//div/div/div/strong//text()").get(),
      #           'price' : div.xpath("//aside/div/strong//text()").get()
      #       }
