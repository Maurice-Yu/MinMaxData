import csv

class ResterantData:
    resterantName = None
    rawData={
        # "netSales": None
        #   ,"transactionCount": None
        #   , "cashOverShort": None
        #   , "beverageCount": None
        #   , "speedOfService" : None
        #   , "discountTotal" : None 
            }
    minMaxData={
        # "netSales": None
        #   ,"transactionCount": None
        #   , "cashOverShort": None
        #   , "beverageCount": None
        #   , "speedOfService" : None
        #   , "discountTotal" : None
              }
    avarageScore = None
    
    def __init__(self, resterantName):
        self.resterantName= resterantName
    def getRawData(self):
        return self.rawData
    def getMinMaxData(self):
        return self.minMaxData
    def getAvarageScore(self):
        return self.avarageScore
    def getName(self):
        return self.resterantName
    def setRawData(self, rawData):
        self.rawData=rawData
    def setAvarageScore(self, avarage):
        self.avarageScore = avarage
    def setMinMaxData(self,minMaxData):
        self.minMaxData=minMaxData
    def setName(self,name):
        self.resterantName = name

def main():
    rest1= ResterantData("test")
    print (rest1.resterantName)
    rest1.getRawData().update({"netSales": 4})
    print (rest1.getRawData().get("netSales"))


if __name__ == "__main__":
    main()
