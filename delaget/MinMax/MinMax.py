from ResterantData.ResterantData import ResterantData
from ParseCSV.ParseCSV import *
def calculateMinMax(resterants):
    minimumScore = {}
    maximumScore = {}
    ''' breadth first calculation: iterates through the fields in a resterant
    calculates the minimum and maximium value for the field
    then goes through each resterant and updates the coresponding minmax value
    '''
    for scoreType in resterants[0].getRawData():
        
        minimumScore.update({scoreType:resterants[0].getRawData().get(scoreType)})
        maximumScore.update({scoreType:resterants[0].getRawData().get(scoreType)})
        for resterant in resterants: #updates min and max score for each resterant for a given field
            if minimumScore.get(scoreType)>= resterant.getRawData().get(scoreType):
                minimumScore.update({scoreType:resterant.getRawData().get(scoreType)})
            if maximumScore.get(scoreType)<= resterant.getRawData().get(scoreType):
                maximumScore.update({scoreType:resterant.getRawData().get(scoreType)})
        # definitions to increase readability
        minScore = minimumScore.get(scoreType)
        maxScore = maximumScore.get(scoreType)
        # updates each resterant with its minmax score
        try:

            for resterant in resterants:
                score = resterant.getRawData().get(scoreType)
                resterant.getRawData().update({scoreType: (score - minScore)/(maxScore-minScore)})            
        except ZeroDivisionError:
            print("Data must have a field that has more than one unique entry")
    return resterants

def AvarageScore(resterant):
    fields = [resterant.rawData.get(field) for field in resterant.getRawData]
    avarage = fields.sum()/len(fields)
    resterant.setAvarageScore(avarage)    

def printResterantRanking(resterants):
    resterantAvarages = [[resterant.getAvarageScore(),resterant.getName()] for resterant in resterants]
    print(resterantAvarages)
    def returnindextwo(e):
        print(e)
        return e[0]
    rankedResterants = sorted(resterantAvarages, key= lambda e: e[0])
    print(rankedResterants)
    for i in rankedResterants:
        print (i)
def main():
    rest1= ResterantData("test")
    print (rest1.resterantName)
    rest1.getRawData().update({"netSales": 4})
    print (rest1.getRawData().get("netSales"))
    rest1.setRawData({"sales":1000})
    rest1.setMinMaxData({"sales":1})
    rest1.setName("mcdonalds")
    restlst = []
    rest2=ResterantData("test2")
    rest2.getRawData().update({"netSales": 4})
    rest2.setRawData({"sales":2000})
    rest2.setMinMaxData({"sales":2})
    rest2.setAvarageScore(4)
    restlst.append(rest1)
    restlst.append(rest2)
    printResterantRanking(restlst)
    calculateMinMax(restlst)
    print(rest2.getMinMaxData())
    

if __name__ == "__main__":
    main()