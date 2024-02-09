# takes in CSV file and outputs a nested dictionary
from RestaurantData.RestaurantData import RestaurantData
import csv
'''takes in a empty list and appends RestaurantData to it'''
def parseCSV(restaurantarg, csvpath):
    file = open(csvpath)
    csvfile = csv.DictReader(file)
    for lines in csvfile:
        newRestaurant = RestaurantData(lines.pop("Location Name"))
        linesAsFloat= {param:float(lines.get(param)) for param in lines}
        newRestaurant.setRawData(linesAsFloat)
        restaurantarg.append(newRestaurant)
            

    return restaurantarg
    
