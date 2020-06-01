import unittest

class test_data(unittest.TestCase):
    def test_data_children(self,namelist):
        actuallist=["ACCT400","ACCT500","ACCT600"]
        self.assertEqual(actuallist,namelist)
    
    def test_data_paid(self,paidlist):
        actuallist=["600","70","0"]
        self.assertEqual(actuallist,paidlist)
    
    def test_data_due(self,duelist):
        actuallist=["10000","40","0"]
        self.assertEqual(actuallist,duelist)
    
