import unittest

def stradd(a, b):
    return a + b

class HelloTest(unittest.TestCase):
    def test_1(self):
        print ("DEBUG test_1")
        self.assertEqual(stradd("a", "b"), "ab")



suite = unittest.TestLoader().loadTestsFromTestCase(HelloTest)
# Default is True
result = unittest.TestResult()
# Call sending here.
suite(result)
if result.wasSuccessful():
    print("SUCESS")
else:
    print("Some tests failed!")
    for test, err in result.failures + result.errors:
        print(test)
        print(err)
