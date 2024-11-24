def securityCode(code):
    if firstDigit(code) > secondDigit(code):
         if thirdDigit(code) % 2 == 0:
              if firstDigit(code) != thirdDigit(code):
                   return True
    return False

def checkLength(code):
    return type(code) == int and code > 99 and code < 1000
            
def firstDigit(code):
     return code // 100

def secondDigit(code):
     return (code - firstDigit(code)*100) // 10

def thirdDigit(code):
     return code - firstDigit(code)*100 - secondDigit(code)*10


