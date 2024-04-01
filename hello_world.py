import unittest
	
class TestString(unittest.TestCase):
	
	def test_add(self):
	    a = int(input("First Number:"))
	    b = int(input("Second Number:"))
	    c = int(a * b)
	    print(c,"akshay")
	    self.assertEqual(c, 21)

if __name__ == '__main__': 
    unittest.main() 