import json

class NseJsonProcessor:

    def __init__(self):
        self.fileName = "Nse_stock_data.json"


    def _readFile(self, fileName):
        with open(fileName) as fileReader:
            jsonData = fileReader.read();

        return json.loads(jsonData)


    def find_volume_breakout_stocks(self):
        jsonData = self._readFile(self.fileName)
        print(jsonData.keys())
        for key in jsonData.keys():
            if jsonData[key]["volume_breakout"] != 0 and jsonData[key]["today_change"] == "UP" and jsonData[key]["sudden_variation"] != "":
                print(key)



    def find_falling_stocks_with_volume(self):
        pass



nseProc = NseJsonProcessor()
nseProc.find_volume_breakout_stocks();
