from Market.AlphaClient import AlphaClient
from Market.AlphaConstants import ALPHA_CONSTANTS

class AlphaAdv:

    def __init__(self):
        self.alphaClient= AlphaClient()


        pass

    def get_daily_series(self, stock_id):
        return self.alphaClient.do_get("TIME_SERIES_DAILY_ADJUSTED", stock_id)


    def get_volume(self, stock_id, interval="daily"):
        return self.alphaClient.do_get("OBV", stock_id, "&interval=" + interval)


    def get_overview(self, stock_id):
        self.alphaClient.do_get("OVERVIEW", stock_id)

    def get_moving_average(self, stock_id, type="simple", interval="daily", period="20"):
        fun="SMA"
        alphaClient = AlphaClient()
        if type == "simple":
            fun = "SMA"
        else:
            fun = "EMA"

        return self.alphaClient.do_get(fun, stock_id, "&series_type=open&interval=" + interval + "&time_period=" + period)


    def get_vwap(self, stock_id, interval="15min"):
        return self.alphaClient.do_get("VWAP", stock_id, "&interval=" + interval)

