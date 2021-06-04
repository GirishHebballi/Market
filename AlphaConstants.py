ALPHA_CONSTANTS = {
    'BASE_URL' : "https://www.alphavantage.co/",
    'API_KEY' : "FYOCWS4AHJ1D09F4",
    'API_KEYS' : ['FYOCWS4AHJ1D09F4', 'RFSCJ8HGPSEU3R7O', '6AOG6JMOGWQGJA04']

}


def api_key_generator():
    indx = 0;
    while True:
        print("Index selected is ")
        print(indx)
        key = ALPHA_CONSTANTS['API_KEYS'][indx]
        indx = indx + 1
        indx = indx%3
        yield key