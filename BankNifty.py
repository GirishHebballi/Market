import json;
from Market.NseClient import NseClient
from Market import NseConstants


class BankNifty:

    def __init__(self):
        self.nse = NseClient()
        pass;

    def get_banknifty_options_data(self):
        banknifty_api_response =  self.nse.do_get(NseConstants.NSE_APIS.get("BANKNIFTY_API_RESOURCE"));
        #return json.dumps(json.loads(banknifty_api_response.text), indent=2)
        return json.loads(banknifty_api_response.text)

    def sort_by_expiry(self, banknifty_data, remove_zero_value_options):
        if remove_zero_value_options:
            banknifty_nonzero_options = list(filter(lambda options_data: options_data['value'] != 0, banknifty_data ))
        else:
            banknifty_nonzero_options = banknifty_data

        banknifty_options = {}
        for banknifty_list_value in banknifty_nonzero_options:
            if banknifty_list_value['expiryDate'] in banknifty_options:
                banknifty_options[banknifty_list_value['expiryDate']].append(banknifty_list_value)
            else:
                banknifty_options[banknifty_list_value['expiryDate']] = [];
                banknifty_options[banknifty_list_value['expiryDate']].append(banknifty_list_value)

        return banknifty_options;

    def get_banknifty_all_data(self):
        banknifty_api_response =  self.nse.do_get(NseConstants.NSE_APIS.get("BANKNIFTY_API_ALL_DATA"));
        return json.loads(banknifty_api_response.text)


    def sort_all_data_by_expiry(self, banknifty_data, remove_zero_value_options):
        if remove_zero_value_options:
            banknifty_nonzero_options = list(filter(lambda options_data: options_data['metadata']["numberOfContractsTraded"] != 0, banknifty_data ))
        else:
            banknifty_nonzero_options = banknifty_data

        banknifty_options = {}
        for banknifty_list_value in banknifty_nonzero_options:
            if banknifty_list_value['metadata']['expiryDate'] in banknifty_options:
                banknifty_options[banknifty_list_value['metadata']['expiryDate']].append(banknifty_list_value)
            else:
                banknifty_options[banknifty_list_value['metadata']['expiryDate']] = [];
                banknifty_options[banknifty_list_value['metadata']['expiryDate']].append(banknifty_list_value)

        return banknifty_options;

