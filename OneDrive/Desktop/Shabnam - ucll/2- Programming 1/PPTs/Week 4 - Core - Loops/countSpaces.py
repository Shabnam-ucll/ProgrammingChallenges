def count_spaces(text):
    counter = 0
    for i in range(0,len(text)):
        if text[i] == ' ':
            counter += 1
    return counter


# alternative
def count_spaces(text):
    count = 0
    for char in text:
        if char == ' ':
            count += 1
    return count


print(count_spaces("Hello, how are you?")) # 3