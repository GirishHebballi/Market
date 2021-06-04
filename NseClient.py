import requests
from Market import NseConstants


class NseClient:
    NSE_HEADER={'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
                }
    BASE_URL="https://www.nseindia.com/"

    def __init__(self):
        getCookieRequest=requests.get(self.BASE_URL, headers=self.NSE_HEADER)
        self.COOKIES=getCookieRequest.cookies;
        print(self.COOKIES)
        print(self.BASE_URL)
        print(self.NSE_HEADER)


    def do_get(self, uri_resource):
        print(self.BASE_URL + uri_resource)
        return requests.get(self.BASE_URL + uri_resource, cookies=self.COOKIES, headers=self.NSE_HEADER);

    def get_quote(self, stock_code):
        return requests.get(self.BASE_URL + NseConstants.NSE_APIS['QUOTE_EQUITY'] + stock_code, cookies=self.COOKIES, headers=self.NSE_HEADER)

