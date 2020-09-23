# farm_animals = {"sheep", "cows", "chickens"}

# for animal in farm_animals:
#     print(animal)

# print("=" * 40)

# farm_animals.add("jobert")
# print(farm_animals)


even = set(range(0, 40, 2))
print(even)
print(len(even))
print()
squares = {1, 4, 9, 16, 25}
print(squares)
print(len(squares))
print()
print(even.union(squares))
print(len(even.union(squares)))
print(even & squares)
print(squares.intersection(even))