from MinMax.MinMax import *
from RestaurantData.RestaurantData import *
import unittest
from hypothesis import given, strategies as st, settings,Verbosity

'''Used for testing program. Tests MinMax functions'''

class TestRestaurantData(unittest.TestCase):
    def setUp(self):
        self.restaurant = RestaurantData("name")    
        self.restaurant2 = RestaurantData("name2")
        self.restaurant3 = RestaurantData("name3")
    def tearDown(self):
        self.restaurant = None
        self.restaurant2 = None
        self.restaurant3 = None
    def test_get_methods(self):
        self.assertEqual
    
    @given(param1=st.floats(min_value=-100, max_value=100),param2=st.floats(min_value=-100, max_value=100),param3=st.floats(min_value=-100, max_value=100))
    @settings(verbosity=Verbosity.verbose, max_examples=20)
    def testMinMax(self,param1,param2,param3):
        self.setUp()
        maxparam=max(param1,param2,param3)
        minparam=min(param1,param2,param3)
        if(minparam!=maxparam):
            self.restaurant.setRawData({"sales":param1})
            self.restaurant2.setRawData({"sales":param2})
            self.restaurant3.setRawData({"sales":param3})
            restaurants=[self.restaurant,self.restaurant2,self.restaurant3]
            calculateMinMax(restaurants)
            self.assertEqual(restaurants[0].getMinMaxData(),{"sales":(param1-minparam)/(maxparam-minparam)})
            self.assertEqual(restaurants[1].getMinMaxData(),{"sales":(param2-minparam)/(maxparam-minparam)})
            self.assertEqual(restaurants[2].getMinMaxData(),({"sales":(param3-minparam)/(maxparam-minparam)}))

        self.tearDown()
    
    @given(cash=st.floats(min_value=-1, max_value=1),speed=st.floats(min_value=-1, max_value=1),discount=st.floats(min_value=-1, max_value=1))
    @settings(verbosity=Verbosity.verbose, max_examples=15)
    def testMinMax(self,cash,speed,discount):
        self.setUp()
        self.restaurant.setMinMaxData({" Cash Over/Short":cash," Discount Total Amount": discount, " Speed of Service Total Seconds": speed})
        AvarageScore(self.restaurant)
        self.assertAlmostEqual(self.restaurant.getAvarageScore(),sum([-1*abs(cash),-1*speed,-1*discount])/3)
        self.tearDown()