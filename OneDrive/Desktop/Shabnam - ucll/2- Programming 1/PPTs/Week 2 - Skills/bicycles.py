def rentbicycles(num_bikes,rental_days,is_member,insurance):
    basePrice = 5
    if is_member:
        basePrice *= 0.85
    if insurance:
        basePrice += 2
    price = basePrice * num_bikes * rental_days
    if num_bikes == 2:
        price += 3
    elif num_bikes >= 3:
        price += 6
    return price

