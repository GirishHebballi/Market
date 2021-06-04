from Market.StockList import INDIA_STOCK_LIST
from Market.Nifty import Nifty50
from Market.NseProcessor import NseProcessor
import json
import datetime

class NiftyStocks:
    def __init__(self):
        self.STOCK_DATA = {}
        pass

    def parse_all_stocks(self):
        nifty = Nifty50()
        write_index = 0
        for stock_symbol in INDIA_STOCK_LIST:
            stock_data = nifty.get_nifty_stock_data(stock_symbol)
            nseProcessor = NseProcessor()
            if stock_data == None:
                continue

            try:
                stock_tmp_data = nseProcessor.process_stock(stock_data)
            except Exception as ex:
                print("Exception in the stock")
                print(ex)
            except:
                print("Just pass as next stock needs to be processed")
                pass

            print("=========================================")
            print(stock_tmp_data)
            print("=========================================")

            self.STOCK_DATA[stock_symbol] = stock_tmp_data
            write_index =  write_index + 1
            if write_index % 25 == 0:
                currentDate = "{}".format(datetime.datetime.now().strftime("%m%d%Y")).replace(" ", "_").replace(".","_").replace(":","-")
                print(currentDate)
                f = open("Nse_stock_data"+ currentDate + ".json", "w")
                f.write(json.dumps(self.STOCK_DATA))
                f.close()

        print(self.STOCK_DATA)
        return self.STOCK_DATA



