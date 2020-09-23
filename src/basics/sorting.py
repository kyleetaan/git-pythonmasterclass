pangram = "The quick brown fox jumps over the lazy dog."

names = ["Duters",
         "Cynthia",
         "bong",
         "abueva"]
letters = sorted(pangram,
                 key=str.casefold)
sorted_letters = []
names.sort(key=str.casefold)
print(names)

for i, char in enumerate(letters[:-1]):
    if char == letters[i + 1]:
        continue
    else:
        sorted_letters.append(char)
print(sorted_letters)