class Player(object):
    """A Basic Player Model"""

    def __init__(self):
        """Basic Stats Initialisation"""
        self.health = 100
        self.strength = 100
        self.food = 100

    def damage(self, amount):
        if type(amount) != type(int()):
            return False
        else:
            self.health = self.health - amount
            return self.health

    def heal(self, amount):
        if type(amount) != type(int()):
            return False
        else:
            self.health = self.health + amount
            return self.health

    def weaken(self, amount):
        if type(amount) != type(int()):
            return False
        else:
            self.strength = self.strength - amount
        return self.strength

    def strengthen(self, amount):
        if type(amount) != type(int()):
            return False
        else:
            self.strength = self.strength + amount
        return self.strength

    def starve(self, amount):
        if type(amount) != type(int()):
            return False
        else:
            self.food = self.food - amount
        return self.food

    def feed(self, amount):
        if type(amount) != type(int()):
            return False
        else:
            self.food = self.food - amount
        return self.food

    def attack(self, enemyObj):
        self.strength = self.strength - 1
        if self.strength < 0:
            self.strength = 0
            return False
        else:
            enemyObj.health = enemyObj.health - self.strength
            return True

    def defend(self, enemyObj):
        self.strength = self.strength - 1
        if self.strength < 0:
            self.strength = 0
            enemyObj.health = enemyObj.health - 1
            return False
        else:
            enemyObj.health = enemyObj.health - 2
            return True

    def make(self=False, health=False,strength=False,food=False):
        make_asset = Player()
        if health:
            make_asset.health = health
        if strength:
            make_asset.strength = strength
        if food:
            make_asset.food = food
        return make_asset

class NonPlayer(Player):
    """A Basic Non Player model"""

    def __init__(self, base_raise={"health":50,"strength":50,"food":50}):
        """Basic Instantiation"""
        super(NonPlayer, self).__init__()
        self.health = self.health + base_raise['health']
        self.strength = self.strength + base_raise['strength']
        self.food = self.food + base_raise['food']

    def damage(self, amount):
        super(NonPlayer, self).damage(amount)

    def heal(self, amount):
        super(NonPlayer, self).heal(amount)

    def weaken(self, amount):
        super(NonPlayer, self).weaken(amount)

    def strengthen(self, amount):
        super(NonPlayer, self).strengthen(amount)

    def starve(self, amount):
        super(NonPlayer, self).starve(amount)

    def feed(self, amount):
        super(NonPlayer, self).feed(amount)

    def attack(self, playerObj):
        self.strength = self.strength - 4
        if self.strength < 0:
            self.strength = 0
            return False
        else:
            playerObj.health = playerObj.health - 1
            return True

    def defend(self, playerObj):
        self.strength = self.strength - 2
        if self.strength < 0:
            self.strength = 0
            self.health = self.health - 1 
            return False
        else:
            return True

    def make(health=False,strength=False,food=False):
        make_asset = NonPlayer()
        if health:
            make_asset.health = health
        if strength:
            make_asset.strength = strength
        if food:
            make_asset.food = food
        return make_asset

class NonPlayerBoss(NonPlayer):
    """A Basic NonPlayer Boss Model"""
    def __init__(self, base_multiplier={"health":2,"strength":2,"food":2}):
        super(NonPlayerBoss, self).__init__()
        self.health = self.health * base_multiplier["health"]
        self.strength = self.strength * base_multiplier["strength"]
        self.food = self.food * base_multiplier["food"]

    def damage(self, amount):
        super(NonPlayerBoss, self).damage(amount)

    def heal(self, amount):
        super(NonPlayerBoss, self).heal(amount)

    def weaken(self, amount):
        super(NonPlayerBoss, self).weaken(amount)

    def strengthen(self, amount):
        super(NonPlayerBoss, self).strengthen(amount)

    def starve(self, amount):
        super(NonPlayerBoss, self).starve(amount)

    def feed(self, amount):
        super(NonPlayerBoss, self).feed(amount)

    def attack(self, playerObj):
        super(NonPlayerBoss, self).attack(playerObj)

    def defend(self, playerObj):
        super(NonPlayerBoss, self).defend(playerObj)

    def make(health=False,strength=False,food=False):
        make_asset = NonPlayerBoss()
        if health:
            make_asset.health = health
        if strength:
            make_asset.strength = strength
        if food:
            make_asset.food = food
        return make_asset
