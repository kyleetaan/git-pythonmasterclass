import shelve

blt = ["bacon", "lettuce", "tomato", "bread"]

with shelve.open("recipes") as recipes:
    recipes["blt"] = blt
    # del recipes
    for snack in recipes:
        print(snack, recipes[snack])