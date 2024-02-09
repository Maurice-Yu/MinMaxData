from RestaurantData.RestaurantData import RestaurantData
from ParseCSV.ParseCSV import *
def calculateMinMax(restaurants):

    ''' breadth first calculation: iterates through the fields in a restaurant
    calculates the minimum and maximium value for the field
    then goes through each restaurant and updates the coresponding minmax value
    '''

    for scoreType in restaurants[0].getRawData().copy():
        minimumScore = {}
        maximumScore = {}
        minimumScore.update({scoreType:restaurants[0].getRawData().get(scoreType)})
        maximumScore.update({scoreType:restaurants[0].getRawData().get(scoreType)})
        for restaurant in restaurants: #updates min and max score for each restaurant for a given field
            if minimumScore.get(scoreType)>= restaurant.getRawData().get(scoreType):
                minimumScore.update({scoreType:restaurant.getRawData().get(scoreType)})
            if maximumScore.get(scoreType)<= restaurant.getRawData().get(scoreType):
                maximumScore.update({scoreType:restaurant.getRawData().get(scoreType)})
        # definitions to increase readability
        minScore = minimumScore.get(scoreType)
        maxScore = maximumScore.get(scoreType)
        # updates each restaurant with its minmax score
        try:

            for restaurantNum in range(len(restaurants)):
                rawScore = restaurants[restaurantNum].getRawData()[scoreType]
                normalizedscore=((rawScore - minScore)/(maxScore-minScore))
                restaurants[restaurantNum].getMinMaxData().update({scoreType: normalizedscore})
                restaurants[restaurantNum].setMinMaxData(restaurants[restaurantNum].getMinMaxData().copy())
                ''' need to set to copy since restaurant is a mutable type'''
        except ZeroDivisionError:
            print("Data must have a field that has more than one unique entry")

'''Sets the avarage score for a restaurant. You can add modifications to types different types of fields'''
def AvarageScore(restaurant):
    data=restaurant.getMinMaxData()
    adjustedData=data.copy()
    try:
        adjustedData.update({" Cash Over/Short":-1*abs(adjustedData.get(" Cash Over/Short"))})
        adjustedData.update({" Discount Total Amount":-1*(adjustedData.get(" Discount Total Amount"))})
        adjustedData.update({" Speed of Service Total Seconds":-1*(adjustedData.get(" Speed of Service Total Seconds"))})
    finally:
        avarage = sum(adjustedData.values())/len(adjustedData.values())
        restaurant.setAvarageScore(avarage)
        print (restaurant.getAvarageScore())    

'''prints the ranking for the best restaurants'''
def printrestaurantRanking(restaurants):
    restaurantAvarages = [[restaurant.getAvarageScore(),restaurant.getName()] for restaurant in restaurants]
    rankedrestaurants = sorted(restaurantAvarages, key= lambda e: e[0],reverse=True)
    for i in rankedrestaurants:
        print (i[1])
