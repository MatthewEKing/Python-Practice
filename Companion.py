class Companion:

    friendliness = 0

    def __init__(self, name, weapon, favorite_food):
        self.name = name
        self.weapon = weapon
        self.favorite_food = favorite_food

    def check_friendliness(self):
        isFriendly = False
        if self.friendliness <= 5:
            isFriendly = False
        else:
            isFriendly = True
        return isFriendly

    def increase_friendliness(self, amount=1):
        self.friendliness += amount

    def decrease_friendliness(self, amount=1):
        self.friendliness -= amount