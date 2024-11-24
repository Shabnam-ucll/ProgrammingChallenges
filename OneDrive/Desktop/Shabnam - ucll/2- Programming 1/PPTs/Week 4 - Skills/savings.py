
def years_to_target(investment,yearly_rate,target_amount):
    years = 0
    while investment < target_amount:
        years += 1
        investment += investment * yearly_rate/100
    return years

print(years_to_target(500,5,1000)) # 15

