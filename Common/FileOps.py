

class FileOps:

    def __init__(self):
        pass

    def readFile(self, fileName):
        print(fileName)
        with open(fileName, 'r') as file:
            data = file.read().replace('\n', '')

        #print(data)
        return data;