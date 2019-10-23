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
        second_request = scrapy.Request(url='https://www.booking.com/hotel/de/arabest-aparthotel.en-gb.html',
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
        photo_data =  [[{
"id": '142769646',
"thumb_url": 'https://r-cf.bstatic.com/images/hotel/max200/142/142769646.jpg',
"large_url": 'https://r-cf.bstatic.com/images/hotel/max1024x768/142/142769646.jpg'
,"highres_url": 'https://r-cf.bstatic.com/images/hotel/max1280x900/142/142769646.jpg'
,"orientation": 'portrait'
,"created" : '2018-05-14 15:45:26'
}
,
{
"id": '142770426',
"thumb_url": 'https://q-cf.bstatic.com/images/hotel/max200/142/142770426.jpg',
"large_url": 'https://r-cf.bstatic.com/images/hotel/max1024x768/142/142770426.jpg'
,"highres_url": 'https://q-cf.bstatic.com/images/hotel/max1280x900/142/142770426.jpg'
,"orientation": 'landscape'
,"created" : '2018-05-14 15:50:22'
}
,
{
"id": '142770423',
"thumb_url": 'https://q-cf.bstatic.com/images/hotel/max200/142/142770423.jpg',
"large_url": 'https://r-cf.bstatic.com/images/hotel/max1024x768/142/142770423.jpg'
,"highres_url": 'https://q-cf.bstatic.com/images/hotel/max1280x900/142/142770423.jpg'
,"orientation": 'landscape'
,"created" : '2018-05-14 15:50:20'
}
,
{
"id": '142770432',
"thumb_url": 'https://r-cf.bstatic.com/images/hotel/max200/142/142770432.jpg',
"large_url": 'https://r-cf.bstatic.com/images/hotel/max1024x768/142/142770432.jpg'
,"highres_url": 'https://q-cf.bstatic.com/images/hotel/max1280x900/142/142770432.jpg'
,"orientation": 'portrait'
,"created" : '2018-05-14 15:50:26'
}
,
{
"id": '149431230',
"thumb_url": 'https://r-cf.bstatic.com/images/hotel/max200/149/149431230.jpg',
"large_url": 'https://r-cf.bstatic.com/images/hotel/max1024x768/149/149431230.jpg'
,"highres_url": 'https://q-cf.bstatic.com/images/hotel/max1280x900/149/149431230.jpg'
,"orientation": 'landscape'
,"created" : '2018-06-21 14:16:59'
}
,
{
"id": '149431217',
"thumb_url": 'https://q-cf.bstatic.com/images/hotel/max200/149/149431217.jpg',
"large_url": 'https://q-cf.bstatic.com/images/hotel/max1024x768/149/149431217.jpg'
,"highres_url": 'https://r-cf.bstatic.com/images/hotel/max1280x900/149/149431217.jpg'
,"orientation": 'landscape'
,"created" : '2018-06-21 14:16:54'
}
,
{
"id": '142769591',
"thumb_url": 'https://q-cf.bstatic.com/images/hotel/max200/142/142769591.jpg',
"large_url": 'https://r-cf.bstatic.com/images/hotel/max1024x768/142/142769591.jpg'
,"highres_url": 'https://q-cf.bstatic.com/images/hotel/max1280x900/142/142769591.jpg'
,"orientation": 'landscape'
,"created" : '2018-05-14 15:45:13'
}
,
{
"id": '179396868',
"thumb_url": 'https://q-cf.bstatic.com/images/hotel/max200/179/179396868.jpg',
"large_url": 'https://q-cf.bstatic.com/images/hotel/max1024x768/179/179396868.jpg'
,"highres_url": 'https://r-cf.bstatic.com/images/hotel/max1280x900/179/179396868.jpg'
,"associated_rooms": [
'259517305'
,'259517306'
]
,"orientation": 'landscape'
,"created" : '2019-01-27 19:56:29'
}
,
{
"id": '179396883',
"thumb_url": 'https://r-cf.bstatic.com/images/hotel/max200/179/179396883.jpg',
"large_url": 'https://q-cf.bstatic.com/images/hotel/max1024x768/179/179396883.jpg'
,"highres_url": 'https://q-cf.bstatic.com/images/hotel/max1280x900/179/179396883.jpg'
,"associated_rooms": [
'259517305'
,'259517307'
,'259517308'
]
,"orientation": 'landscape'
,"created" : '2019-01-27 19:56:44'
}
,
{
"id": '179396865',
"thumb_url": 'https://q-cf.bstatic.com/images/hotel/max200/179/179396865.jpg',
"large_url": 'https://q-cf.bstatic.com/images/hotel/max1024x768/179/179396865.jpg'
,"highres_url": 'https://q-cf.bstatic.com/images/hotel/max1280x900/179/179396865.jpg'
,"associated_rooms": [
'259517303'
,'259517306'
]
,"orientation": 'landscape'
,"created" : '2019-01-27 19:56:26'
}
,
{
"id": '179396856',
"thumb_url": 'https://r-cf.bstatic.com/images/hotel/max200/179/179396856.jpg',
"large_url": 'https://r-cf.bstatic.com/images/hotel/max1024x768/179/179396856.jpg'
,"highres_url": 'https://r-cf.bstatic.com/images/hotel/max1280x900/179/179396856.jpg'
,"orientation": 'landscape'
,"created" : '2019-01-27 19:56:19'
}
,
{
"id": '179407589',
"thumb_url": 'https://r-cf.bstatic.com/images/hotel/max200/179/179407589.jpg',
"large_url": 'https://q-cf.bstatic.com/images/hotel/max1024x768/179/179407589.jpg'
,"highres_url": 'https://q-cf.bstatic.com/images/hotel/max1280x900/179/179407589.jpg'
,"associated_rooms": [
'259517302'
,'259517303'
,'259517304'
,'259517305'
,'259517306'
,'259517307'
,'259517308'
]
,"orientation": 'landscape'
,"created" : '2019-01-27 22:00:04'
}
,
{
"id": '179396844',
"thumb_url": 'https://r-cf.bstatic.com/images/hotel/max200/179/179396844.jpg',
"large_url": 'https://r-cf.bstatic.com/images/hotel/max1024x768/179/179396844.jpg'
,"highres_url": 'https://q-cf.bstatic.com/images/hotel/max1280x900/179/179396844.jpg'
,"associated_rooms": [
'259517303'
,'259517304'
,'259517305'
,'259517306'
]
,"orientation": 'landscape'
,"created" : '2019-01-27 19:56:12'
}
,
{
"id": '179400530',
"thumb_url": 'https://r-cf.bstatic.com/images/hotel/max200/179/179400530.jpg',
"large_url": 'https://q-cf.bstatic.com/images/hotel/max1024x768/179/179400530.jpg'
,"highres_url": 'https://q-cf.bstatic.com/images/hotel/max1280x900/179/179400530.jpg'
,"associated_rooms": [
'259517301'
]
,"orientation": 'landscape'
,"created" : '2019-01-27 20:34:47'
}
,
{
"id": '158008925',
"thumb_url": 'https://r-cf.bstatic.com/images/hotel/max200/158/158008925.jpg',
"large_url": 'https://q-cf.bstatic.com/images/hotel/max1024x768/158/158008925.jpg'
,"highres_url": 'https://r-cf.bstatic.com/images/hotel/max1280x900/158/158008925.jpg'
,"associated_rooms": [
'259517307'
]
,"orientation": 'landscape'
,"created" : '2018-08-19 22:33:20'
}
,
{
"id": '179396850',
"thumb_url": 'https://r-cf.bstatic.com/images/hotel/max200/179/179396850.jpg',
"large_url": 'https://q-cf.bstatic.com/images/hotel/max1024x768/179/179396850.jpg'
,"highres_url": 'https://r-cf.bstatic.com/images/hotel/max1280x900/179/179396850.jpg'
,"associated_rooms": [
'259517302'
,'259517303'
,'259517304'
,'259517306'
,'259517308'
]
,"orientation": 'portrait'
,"created" : '2019-01-27 19:56:16'
}
,
{
"id": '144027854',
"thumb_url": 'https://q-cf.bstatic.com/images/hotel/max200/144/144027854.jpg',
"large_url": 'https://r-cf.bstatic.com/images/hotel/max1024x768/144/144027854.jpg'
,"highres_url": 'https://r-cf.bstatic.com/images/hotel/max1280x900/144/144027854.jpg'
,"associated_rooms": [
'259517305'
,'259517307'
]
,"orientation": 'landscape'
,"created" : '2018-05-21 23:30:05'
}
,
{
"id": '179396871',
"thumb_url": 'https://r-cf.bstatic.com/images/hotel/max200/179/179396871.jpg',
"large_url": 'https://r-cf.bstatic.com/images/hotel/max1024x768/179/179396871.jpg'
,"highres_url": 'https://q-cf.bstatic.com/images/hotel/max1280x900/179/179396871.jpg'
,"associated_rooms": [
'259517302'
,'259517303'
,'259517304'
,'259517306'
,'259517308'
]
,"orientation": 'portrait'
,"created" : '2019-01-27 19:56:33'
}
,
{
"id": '142766229',
"thumb_url": 'https://q-cf.bstatic.com/images/hotel/max200/142/142766229.jpg',
"large_url": 'https://r-cf.bstatic.com/images/hotel/max1024x768/142/142766229.jpg'
,"highres_url": 'https://r-cf.bstatic.com/images/hotel/max1280x900/142/142766229.jpg'
,"associated_rooms": [
'259517302'
,'259517303'
,'259517304'
,'259517308'
,'259517309'
]
,"orientation": 'portrait'
,"created" : '2018-05-14 15:27:03'
}
,
{
"id": '142770291',
"thumb_url": 'https://q-cf.bstatic.com/images/hotel/max200/142/142770291.jpg',
"large_url": 'https://q-cf.bstatic.com/images/hotel/max1024x768/142/142770291.jpg'
,"highres_url": 'https://r-cf.bstatic.com/images/hotel/max1280x900/142/142770291.jpg'
,"orientation": 'portrait'
,"created" : '2018-05-14 15:49:32'
}
,
{
"id": '142770348',
"thumb_url": 'https://r-cf.bstatic.com/images/hotel/max200/142/142770348.jpg',
"large_url": 'https://q-cf.bstatic.com/images/hotel/max1024x768/142/142770348.jpg'
,"highres_url": 'https://q-cf.bstatic.com/images/hotel/max1280x900/142/142770348.jpg'
,"orientation": 'portrait'
,"created" : '2018-05-14 15:49:47'
}
,
{
"id": '179396863',
"thumb_url": 'https://q-cf.bstatic.com/images/hotel/max200/179/179396863.jpg',
"large_url": 'https://r-cf.bstatic.com/images/hotel/max1024x768/179/179396863.jpg'
,"highres_url": 'https://q-cf.bstatic.com/images/hotel/max1280x900/179/179396863.jpg'
,"associated_rooms": [
'259517303'
,'259517305'
,'259517306'
,'259517307'
,'259517308'
]
,"orientation": 'landscape'
,"created" : '2019-01-27 19:56:22'
}
,
{
"id": '142770439',
"thumb_url": 'https://q-cf.bstatic.com/images/hotel/max200/142/142770439.jpg',
"large_url": 'https://r-cf.bstatic.com/images/hotel/max1024x768/142/142770439.jpg'
,"highres_url": 'https://q-cf.bstatic.com/images/hotel/max1280x900/142/142770439.jpg'
,"orientation": 'landscape'
,"created" : '2018-05-14 15:50:31'
}
]
]
          
        data = html.document_fromstring(response.body)
        hotel_photo_list = data.xpath('//script[contains(., "b_experiments")]/text()')[0]
        start_range = re.search("hotelPhotos:", hotel_photo_list).end()
        end_range = re.search("fe_num_photo_landmarks:", hotel_photo_list).start()
        dummay_data = hotel_photo_list[start_range:end_range]

        obj = dummay_data.replace('}\n,', '}').replace('verticalAlign', '"verticalAlign"').replace('className', '"className"').replace('contains:', '"contains"').replace('thumb_className', '"thumb_className"').replace('thumb_contains', '"thumb_contains"').replace('id', '"id"').replace('thumb_url', '"thumb_url"').replace('created', '"created"').replace('large_url', '"large_url"').replace("highres_url", '"highres_url"').replace("associated_rooms", '"associated_rooms"').replace("orientation", '"orientation"') + "}"
        obj = obj + '}'
        # file = open("booking_file.html", 'wb')
        # file.write(bytes(obj, 'utf-8'))
        # file.close()

        obj2 = [obj]
        for i in [obj2[0][2:-438]]:
            print("online\n", i)

        # for i in [obj2[0][2:-438]]:
        #     print(type(i))

        # for i in obj2[0][2:-438]:
        #     print(i)
            
        for i in photo_data[0]:
            try:
                print("custome\n", i)
            except KeyError:
                print(KeyError)






        # rating_list = data.xpath('//span[contains(@class, "hp__hotel_ratings__stars")]')
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
        