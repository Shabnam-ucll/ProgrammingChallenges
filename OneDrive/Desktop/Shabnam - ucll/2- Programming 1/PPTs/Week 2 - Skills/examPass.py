
def examPass(result1,result2):
    lowest = min(result1,result2)
    sum = result1 + result2
    if result1 >= 50 and result2 >= 50:
        return True
    if lowest >= 45 and sum >= 100:
        return True
    if lowest < 45 and lowest >= 40 and sum >= 120:
        return True
    return False

def examPass(result1,result2):
    lowest = min(result1,result2)
    sum = result1 + result2
    succeed = False
    if lowest >= 45 and sum >= 100:
        succeed = True
    elif lowest < 45 and lowest >= 40 and sum >= 120:
        succeed = True
    return succeed


print(examPass(50,50))      # True
print(examPass(48,53))      # True
print(examPass(44,76))      # True
print(examPass(44,75))      # False



    

