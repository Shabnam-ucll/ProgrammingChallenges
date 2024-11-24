
def count_Vowels(text):
    count = 0
    for char in text:
        if char.lower() in "aeiouy":
            count += 1
    return count

print(count_Vowels("You are looking good!")) # 10
