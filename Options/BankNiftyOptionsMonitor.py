from Market.Common.FileOps import FileOps
import json

class BankNiftyOptionsMonitor:

    def __init__(self):
        pass

    def monitor(self):
        fileOps = FileOps();
        options_chain_data = fileOps.readFile("banknifty_options.json");
        options_chain = json.loads(options_chain_data)
        #print(options_chain)
        print(options_chain["records"].keys())
        options_data = options_chain["records"]["data"]
        print(len(options_data))
        print(options_data[0])
        current_price = options_data[0]["CE"]["underlyingValue"]
        current_price = int(current_price - current_price%100)
        print(current_price)



    def get_500_plus_minus_strike(self, current_price):
        thousand_list = [500, 400, 300, 200, 100 , 0 , -100, -200, -300, -400, -500]
        thousand_strike_price_list = [strikes + current_price for strikes in thousand_list]
        print(thousand_strike_price_list)
        return thousand_strike_price_list




bn = BankNiftyOptionsMonitor()
bn.monitor()
bn.get_500_plus_minus_strike(35100)