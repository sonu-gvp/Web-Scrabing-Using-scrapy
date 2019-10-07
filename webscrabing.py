import urllib3
from bs4 import BeautifulSoup

# Create instance of urllib to get the data form browser
http = urllib3.PoolManager()

# Get the data using urls
request_data = http.request('GET', 'https://in.hotels.com/search.do?resolved-location=CITY%3A1506246%3AUNKNOWN%3AUNKNOWN&destination-id=1506246&q-destination=New%20York,%20New%20York,%20United%20States%20Of%20America&q-rooms=1&q-room-0-adults=2&q-room-0-children=0')

# check the status is ok or not
print(request_data.status)

# store the data 
paga_data = request_data.data

# To deal with html content and formate the code use the BeautifulSoup 
soup = BeautifulSoup(paga_data, features="html.parser")

# nested structure

html_page = soup.prettify()

print("\t \t Titel of the page \n\n")

print(soup.title.string)

print("\t \t Name of the hotels \n\n")

hotel_names = soup.find_all("h3", class_='p-name')

for hotel_name in hotel_names:
	print(hotel_name.string)

print("\t \t Address of the hotels \n\n")

hotel_address = soup.find_all("address", class_="contact")

for hotel_addres in hotel_address:
	print(hotel_addres.string)

print("\t \t Rating of the hotels \n\n")

hotel_ratings = soup.find_all("div" ,class_="reviews-box resp-module")

for hotel_ratins in hotel_ratings:
	print(hotel_ratins.find('strong').string)


print("\t \t price of the hotels \n\n")
hotel_prices = soup.find_all("div", class_="price")

for hotel_price in hotel_prices:
	if hotel_price.find('strong') is None:
		print("Delete price:\t", hotel_price.find('del').string)
		print("New price:\t", hotel_price.find('ins').string)
	else:
		print("Originale price:\t", hotel_price.find('strong').string)