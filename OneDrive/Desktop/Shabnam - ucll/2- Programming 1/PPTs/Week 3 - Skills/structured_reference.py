
def control_digit(number):
    control_digit = number % 97
    if control_digit == 0:
        control_digit = 97
    return control_digit
    
print(control_digit(50)) # 50
print(control_digit(97)) # 97
print(control_digit(123456789)) # 39

def make_10_digits(number):
    return f"{number:010}"

print(make_10_digits(123)) # "0000000123"

def add_control_digit(text):
    number = int(text)
    x = control_digit(number)
    result = f"{text}{x:02}"
    return result

print(add_control_digit("0123456789")) # "012345678939"
print(add_control_digit("0123456754")) # "012345675404"
print(add_control_digit("0123456750")) # "012345675097"

def add_symbols(text):
    first_part = text[0:3]
    second_part = text[3:7]
    third_part = text[7:]
    result = f"+++{first_part}/{second_part}/{third_part}+++"
    return result

print(add_symbols("012345675404")) # "+++012/3456/78939+++"

def create_reference_number(number):
    text_10_digits = make_10_digits(number)
    text_with_control_digit = add_control_digit(text_10_digits)
    final_reference = add_symbols(text_with_control_digit)
    return final_reference

print(create_reference_number(123456789)) # "+++012/3456/78939+++"


