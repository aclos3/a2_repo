###############################################################################
#    Andrew Clos
#    CS362 - A 2 - TDD Hands On
#    Date: 7/27/2020
#    Description: contains the test cases of the check_pwd function
###############################################################################


import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):
    def test1(self):
        input = "1"
        self.assertFalse(check_pwd(input))

    def test2(self):
        input = "2"
        self.assertFalse(check_pwd(input))
    
    def test3(self):
        input = "11"
        self.assertFalse(check_pwd(input))

    def test4(self):
        input = "a"
        self.assertFalse(check_pwd(input))
    
    def test5(self):
        input = "aaaaaaaa"
        self.assertFalse(check_pwd(input))
    
    def test6(self):
        input = "baaaaaaa"
        self.assertFalse(check_pwd(input))

    def test7(self):
        input = "BAAAAAAA"
        self.assertFalse(check_pwd(input))

    def test8(self):
        input = "~`!@#$%^&*()_+-="
        self.assertFalse(check_pwd(input))

    def test9(self):
        input = "!aBcDeFg"
        self.assertFalse(check_pwd(input))

    def test10(self):
        input = "!aBcDeFg2"
        self.assertFalse(check_pwd(input))
    
    def test11(self):
        input = "!aBcDeFg2!aBcDeFg2!aBcDeFg2"
        self.assertFalse(check_pwd(input))
        
if __name__ == '__main__':
    unittest.main()