from player import Player
from enemy import Enemy, Troll, Vampyre, VampyreKing

kyle = Player("Kyle")
print(kyle)

hatdog = Enemy("Hatdog", 11, 12)
print(hatdog)

random_monster = Troll("Jorb")
print("Ugly troll - {}".format(random_monster))

another_troll = Troll("Ug")
print(another_troll)

broda = Troll("Urg")
print(broda)

broda.grunt()
another_troll.grunt()
random_monster.grunt()

drac = Vampyre("Drac")
print(drac)

# while drac._alive:
#     drac.take_damage(1)
#     #print(drac)

king = VampyreKing("Robert")
print(king)
while king._hit_points  >= 0 and king._lives > 0:
    king.take_damage(200)
    print(king)