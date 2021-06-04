from Market.AlphaAdv import AlphaAdv
from Market.AlphaProcessor import AlphaProcessor
import json
import datetime

currentDate = "{}".format(datetime.datetime.now().strftime("%m%d%Y")).replace(" ", "_").replace(".","_").replace(":","-")
print(currentDate + ".json")

#alpha= AlphaAdv()
#stockData=alpha.get_daily_proces("ENPH")
#print(stockData.text)

#print(alpha.get_daily_series("ENPH", "weekly"));
#print(alpha.get_overview("ENPH"))
#print(alpha.get_daily_series("ENPH"))

alphaProcessor = AlphaProcessor()
jsonData = alphaProcessor.process_all_stocks()
print(jsonData);
f = open("usa_stocks_" + currentDate +".json", "w")
f.write(json.dumps(jsonData))
f.close()
