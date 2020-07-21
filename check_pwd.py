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

def check_pwd(testStr):
    numCount = 0
    lowerCount = 0
    upperCount = 0
    specialCount = 0

    if(len(testStr) < 8):
        return False
    
    for x in range (0, len(testStr)):    
        
        for y in range (0, len(VALID_LOWER)):
            if(testStr[x] == VALID_LOWER[y]):
                lowerCount = lowerCount + 1
            if(testStr[x] == VALID_UPPER[y]):
                upperCount = upperCount + 1    
        
        for y in range (0, len(VALID_NUMS)):
            if(testStr[x] == VALID_NUMS[y]):
                numCount = numCount + 1
        
        for y in range (0, len(VALID_SPECIAL)):
            if(testStr[x] == VALID_SPECIAL[y]):
                specialCount = specialCount + 1
        
    if(lowerCount == 0 or upperCount == 0 or specialCount == 0):
        return False

    return True