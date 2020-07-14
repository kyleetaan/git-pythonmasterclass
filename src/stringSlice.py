#          0123456789012345678901234
letters = "abcdefghijklmnopqrstuvwyz"

print(letters[16:13:-1])
print(letters[4::-1])
print(letters[:-9:-1])

for i in range(1, 13):
    print("No. {0:<2} squared is {1:<3} and cubed is {2:<4}".format(i, i**2, i**3))