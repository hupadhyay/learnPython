import unittest
import calcu

class CalcuTest(unittest.TestCase):
    
    def testAdd(self):
        val = calcu.add(4, 7)
        self.assertEqual(val, 11) 
        
    def testDevide(self):
        val = calcu.divide(10, 5)
        self.assertEqual(val, 2) 
        
    def testDevideZero(self):
        val = calcu.divide(10, 4)
        self.assertEqual(val, 3) 
        
unittest.main()