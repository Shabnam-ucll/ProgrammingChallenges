def remove_double_space(text):
    # check if there is at least one space
    if text.find(" ")<0:
        return text
    result = text[0]
    for i in range(1,len(text)):
        if text[i] != " " or text[i-1] != " ": 
            # no space, or in case it is a space, the previous one is not a space
            result += text[i]
    # optional: result = result.strip()
    return f'"{result}"' # quoted string to show leading and trailing spaces

print(remove_double_space("   Hello     there  !   "))


