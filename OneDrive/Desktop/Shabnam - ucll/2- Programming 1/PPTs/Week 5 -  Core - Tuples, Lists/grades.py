# DEMO TUPLE

def entrance_exam(grades):
    number_skipped = 0
    total = 0
    for grade in grades:
        if grade != None:
            total += grade
        else:
            number_skipped +=1
    average = total / (len(grades) - number_skipped)
    if number_skipped >= 2:
        return False, average
    return average >= 12 , average

# DEMO LIST

def entrance_exam(grades): 
    number_skipped = 0
    total = 0
    for i in range(len(grades)-1,-1,-1):
        if grades[i] != None:
            total += grades[i]
        else:
            number_skipped +=1
            grades.pop(i) 
    average = total / (len(grades))
    if number_skipped >= 2:
        return False, average
    return average >= 12 , average


grades = [12,None,15,12,12,12]
print(entrance_exam(grades))
print(grades)

