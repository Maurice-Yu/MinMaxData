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
                # score = restaurants[restaurantNum].getRawData().get(scoreType)
                # print((score - minScore)/(maxScore-minScore))
                rawScore = restaurants[restaurantNum].getRawData()[scoreType]
                normalizedscore=((rawScore - minScore)/(maxScore-minScore))
                restaurants[restaurantNum].getMinMaxData().update({scoreType: normalizedscore})
                restaurants[restaurantNum].setMinMaxData(restaurants[restaurantNum].getMinMaxData().copy())
                ''' need to set to copy since restaurant is a mutable type'''
           
        except ZeroDivisionError:
            print("Data must have a field that has more than one unique entry")
def AvarageScore(restaurant):
    fields = [restaurant.rawData.get(field) for field in restaurant.getRawData]
    avarage = fields.sum()/len(fields)
    restaurant.setAvarageScore(avarage)    

def printrestaurantRanking(restaurants):
    restaurantAvarages = [[restaurant.getAvarageScore(),restaurant.getName()] for restaurant in restaurants]
    print(restaurantAvarages)
    def returnindextwo(e):
        print(e)
        return e[0]
    rankedrestaurants = sorted(restaurantAvarages, key= lambda e: e[0])
    print(rankedrestaurants)
    for i in rankedrestaurants:
        print (i)
