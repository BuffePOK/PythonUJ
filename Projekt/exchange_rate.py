import requests # Moduł do obsługi adresów URL
from bs4 import BeautifulSoup # Moduł do pracy z HTML (parsing)

class Currency:
	# link do kursu walut
	USD_PLN = 'https://www.google.com/search?q=USD+in+PLN&sxsrf=AOaemvLY5Ee04icxLimZk_4oKzDVc3Dwjw%3A1638265179820&ei=W_GlYdCkMebKrgSY3oeoDw&ved=0ahUKEwiQvtyw5b_0AhVmpYsKHRjvAfUQ4dUDCA8&uact=5&oq=USD+in+PLN&gs_lcp=Cgdnd3Mtd2l6EAMyCggAEIAEEEYQggIyBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB46BwgAEEcQsAM6BwgAELADEEM6BAgjECc6CwguEIAEEMcBENEDOgUIABCABDoHCCMQ6gIQJzoLCC4QgAQQxwEQowI6BAgAEEM6BQgAEMsBOgcIABCABBAKOggIABAWEAoQHkoECEEYAFC5BVjHH2DdIWgEcAJ4AIABdYgBxgiSAQM1LjaYAQCgAQGwAQrIAQrAAQE&sclient=gws-wiz'
	PLN_USD = 'https://www.google.com/search?q=PLN+in+USD&sxsrf=AOaemvIuk1s476DHWN2-uBLCelIDdgyAkg%3A1638265185255&ei=YfGlYYP6Ds-IrwTu15DoCg&ved=0ahUKEwjDrqiz5b_0AhVPxIsKHe4rBK0Q4dUDCA8&uact=5&oq=PLN+in+USD&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeOgYIABAHEB46CAgAEAgQBxAeOgIIJjoKCAAQgAQQhwIQFDoICAAQFhAKEB5KBAhBGABQAFjvFmCdGWgAcAJ4AIABwQGIAZ4FkgEDNC4ymAEAoAEBwAEB&sclient=gws-wiz'
	EUR_PLN = 'https://www.google.com/search?q=EUR+in+PLN&sxsrf=AOaemvKlNUKXaraebSo4Vd74Gfwc5aQjbg%3A1638265410991&ei=QvKlYdv_O8fHrgT1_peoCg&ved=0ahUKEwjbqPqe5r_0AhXHo4sKHXX_BaUQ4dUDCA8&uact=5&oq=EUR+in+PLN&gs_lcp=Cgdnd3Mtd2l6EAMyCggAEMsBEEYQggIyBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB46BAgjECc6BAgAEEM6CgguEMcBENEDEEM6BQgAEIAEOgsILhCABBDHARCjAjoLCC4QgAQQxwEQrwE6CQgAEEMQRhCCAjoFCAAQywE6BwgAEAoQywE6CggAEIAEEIcCEBQ6CAgAEBYQChAeSgQIQRgAUABY0xBgvhRoAHACeACAAdUBiAGCCZIBBTQuNS4xmAEAoAEBwAEB&sclient=gws-wiz'
	PLN_EUR = 'https://www.google.com/search?q=PLN+in+EUR&sxsrf=AOaemvJxaRPQEOUEEXTYEt8bJWUWXMXNgQ%3A1638265418618&ei=SvKlYYGQJe-lrgThp6WgCA&ved=0ahUKEwiB3cui5r_0AhXvkosKHeFTCYQQ4dUDCA8&uact=5&oq=PLN+in+EUR&gs_lcp=Cgdnd3Mtd2l6EAMyCQgjECcQRhCCAjIFCAAQywEyCAgAEBYQChAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMggIABAWEAoQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjoHCAAQRxCwAzoHCAAQsAMQQzoECCMQJzoECAAQQzoECC4QQzoLCC4QgAQQxwEQowI6BQgAEIAEOgoIABCABBCHAhAUSgQIQRgAUPgGWPgVYPMXaANwAngAgAGUAYgBxweSAQM4LjKYAQCgAQHIAQrAAQE&sclient=gws-wiz'

    # Nagłówki do przekazania wraz z adresem URL
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

    # Metoda na uzyskanie kursu waluty
	def get_currency_price(self):
		# Parsing całej strony
		full_page_USD_PLN = requests.get(self.USD_PLN, headers=self.headers)
		full_page_PLN_USD = requests.get(self.PLN_USD, headers=self.headers)
		full_page_EUR_PLN = requests.get(self.EUR_PLN, headers=self.headers)
		full_page_PLN_EUR = requests.get(self.PLN_EUR, headers=self.headers)

		# Rozbieramy przez BeautifulSoup
		soup_USD_PLN = BeautifulSoup(full_page_USD_PLN.content, 'html.parser')
		soup_PLN_USD = BeautifulSoup(full_page_PLN_USD.content, 'html.parser')
		soup_EUR_PLN = BeautifulSoup(full_page_EUR_PLN.content, 'html.parser')
		soup_PLN_EUR = BeautifulSoup(full_page_PLN_EUR.content, 'html.parser')

		# Otrzymujemy potrzebną dla nas wartość i zwracamy ją
		convert_USD_PLN = soup_USD_PLN.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
		convert_PLN_USD = soup_PLN_USD.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
		convert_EUR_PLN = soup_EUR_PLN.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
		convert_PLN_EUR = soup_PLN_EUR.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
		
		course = [convert_USD_PLN[0].text, convert_PLN_USD[0].text, convert_EUR_PLN[0].text, convert_PLN_EUR[0].text]
		return course

# Tworzenie obiektu i wywoływanie metody
if __name__ == "__main__":
	currency = Currency()
	course = currency.get_currency_price()
	print("USD in PLN: " + course[0].replace(",", "."))
	print("PLN in USD: " + course[1].replace(",", "."))
	print("EUR in PLN: " + course[2].replace(",", "."))
	print("PLN in EUR: " + course[3].replace(",", "."))