#How to use math function
from math import pi, pow
from pickle import FALSE

def vol(radius):
    return 4/3 * pi * pow(radius, 3)

volume = vol(4)
print(f'volumen of sphere is {volume:.2f}')

#To check range..
def checkRange(lower, upper, value):
    return value in range(lower, upper)

print(checkRange(5, 15, 10))
print(checkRange(10, 25, 5))

# Test lower and upper function
def countLowerUpper(myStr):
    countLower = 0;
    countUpper = 0;
    
    for ctr in myStr:
        if ctr.islower():
            countLower += 1
        elif ctr.isupper():
            countUpper += 1
        else:
            pass
            
    print(f'Number of lower character: {countLower}')
    print(f'Number of upper character: {countUpper}')

countLowerUpper('IndiA is a great CounTry')

#Palindrom Check 1
def checkPalndrom(myStr):
    localStr = myStr[::-1]
    if myStr == localStr:
        return True
    else:
        return False
    
print(checkPalndrom('madam'))
print(checkPalndrom('loop'))

#Palindrom Check 2
def checkPalindrom2(myStr):
    end = len(myStr)
    # // is a integer division while / is float division
    for i in (0, end//2):
        if myStr[i] == myStr[end-1-i]:
            continue
        else:
            return False
    return True

print(checkPalindrom2('madam'))
print(checkPalindrom2('loop'))

#Pangram Check 
def checkPangram(myStr):
    print(f'Length of given string is {len(myStr)}')
    alphaSet = {'a','b','c','d','e','f','g','h','i','j','k','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
    ctrSet = set();
    
    for ctr in myStr:
        ctrSet.add(ctr)
    
    if len(alphaSet - ctrSet) == 0:
        print('It is pangram sentence')
    else:
        print('It is not pangram sentence')

checkPangram("the quick brown fox jumps over the lazy dog")
checkPangram("Bharat mata ki jai")
        