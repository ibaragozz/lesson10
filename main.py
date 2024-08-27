class Hero():
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -= self.attack_power
        if other.is_alive():
            print(f"{self.name} атакует {other.name} и наносит {self.attack_power} очков урона. Осталось {other.health} очков здоровья.")
        else:
            print(f"{self.name} атакует {other.name} и наносит {self.attack_power} очков урона. {other.name} погибает.")

    def is_alive(self):
        return self.health > 0

class Game():
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def start(self):
        while self.player.is_alive() and self.computer.is_alive():
            self.player.attack(self.computer)
            if self.computer.is_alive():  # Проверяем, жив ли компьютер, перед тем как он атакует
                self.computer.attack(self.player)
                if not self.player.is_alive():  # Проверяем, жив ли игрок, после атаки монстра
                    print(f"{self.player.name} погибает.")

player = Hero("Knight")
computer = Hero("Monster")
game = Game(player, computer)
game.start()
