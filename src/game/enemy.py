class Enemy:

    def __init__(self, name = "Enemy", hit_points = 0, lives = 1):
        self.name = name
        self.hit_points = hit_points
        self.lives = lives

    def take_damage(self, damage):
        remaining_points = self.hit_points - damage
        if remaining_points >= 0:
            self.hit_points = remaining_points
            print("I took {} points damage and have {} left".format(damage, self.hit_points))
        else:
            self.lives -= 1

    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, HP: {0.hit_points}".format(self)


class Troll(Enemy):
    
    def __init__(self, name):
        # super(Troll, self).__init__(name = name, hit_points= 23, lives = 1)
        super().__init__(name = name, hit_points= 23, lives = 1)

    def grunt(self):
        print("Me {0.name}. {0.name} stomp you!".format(self))