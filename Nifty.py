import json;
from Market.NseClient import NseClient
from Market import NseConstants

class Nifty50:

    def __init__(self):
        self.nse = NseClient()
        pass;

    def get_nifty_stock_data(self, stock_symbol):
        Nifty_api_response = self.nse.do_get(NseConstants.NSE_APIS.get("NIFTY_STOCK_HISTORICAL_DATA") + stock_symbol);
        print(Nifty_api_response)
        if Nifty_api_response.status_code != 200:
            return None
        if Nifty_api_response.text == None:
            return None
        return json.loads(Nifty_api_response.text)

    def get_nifty_options_data(self):
        Nifty_api_response =  self.nse.do_get(NseConstants.NSE_APIS.get("NIFTY_API_ALL_DATA"));
        #return json.dumps(json.loads(Nifty_api_response.text), indent=2)
        return json.loads(Nifty_api_response.text)

    def sort_by_expiry(self, Nifty_data, remove_zero_value_options):
        if remove_zero_value_options:
            Nifty_nonzero_options = list(filter(lambda options_data: options_data['value'] != 0, Nifty_data ))
        else:
            Nifty_nonzero_options = Nifty_data

        Nifty_options = {}
        for Nifty_list_value in Nifty_nonzero_options:
            if Nifty_list_value['expiryDate'] in Nifty_options:
                Nifty_options[Nifty_list_value['expiryDate']].append(Nifty_list_value)
            else:
                Nifty_options[Nifty_list_value['expiryDate']] = [];
                Nifty_options[Nifty_list_value['expiryDate']].append(Nifty_list_value)

        return Nifty_options;

    def get_nifty_all_data(self):
        Nifty_api_response =  self.nse.do_get(NseConstants.NSE_APIS.get("NIFTY_API_ALL_DATA"));
        return json.loads(Nifty_api_response.text)


    def sort_all_data_by_expiry(self, Nifty_data, remove_zero_value_options):
        if remove_zero_value_options:
            Nifty_nonzero_options = list(filter(lambda options_data: options_data['metadata']["numberOfContractsTraded"] != 0, Nifty_data ))
        else:
            Nifty_nonzero_options = Nifty_data

        Nifty_options = {}
        for Nifty_list_value in Nifty_nonzero_options:
            if Nifty_list_value['metadata']['expiryDate'] in Nifty_options:
                Nifty_options[Nifty_list_value['metadata']['expiryDate']].append(Nifty_list_value)
            else:
                Nifty_options[Nifty_list_value['metadata']['expiryDate']] = [];
                Nifty_options[Nifty_list_value['metadata']['expiryDate']].append(Nifty_list_value)

        return Nifty_options;

