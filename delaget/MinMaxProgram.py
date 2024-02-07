from MinMax.MinMax import *
def main():
    rest1= ResterantData("test")
    print (rest1.resterantName)
    rest1.getRawData().update({"netSales": 4})
    print (rest1.getRawData().get("netSales"))
    rest1.setRawData({"sales":1000,"netSales": 4})
    rest1.setMinMaxData({"sales":1})
    rest1.setName("mcdonalds")
    rest1.setAvarageScore(1)
    restlst = []
    rest2=ResterantData("test2")
    rest2.getRawData().update({"netSales": 4})
    rest2.setRawData({"sales":2000,"netSales": 3})
    rest2.setMinMaxData({"sales":2})
    rest2.setAvarageScore(4)
    restlst.append(rest1)
    restlst.append(rest2)
    rest2.setName("wendys")
    printResterantRanking(restlst)
    print (restlst)
    calculateMinMax(restlst)
    print(rest2.getMinMaxData())
    

if __name__ == "__main__":
    main()