class Hero():

    def __init__(self, name, health = 100, attack_power = 20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def atack(other):
        pass

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

class Game():

    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def start(self):
        pass



player = Hero("Knight")
computer = Hero("Monster")
game = Game(player, computer)
game.start()