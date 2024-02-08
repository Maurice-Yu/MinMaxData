from tests.testMinMax import *
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRestaurantData)
    unittest.TextTestRunner(verbosity=2).run(suite)