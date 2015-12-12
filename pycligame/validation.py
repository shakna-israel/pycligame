class Player(object):
    def __init__(self):
        self.healthmax = 100
        self.healthmin = 0
        self.strengthmax = 100
        self.strengthmin = 0
        self.foodmax = 100
        self.foodmin = 0
    
    def validate_health(self, playerObj):
        if playerObj.health > self.healthmax:
            playerObj.health = self.healthmax
        elif playerObj.health < self.healthmin:
            playerObj.health = self.healthmin

    def validate_strength(self, playerObj):
        if playerObj.strength > self.strengthmax:
            playerObj.strength = self.strengthmax
        elif playerObj.strength < self.strengthmin:
            playerObj.strengh = self.strengthmin

    def validate_food(self, playerObj):
        if playerObj.food > self.foodmax:
            playerObj.food = self.foodmax
        elif playerObj.food < self.foodmin:
            playerObj.food = self.foodmin

    def validate(self, playerObj):
        self.validate_health(playerObj)
        self.validate_strength(playerObj)
        self.validate_food(playerObj)
