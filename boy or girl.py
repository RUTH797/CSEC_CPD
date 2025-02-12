username = raw_input().strip()

unique_characters = len(set(username))

if unique_characters % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
