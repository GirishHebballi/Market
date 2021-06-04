import json

from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin

from Market.Nifty import Nifty50
from Market.BankNifty import BankNifty


app = Flask(__name__)
api = Api(app)
CORS(app)
class Options(Resource):
    def get(self):
        bank = BankNifty();
        # print(bank.get_banknifty_options_data())
        return bank.sort_all_data_by_expiry(bank.get_banknifty_all_data()["stocks"], True);


class Nifty(Resource):
    def get(self):
        nifty = Nifty50();
        return nifty.sort_all_data_by_expiry(nifty.get_nifty_all_data()["stocks"], True);

api.add_resource(Options, '/get_banknifty_data')
api.add_resource(Nifty, '/get_nifty_data')


if __name__ == '__main__':
    app.run(debug=True)