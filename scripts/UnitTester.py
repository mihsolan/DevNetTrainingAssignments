import unittest

class test_data(unittest.TestCase):
    def test_data_children(self,namelist):
        self.count=0
        for names in namelist:
            self.assertEqual("ACCT",names[0:4])
            self.count+=1
    
    def test_data_paid(self,paidlist):
        self.assertEqual(self.count,len(paidlist))
        for data in paidlist:
            self.assertEqual(float,type(float(data)))
        
    
    def test_data_due(self,duelist):
        self.assertEqual(self.count,len(duelist))
        for data in duelist:
            self.assertEqual(float,type(float(data)))
    
