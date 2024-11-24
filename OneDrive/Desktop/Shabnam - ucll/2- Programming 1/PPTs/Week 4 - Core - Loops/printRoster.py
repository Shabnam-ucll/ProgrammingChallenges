def print_roster():
    for char in "abcde":
        row = ""
        for i in range(1,4):
            row += f"{char}{i}\t"
        print(row)

# alternative
def print_roster():
    for char in "abcde":
        print_row(char)

def print_row(char):
    row = ""
    for i in range(1,4):
        row += f"{char}{i}\t"
    print(row)


print_roster()