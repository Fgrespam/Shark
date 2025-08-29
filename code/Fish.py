from code.Entity import Entity
from code.Const import WIN_WIDTH, WIN_HEIGHT
import random

class Fish(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.speed = random.randint(1, 3)  # velocidade aleatória

    def move(self):
        self.rect.centerx -= self.speed
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH
            self.rect.top = random.randint(50, WIN_HEIGHT - 50)