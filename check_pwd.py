###############################################################################
#    Andrew Clos
#    CS362 - A 2 - TDD Hands On
#    Date: 7/27/2020
#    Description: contains the password checking function
###############################################################################
VALID_NUMS = '1234567890'
VALID_LOWER = 'abcdefghijklmnopqrstuvwxyz'
VALID_UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VALID_SPECIAL = '~`!@#$%^&*()_+-='


# This function checks for a valid password
def check_pwd(testStr):

    # for counting each type of character in the string.
    numCount = 0
    lowCount = 0
    upperCount = 0
    specialCount = 0

    # check that the string is not too short or too long.
    if(len(testStr) < 8 or len(testStr) > 20):
        return False

    # loop through each character in the string
    for x in range(0, len(testStr)):

        # count the upper case and lower case characters in the string
        for y in range(0, len(VALID_LOWER)):
            if(testStr[x] == VALID_LOWER[y]):
                lowCount = lowCount + 1
            if(testStr[x] == VALID_UPPER[y]):
                upperCount = upperCount + 1

        # count the numerical characters in the string
        for y in range(0, len(VALID_NUMS)):
            if(testStr[x] == VALID_NUMS[y]):
                numCount = numCount + 1

        # count the special characters in the string
        for y in range(0, len(VALID_SPECIAL)):
            if(testStr[x] == VALID_SPECIAL[y]):
                specialCount = specialCount + 1

    # make we do not have zero of any of the character types.
    if(lowCount == 0 or upperCount == 0 or specialCount == 0 or numCount == 0):
        return False

    return True