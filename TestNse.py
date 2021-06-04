from Market.NseClient import NseClient
from Market.BankNifty import BankNifty;
from Market.NiftyStocks import NiftyStocks
import json
import datetime

nseStocks = NiftyStocks()
stock_data = nseStocks.parse_all_stocks();
currentDate = "{}".format(datetime.datetime.now().strftime("%m%d%Y")).replace(" ", "_").replace(".", "_").replace(":",
                                                                                                                  "-")

f = open("Nse_stock_data" + currentDate + ".json", "w")
f.write(json.dumps(stock_data))
f.close()

f = open("Nse_stock_data.json", "w")
f.write(json.dumps(stock_data))
f.close()
#nse=NseClient()
#bank = BankNifty();
#print(bank.get_banknifty_options_data())
#print(json.dumps(bank.sort_all_data_by_expiry(bank.get_banknifty_all_data()["stocks"], True), indent=2));
#print(nse.get_quote("INFY").text);

