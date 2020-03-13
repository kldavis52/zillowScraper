from http.cookies import SimpleCookie
from urllib.parse import urlparse, parse_qs, urlencode
import json

URL = 'https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A2%7D%2C%22usersSearchTerm%22%3A%22Miami%2C%20FL%22%2C%22mapBounds%22%3A%7B%22west%22%3A-80.352373%2C%22east%22%3A-80.142305%2C%22south%22%3A25.689672%2C%22north%22%3A25.855607%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A12700%2C%22regionType%22%3A6%7D%5D%2C%22filterState%22%3A%7B%22isForSaleByAgent%22%3A%7B%22value%22%3Afalse%7D%2C%22isForSaleByOwner%22%3A%7B%22value%22%3Afalse%7D%2C%22isNewConstruction%22%3A%7B%22value%22%3Afalse%7D%2C%22isForSaleForeclosure%22%3A%7B%22value%22%3Afalse%7D%2C%22isComingSoon%22%3A%7B%22value%22%3Afalse%7D%2C%22isAuction%22%3A%7B%22value%22%3Afalse%7D%2C%22isPreMarketForeclosure%22%3A%7B%22value%22%3Afalse%7D%2C%22isPreMarketPreForeclosure%22%3A%7B%22value%22%3Afalse%7D%2C%22isForRent%22%3A%7B%22value%22%3Atrue%7D%2C%22isAllHomes%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22isMapVisible%22%3Afalse%7D&includeMap=false&includeList=true'

# def start_URL():
#     #city = input("Search Zillow for what city: ")
#     #state = input("In what state (i.e. NC)? ")

#     URL = 'https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState=%7B%22usersSearchTerm%22%3A%22Miami%2C%20FL%22%2C%22mapBounds%22%3A%7B%22west%22%3A-80.352373%2C%22east%22%3A-80.142305%2C%22south%22%3A25.689672%2C%22north%22%3A25.855607%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A12700%2C%22regionType%22%3A6%7D%5D%2C%22filterState%22%3A%7B%22isForSaleByAgent%22%3A%7B%22value%22%3Afalse%7D%2C%22isForSaleByOwner%22%3A%7B%22value%22%3Afalse%7D%2C%22isNewConstruction%22%3A%7B%22value%22%3Afalse%7D%2C%22isForSaleForeclosure%22%3A%7B%22value%22%3Afalse%7D%2C%22isComingSoon%22%3A%7B%22value%22%3Afalse%7D%2C%22isAuction%22%3A%7B%22value%22%3Afalse%7D%2C%22isPreMarketForeclosure%22%3A%7B%22value%22%3Afalse%7D%2C%22isPreMarketPreForeclosure%22%3A%7B%22value%22%3Afalse%7D%2C%22isForRent%22%3A%7B%22value%22%3Atrue%7D%2C%22isAllHomes%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22isMapVisible%22%3Afalse%7D&includeMap=false&includeList=true'

#     return URL

def cookie_parser():
    cookie_string = 'AWSALB=P1qdh1TUdSIvv632yLZitdgEk8GEEiHEuSYPxslLLJt1KFD3SOpUs0HtKHg7InOLioEZtmeQXtMsJThZeJCr45+I0NN6eg6WMwDGg3/7WAx4NslqWKDz17tB3f8y; AWSALBCORS=P1qdh1TUdSIvv632yLZitdgEk8GEEiHEuSYPxslLLJt1KFD3SOpUs0HtKHg7InOLioEZtmeQXtMsJThZeJCr45+I0NN6eg6WMwDGg3/7WAx4NslqWKDz17tB3f8y; search=6|1582975387435%7Czpid%3D2081355783%09%01%09%09%09%09%090%09US_%09; zguid=23|%24e3f2dada-80ed-4824-96b6-a5f7513caa9f'
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    
    cookies = {}

    for key, morsel in cookie.items():
        cookies[key] = morsel.value

    return cookies


def parse_new_url(url, page_number):
    url_parsed = urlparse(url)
    query_string = parse_qs(url_parsed.query)
    search_query_state = json.loads(query_string.get('searchQueryState')[0])
    search_query_state['pagination'] = {"currentPage": page_number}
    query_string.get('searchQueryState')[0] = search_query_state
    encoded_qs = urlencode(query_string, doseq=1)
    new_url = f'https://www.zillow.com/search/GetSearchPageState.htm?{encoded_qs}'
    return new_url


