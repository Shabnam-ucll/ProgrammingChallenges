# STEP 1

athletes = (
    "Lisa De Vries",
    "James Thompson",
    "Sophie Dubois",
    "Tomoya Sato",
    "Marta Rossi",
    "Jules Francois"
)

def print_athletes(athletes):
    for athlete in athletes:
        print(athlete)

print_athletes(athletes)


# STEP 2

athletes = [
    ("Lisa de Vries", 12.84),
    ("James Thompson", 13.21),
    ("Sophie Dubois", 12.75),
    ("Tomoya Sato", 12.90),
    ("Marta Rossi", 12.88),
    ("Jules Francois", 13.13)
]

def print_athletes(athletes):
    for athlete in athletes:
        print(athlete[0])

print_athletes(athletes)


# STEP 3

athletes = [
    ("Lisa de Vries", 12.84),
    ("James Thompson", 13.21),
    ("Sophie Dubois", 12.75),
    ("Tomoya Sato", 12.90),
    ("Marta Rossi", 12.88),
    ("Jules Francois", 13.13)
]

def findFirstAthlete(athletes):
    first = athletes[0]
    for athlete in athletes:
        if athlete[1] > first[1]:
            first = athlete
    return first

print(findFirstAthlete(athletes))


# STEP 4

athletes = [
    ("Lisa de Vries", 12.84, "Netherlands"),
    ("James Thompson", 13.21, "United States"),
    ("Sophie Dubois", 12.75, "France"),
    ("Tomoya Sato", 12.90, "Japan"),
    ("Marta Rossi", 12.88, "Italy"),
    ("Jules Francois", 13.13, "France")
]

def uniqueCountries(athletes):
    countries = []
    for athlete in athletes:
        if athlete[2] not in countries:
            countries.append(athlete[2])
    return len(countries)

print(uniqueCountries(athletes))


# STEP 5

athletes = [
    ["Lisa de Vries", 12.84, "Netherlands"],
    ("James Thompson", 13.21, "United States"),
    ("Sophie Dubois", 12.75, "France"),
    ("Tomoya Sato", None, "Japan"),
    ("Marta Rossi", None, "Italy"),
    ("Jules Francois", 13.13, "France")
]

def remove_athletes(athletes):
    for i in range(len(athletes)-1,-1,-1):
        if athletes[i][1] == None:
            # athletes.remove(athletes[i])
            athletes.pop(i)

remove_athletes(athletes)
print(athletes)


# STEP 6

copy = [
    ["Lisa de Vries", 12.84, "Netherlands"],
    ("James Thompson", 13.21, "United States"),
    ("Sophie Dubois", 12.75, "France"),
    ("Tomoya Sato", None, "Japan"),
    ("Marta Rossi", None, "Italy"),
    ("Jules Francois", 13.13, "France")
]

def copy_athletes(athletes):
    copy = []
    for athlete in athletes:
        copy.append(athlete)
    return copy

print(copy_athletes(athletes))

# TEST

copy = copy_athletes(athletes)
remove_athletes(copy)
print(copy)
print(athletes)

