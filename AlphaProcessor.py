from Market.AlphaAdv import AlphaAdv
from Market.StockList import STOCKLIST
import numpy
from functools import reduce
import time

class AlphaProcessor:

    def __init__(self):
        self.VOLUME_BREAKOUT_STOCKS = []
        self.VOLUME_BREAKOUT_DOWN_STOCKS = []
        self.REACHING_RESISTANCE_STOCKS = []
        self.VOLATILE_STOCKS = []
        self.alpha = AlphaAdv();

        pass


    def processStock(self, stock_symbol):
        resp = self.alpha.get_daily_series(stock_symbol)
        status = self.predict_breakout_resistance(resp)
        print(status)
        if status["volumeBreakout"]:
            self.VOLUME_BREAKOUT_STOCKS.append(stock_symbol)
        if status["volumeBreakoutDown"]:
            self.VOLUME_BREAKOUT_DOWN_STOCKS.append(stock_symbol)
        if status["volatileStock"]:
            self.VOLATILE_STOCKS.append((stock_symbol))

        if status["resistanceLevel"] != 0:
            self.REACHING_RESISTANCE_STOCKS.append(stock_symbol)


        return status

    def process_all_stocks(self):
        for stock_symbol in STOCKLIST:
            self.processStock(stock_symbol)
            time.sleep(13)


        print(self.VOLUME_BREAKOUT_STOCKS )
        print(self.REACHING_RESISTANCE_STOCKS)
        print(self.VOLATILE_STOCKS)
        return {"Vol" : self.VOLUME_BREAKOUT_STOCKS, "resistance" : self.REACHING_RESISTANCE_STOCKS, "volatileStocks": self.VOLATILE_STOCKS}




    def predict_breakout_resistance(self, resp):
        status = {"volumeBreakout": False, "volumeBreakoutDown" : False,"resistanceLevel": 0, "volatileStock": False}
        isStockUp = False

        print(resp["Time Series (Daily)"])
        tradeDates = list(resp["Time Series (Daily)"].keys());
        volumes = [resp["Time Series (Daily)"][tradeDate]["6. volume"] for tradeDate in tradeDates]
        closePrices = [int(float(resp["Time Series (Daily)"][tradeDate]["4. close"])) for tradeDate in tradeDates]

        todaysPrices = resp["Time Series (Daily)"][tradeDates[0]]
        yesterdaysPrices = resp["Time Series (Daily)"][tradeDates[1]]

        if todaysPrices["4. close"] > yesterdaysPrices["4. close"]:
            isStockUp = True
        else:
            isStockUp = False



        currentPrice = closePrices[0]
        twentyClosePrices = numpy.sort(closePrices[0:20])
        twentyHighPrices = twentyClosePrices[len(twentyClosePrices) - 1]
        print(twentyHighPrices)
        print(twentyClosePrices)
        print("Twenty day high price")
        print(twentyHighPrices)
        print("Twenty Day close price")
        print(twentyClosePrices[0])
        perVol = (twentyHighPrices - twentyClosePrices[0])/twentyClosePrices[0]
        print(perVol)
        volatilityPer = float(perVol * 100)

        if volatilityPer > 40:
            status["volatileStock"] = True


        twentyNearBreakOutPrice = twentyClosePrices[0] * 0.05 + twentyClosePrices[0]
        fiftyClosePrices = numpy.sort(closePrices[0:50])
        fiftyNearBreakOutPrice = fiftyClosePrices[0] * 0.05 + fiftyClosePrices[0]
        hundredClosePrices = numpy.sort(closePrices)
        hundredNearBreakOutPrice = hundredClosePrices[0] * 0.05 + hundredClosePrices[0]
        print("CurrentPrice = " + str(currentPrice))
        print("20 Close Price = " + str(twentyClosePrices[0]))
        print(twentyNearBreakOutPrice)
        print("50 Close Price = " + str(fiftyClosePrices[0]))
        print(fiftyNearBreakOutPrice)
        print("100 Close Price = " + str(hundredClosePrices[0]))
        print(hundredNearBreakOutPrice)
        #if currentPrice < twentyNearBreakOutPrice:
        #    status["resistanceLevel"] = "20"
        #elif currentPrice < fiftyNearBreakOutPrice:
        #    status["resistanceLevel"] = "50"

        if currentPrice < hundredNearBreakOutPrice:
            status["resistanceLevel"] = "100"

        todayVol = volumes[0]
        todayVolume = volumes[0]
        olderVolumes = volumes[1:]
        perChangeInVolumes = dict()
        perChangeInVolumeList = []
        indx = 0
        for oldVol in olderVolumes:
            perChange = abs((int(todayVol) - int(oldVol)) / int(oldVol) * 100)
            todayVol = oldVol
            indx = indx + 1
            # print(tradeDates)
            perChangeInVolumeList.append(int(perChange))
            perChangeInVolumes[tradeDates[indx]] = int(perChange)
        avgVolume = int(
            reduce(lambda volToday, volPrevDay: volToday + volPrevDay, perChangeInVolumeList) / len(
                perChangeInVolumeList))
        perChangeLast5DaysArray = numpy.array(perChangeInVolumeList[0:3])
        volBreakoutList = perChangeLast5DaysArray[perChangeLast5DaysArray > (avgVolume * 4)]
        len(volBreakoutList)
        print(olderVolumes)
        print(perChangeInVolumeList)
        print(perChangeInVolumes)
        print(perChangeLast5DaysArray)
        print(len(volBreakoutList))
        if len(volBreakoutList) > 0 and status["resistanceLevel"] == 0:
            if isStockUp:
                status["volumeBreakout"] = True
            else:
                status["volumeBreakoutDown"] = True
        # Check if there is a volume breakout in last 5 days
        print(avgVolume)
        print(status)
        return status


