# takes in CSV file and outputs a nested dictionary
from ResterantData.ResterantData import ResterantData
import csv
def parseCSV(resterantobj, csvpath):
    with open(csvpath, mode='r') as file:
        csvfile = csv.DictReader(file)
        resterantNum=0
        for lines in csvfile:
            resterantobj[resterantNum].rawData=lines
            resterantNum+=1

    return resterantobj
    
