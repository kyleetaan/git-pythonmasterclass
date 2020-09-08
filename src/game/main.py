from player import Player
from enemy import Enemy, Troll

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