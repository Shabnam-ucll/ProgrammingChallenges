from math import ceil

def orderBooks(x,private_person): # x = number of books, private_person = True/False
    bookprice = 24.95
    if not private_person:
        bookprice = bookprice*0.6 # 40% discount 
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


print(orderBooks(0,True))  # 0.0
print(orderBooks(0,False))  # 0.0
print(orderBooks(1,True))  # 28.0
print(orderBooks(1,False))  # 18.0
print(orderBooks(2,True))  # 53.7
print(orderBooks(2,False))  # 33.7
print(orderBooks(5,True))  # 130.8
print(orderBooks(5,False))  # 80.9
print(orderBooks(7,True))  # 182.2
print(orderBooks(7,False))  # 112.3




