import unittest
import calculator 

class TestCalculator(unittest.TestCase):

    
    def test_add(self):
        """ we are testing add func """
        obj =  calculator.MyCalculator()
        print("we are testing add func ")
        val = obj.add(10, 5)
        self.assertEqual(val, 15)

    def test_sub(self):
        """ we are testing sub functions """
        print("we are testing sub ")
        obj =  calculator.MyCalculator()
        val = obj.sub(10, 5)
        self.assertEqual(val, 5)
                
if __name__ == "__main__":
    unittest.main()
