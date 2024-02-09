from MinMax.MinMax import *
from ParseCSV.ParseCSV import *

def main(argv):
    if len(argv)<2:
        raise Exception("Usage: args <path to csv file>")
    path = argv[1]
    lst=[]
    try:
        parseCSV(lst,path)
    
    except FileNotFoundError:
        print("file: "+path+"is not found")
        return
    
    calculateMinMax(lst)
    for i in lst:
        AvarageScore(i)
    printrestaurantRanking(lst)
    return

if __name__ == "__main__":
    from sys import argv
    main(argv)
