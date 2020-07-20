###############################################################################
#    Andrew Clos
#    CS362 - A 2 - TDD Hands On
#    Date: 7/27/2020
#    Description: contains the credit card validation function
###############################################################################


def check_pwd(testStr):
    for x in range (0, len(testStr)):

        if(int(testStr[x]) >= 0 and int(testStr[x]) <= 9):
            return False

    return True