import csv
class RestaurantData:

    restaurantName = None
    rawData={}
    minMaxData={}
    avarageScore = None
    
    def __init__(self, restaurantName):
        self.restaurantName= restaurantName
    def getRawData(self):
        return self.rawData
    def getMinMaxData(self):
        return self.minMaxData
    def getAvarageScore(self):
        return self.avarageScore
    def getName(self):
        return self.restaurantName
    def setRawData(self, rawData):
        self.rawData=rawData
    def setAvarageScore(self, avarage):
        self.avarageScore = avarage
    def setMinMaxData(self,minMaxData2):
        self.minMaxData=minMaxData2
    def setName(self,name):
        self.restaurantName = name
