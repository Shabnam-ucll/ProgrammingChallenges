from math import ceil

def orderBooks(x): # x = number of books
    bookprice = 24.95*0.6 # 40% discount 
    total = x*bookprice
    # shipping cost:
    if x>=1: # for the first book €3
        total += 3
    if x>=2: # for the remaining books €0.75 per book
        rest = x-1
        total += (rest * 0.75)
    # total as floating point with one decimal, rounded up 
    total = ceil(total*10)/10 
    return total


print(orderBooks(0))  # 0.0
print(orderBooks(1))  # 18.0
print(orderBooks(2))  # 33.7
print(orderBooks(5))  # 80.9
print(orderBooks(7))  # 112.3


