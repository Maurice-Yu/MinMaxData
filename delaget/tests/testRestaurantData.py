from ..ResterantData.ResterantData import *
import unittest
from hypothesis import given, strategies as st, settings,Verbosity
class TestResterantData(unittest.Testcase):
    def setUp(self):
        self.resterant = ResterantData()
        self.resterant.setRawData({"sales":1000})
        self.resterant.setMinMaxData({"sales":1})
        self.resterant.setName("mcdonalds")
        self.resterant.setAvarageScore(1)
    
    def tearDown(self):
        self.resterant = None
    def test_get_methods(self):
        self.assertEqual