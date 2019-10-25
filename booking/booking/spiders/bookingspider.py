# -*- coding: utf-8 -*-
import scrapy
from lxml import html
from booking import settings
import random
from datetime import datetime
import json
import re

class BookingspiderSpider(scrapy.Spider):
    name = 'bookingspider'
    allowed_domains = ['booking.com']
    def start_requests(self):
        user_agent = random.choice(settings.USER_AGENT_LIST)

        # request =  scrapy.Request(url='https://www.booking.com/hotel/de/hilton-munich-park.html',
        # 					       callback=self.get_booking_data)
        second_request = scrapy.Request(url='https://www.booking.com/hotel/de/city-aparthotel.en-gb.html',
                                    callback=self.booking_image)
        second_request.headers['USER-AGENT'] = user_agent
        yield second_request

        # request.headers['USER-AGENT'] = user_agent
        # yield request

    # def get_booking_data(self, response):
    #     data = html.document_fromstring(response.body)
    #     surroundings_list = data.xpath('//div[contains(@class, "hp-poi-content-section")]')
    #     print("surroundings_list", surroundings_list)
    #     all_data_dict = {}
    #     hole_data_list = []
    #     surrounding_list = []
    #     for all_div in surroundings_list:
    #         details_list = []
    #         heading_name_dict = {}
    #         heading_name_list = all_div.xpath('h3/text()')
    #         heading_name = ''.join(filter(lambda x: x, heading_name_list)).replace("\n","").replace("*","")
    #         li_list = all_div.xpath('ul/li')
    #         for li in li_list:
    #             name_dist_dict = {}
    #             name_list = li.xpath('div[contains(@class, "hp-poi-list__body")]/div[contains(@class, "hp-poi-list__description")]/text()')
    #             name = ''.join(filter(lambda x: x, name_list)).replace("\n","")
    #             if name == "":
    #                 name_list = li.xpath('div[contains(@class, "hp-poi-list__body")]/div[contains(@class, "hp-poi-list__description")]/span/text()')
    #                 name = ' '.join(filter(lambda x: x, name_list)).replace("\n","")
    #             dist_list = li.xpath('div[contains(@class, "hp-poi-list__body")]/span/text()')[0]
    #             dist = ''.join(filter(lambda x: x, dist_list)).replace("\n","")
    #             name_dist_dict['name'] = name
    #             name_dist_dict['dist'] = dist
    #             details_list.append(name_dist_dict)
    #         heading_name_dict['name'] = heading_name
    #         heading_name_dict['details'] = details_list
    #         surrounding_list.append(heading_name_dict)
    #     all_data_dict['surrounding'] = surrounding_list
    #     hole_data_list.append(all_data_dict)
    #     print(hole_data_list)

    # def booking_image(self,response):
    #     data = html.document_fromstring(response.body)
    #     #  gallery-side-reviews-wrapper lighter-lightbox
    #     # bh-photo-grid-thumbs-wrapper
    #     print("data>>>>>>>>>>>>>>", data)


    #     image_list = data.xpath('//div[contains(@class, "gallery-side-reviews-wrapper lighter-lightbox")]/div[contains(@class, "\nclearfix bh-photo-grid\nfix-score-hover-opacity\n")]'
    #                             '/div[contains(@class, "bh-photo-grid-thumbs-wrapper")]/div[contains(@class, "bh-photo-grid-thumbs bh-photo-grid-thumbs-s-full")]'
    #                             '/div[contains(@class, "bh-photo-grid-thumb-cell")]')
    #     print(">>>>>>>>>>>>>>image_list", image_list)
    #     for image in image_list:
    #         image_count_list = image.xpath('a/span/span/span/text()')
    #         image_count = ''.join(filter(lambda x: x, image_count_list)).replace("\n","").replace("+","")
    #         print("image_count>>>>>>>>>>", image_count)
    #     image_years = ''

    def booking_image(self, response):
          
        data = html.document_fromstring(response.body)
        hotel_image_list = data.xpath('//script[contains(., "b_experiments")]/text()')[0]
        start_range = re.search("hotelPhotos:", hotel_image_list).end()
        end_range = re.search("fe_num_photo_landmarks:", hotel_image_list).start()
        actual_image_list = hotel_image_list[start_range:end_range]
        actual_image_list = actual_image_list.replace("\n", "")

        cleaned_image_list = actual_image_list.replace('thumb_contains', '"thumb_contains"', 1).replace('thumb_className', '"thumb_className"', 1).replace('verticalAlign', '"verticalAlign"').replace('className:', '"className":', 1).replace('contains:', '"contains":',1).replace('id:', '"id":').replace('thumb_url', '"thumb_url"').replace('created', '"created"').replace('large_url', '"large_url"').replace("highres_url", '"highres_url"').replace("associated_rooms", '"associated_rooms"').replace("orientation", '"orientation"').replace('class="', "").replace('closedlock"', "").replace("'", '"').replace("}],", "}]")       
            
        image_years = []
        for image_list in [cleaned_image_list]:
            json_data = json.loads(image_list)
            image_count = len(json_data) - 1
            print("image_count : " , image_count)
            for image in json_data:
                if 'created' in image:
                    image_year = ';'.join([str(datetime.strptime(image['created'], "%Y-%m-%d %H:%M:%S").year)])
                    image_years.append(image_year)
        print("Image Years : ", image_years)


        # rating_list = data.xpath('//span[contains(@class, "hp__hotel_ratings__stars")]')
        # print("<<<<<<<<<<<<<<<<<<<rating_list>>>>>>>>>>>>>>>>>", rating_list)
        # for rating in rating_list:
        #     if rating.xpath('i[contains(@class, "\nbk-icon-wrapper")]/svg/path'):
        #         rating_star = rating.xpath('i[contains(@class, "\nbk-icon-wrapper")]/span[contains(@class, "invisible_spoken")]/text()')
        #         print("rating_star : ", rating_star)
        #     elif rating.xpath('i[contains(@class, "\nbk-icon-wrapper")]/svg/circle'):
        #         rating_circle = len(rating.xpath('i[contains(@class, "\nbk-icon-wrapper")]/svg/circle'))
        #         print("rating_circle : ", rating_circle)
        #     elif rating.xpath('span/svg'):
        #         rating_square = len(rating.xpath('span/svg'))
        #         print("rating_square : ", rating_square)

        # file = open("booking_file.html", 'wb')
        # file.write(response.body)
        # file.close()

         
        # image_list = data.xpath('//div[contains(@id, "photo_wrapper")]//div/@data-photo-"created"')
        # image_count = len(image_list)
        # image_years = ';'.join([str(datetime.strptime(dt, "%Y-%m-%d %H:%M:%S").year) for dt in image_list])
        # print("image_count : ", image_count)
        # print("image_years : ", image_years)
        