# takes in CSV file and outputs a nested dictionary
from RestaurantData.RestaurantData import RestaurantData
import csv
def parseCSV(restaurantarg, csvpath):
    with open(csvpath, mode='r') as file:
        csvfile = csv.DictReader(file)
        for lines in csvfile:
            print(lines)
            newRestaurant = RestaurantData(lines.pop("Location Name"))
            linesAsFloat= {param:float(lines.get(param)) for param in lines}

            newRestaurant.setRawData(linesAsFloat)
            
            restaurantarg.append(newRestaurant)
            

    return restaurantarg
    
