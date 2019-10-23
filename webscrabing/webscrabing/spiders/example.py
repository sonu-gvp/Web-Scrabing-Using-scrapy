import scrapy
from scrapy import Selector
from lxml import html
import json
from webscrabing.items import WebscrabingItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ['in.hotels.com']

    def start_requests(self):
        # yield scrapy.Request('https://in.hotels.com/search.do?resolved-location=CITY%3A1506246%3AUNKNOWN%3AUNKNOWN&destination-id=1506246&q-destination=New%20York,%20New%20York,%20United%20States%20Of%20America&q-rooms=1&q-room-0-adults=2&q-room-0-children=0',
        # 					 self.get_hotel_data)

        yield scrapy.Request('https://in.hotels.com/search/listings.json?destination-id=1506246',
        					self.get_api_data)
        


    # def get_hotel_data(self, response):
    # 	data = html.document_fromstring(response.body)
    	
    # 	summary = data.xpath("//div[@class='main-inner']/div[@class='summary']/h1/text()")
    # 	summary = summary[0].split(',')
    # 	summary = summary[-1]
    # 	data_list = data.xpath("//div[@id='listings']/ol/li/article/section")
    # 	for div in  data_list:
    		
    # 		name = div.xpath("div[@class='description resp-module']/h3[@class='p-name']/a/text()")[0]
    		
    # 		address = div.xpath("div[@class='description resp-module']/address[@class='contact']/span[@class='address']/text()")[0]

    # 		additional_details = div.xpath("div[@class='description resp-module']/div[@class='details resp-module']/div[@class='additional-details resp-module']")[0]

    # 		location_info = additional_details.xpath("div[@class='location-info resp-module']//text()")
    # 		location = location_info[0]
    # 		property_landmarks = location_info[1:]

    # 		amenities = additional_details.xpath("ul[@class='hmvt8258-amenities']//text()")
    		
    # 		reviews_box = div.xpath("div[@class='description resp-module']/div[@class='details resp-module']/div[@class='reviews-box resp-module']")[0]

    # 		guest_reviews = reviews_box.find("strong").text
    # 		trip_advisor_rating = reviews_box.xpath("div[@class='trip-advisor']/div[@class='tripadvisor-rating']/div[@class='ta-total-reviews']/text()")
    # 		print(trip_advisor_rating)

    # 		price_div = div.xpath("aside[@class='pricing resp-module']/div[@class='price']")[0]

    # 		if price_div.find("strong") is not None:
    # 			price = price_div.find("strong").text
    # 		else:
    # 			price = price_div.find("ins").text

    # 		hotels_details['name'] = name
    # 		hotels_details['address'] = address
    # 		hotels_details['price'] = price
    # 		hotels_details['summary'] = summary
    # 		hotels_details['location'] = location
    # 		hotels_details['property_landmarks'] = property_landmarks
    # 		hotels_details['amenities'] = amenities
    # 		hotels_details['guest_reviews'] = guest_reviews
    # 		hotels_details['trip_advisor_rating'] = trip_advisor_rating
    # 		hotels_details_list.append(hotels_details)
    # 	return hotels_details_list


    def get_api_data(self, response):
    	print(">>>>>>>>>>>>>>>>>>>>>")
    	hotels_details_list = []
    	
    	# variable declarations for avoiding referenced before assignment error
    	streetAddress = ''
    	postalCode = ''
    	guest_reviews = ''
    	trip_advisor_rating = ''
    	price = ''
    	amenities = ''
    	guest_reviews_number = ''

    	result = json.loads(response.body)
    	summary =  result['data']['body']['header']
    	next_page = result['data']['body']['searchResults']['pagination']


    	if 'nextPageUrl' in next_page:
    		next_page = result['data']['body']['searchResults']['pagination']['nextPageUrl']
    		next_page = 'https://in.hotels.com/search/listings.json' + next_page
	
    	for i in result['data']['body']['searchResults']['results']:
    		hotels_details = {}
    		name =  i['name']
    		hole_address =  i['address']
    		
    		if 'streetAddress' in hole_address :
    			streetAddress = i['address']['streetAddress']
    			
    		elif "postalCode" in hole_address:
    			postalCode =  i["address"]["postalCode"]
    			
    		locality =  i['address']['locality']

    		region =  i['address']['region']
    		
    		countryName =  i["address"]["countryName"]
    		
    		address = streetAddress + ','+ locality + ',' + region + ',' + postalCode + ',' + countryName

    		if 'guestReviews' in i:
    			if 'badgeText' in i['guestReviews']:
    				guest_reviews_text =  i['guestReviews']['badgeText']
    				guest_reviews = guest_reviews_text + ' ' + guest_reviews_number
    			elif 'rating' in i['guestReviews']:
    				guest_reviews_number =  i['guestReviews']['rating']
    				guest_reviews = guest_reviews_text + ' ' + guest_reviews_number
    			

    		if 'tripAdvisorGuestReviews' in i:
    			trip_advisor_rating =  str(i['tripAdvisorGuestReviews']['total']) + ' ' + 'reviews'

    		if 'ratePlan' in i:
    			price = i['ratePlan']['price']['current']
    		property_landmarks = i['geoBullets']

    		if 'popularAmenities' in i:
    			amenities = [ j['description'] for j in i['popularAmenities']]
    		
    		hotels_details['name'] = name
    		hotels_details['address'] = address
    		hotels_details['price'] = price
    		hotels_details['summary'] = summary
    		hotels_details['location'] = locality
    		hotels_details['property_landmarks'] = property_landmarks
    		hotels_details['amenities'] = amenities
    		hotels_details['guest_reviews'] = guest_reviews
    		hotels_details['trip_advisor_rating'] = trip_advisor_rating
    		hotels_details_list.append(hotels_details)
    		print("hotels_details \t >>>>>>>", hotels_details)
    		print("hotels_details_list \t>>>>>>>>", hotels_details_list)
    		print("\n\n\n")
    	if next_page is not None:
    		print(">>>>>>>>>>>>>>>>url", next_page)
    		yield response.follow(next_page, callback=self.get_api_data)

    	return hotels_details_list
    	
    	