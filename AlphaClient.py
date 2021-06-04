import requests
import json
from Market.AlphaConstants import ALPHA_CONSTANTS
from Market.AlphaConstants import api_key_generator

class AlphaClient:

    def __init__(self):
        self.COOKIES = ""
        self.key = api_key_generator()

        pass

    def _build_url(self, functionKey, stock, url_args=""):
        self.url = ALPHA_CONSTANTS.get("BASE_URL") + "query?apikey=" + ALPHA_CONSTANTS.get("API_KEY")
        self.url +="&function=" + functionKey + "&symbol=" + stock + url_args
        print(self.url)
        return self.url


    def do_get(self, functionKey, stock, url_args=""):
        url = self._build_url(functionKey, stock, url_args)
        #result=requests.get(url, cookies=self.COOKIES);
        result=requests.get(url);

        self.COOKIES = result.cookies
        print(self.COOKIES)
        result = json.loads(result.content)
        print(result)
        return result
