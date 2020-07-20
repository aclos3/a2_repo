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
        input =  1
        self.assertFalse(check_pwd(input), True)

if __name__ == '__main__':
    unittest.main()