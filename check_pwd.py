###############################################################################
#    Andrew Clos
#    CS362 - A 2 - TDD Hands On
#    Date: 7/27/2020
#    Description: contains the credit card validation function
###############################################################################


def check_pwd(testStr):
    if(int(testStr) >= 0 and int(testStr) <= 9):
        return False

    return True