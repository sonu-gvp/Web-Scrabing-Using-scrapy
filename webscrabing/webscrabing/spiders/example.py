import scrapy
from scrapy import Selector
from lxml import html
from webscrabing.items import WebscrabingItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ['in.hotels.com']

    def start_requests(self):
        yield scrapy.Request('https://in.hotels.com/search.do?resolved-location=CITY%3A1506246%3AUNKNOWN%3AUNKNOWN&destination-id=1506246&q-destination=New%20York,%20New%20York,%20United%20States%20Of%20America&q-rooms=1&q-room-0-adults=2&q-room-0-children=0',
        					 self.get_hotel_data)


    def get_hotel_data(self, response):
    	data = html.document_fromstring(response.body)
    	hotels_details_list = []
    	location = data.xpath("//div[@class='main-inner']/div[@class='summary']/h1/text()")
    	location = location[0].split(',')
    	country = location[-1]
    	data_list = data.xpath("//div[@id='listings']/ol/li/article/section")
    	for div in  data_list:
    		hotels_details = {}
    		name = div.xpath("div[@class='description resp-module']/h3[@class='p-name']/a/text()")[0]
    		
    		address = div.xpath("div[@class='description resp-module']/address[@class='contact']/span[@class='address']/text()")[0]
    		
    		rating = div.xpath("div[@class='description resp-module']/div[@class='details resp-module']/div[@class='reviews-box resp-module']/strong/text()")[0]
    		
    		price_div = div.xpath("aside[@class='pricing resp-module']/div[@class='price']")[0]
    		
    		if price_div.find("strong") is not None:
    			price = price_div.find("strong").text
    		else:
    			price = price_div.find("ins").text
    		hotels_details['name'] = name
    		hotels_details['address'] = address
    		hotels_details['rating'] = rating
    		hotels_details['price'] = price
    		hotels_details['country'] = country
    		hotels_details_list.append(hotels_details)
    	return hotels_details_list
