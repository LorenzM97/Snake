import random, pygame

class Food:

    def __init__(self, width, height):
        self.x = random.randint(30, width - 30)
        self.y = random.randint(30, height -30)
        self.radius = 15
        self.color = 0, 50, 110

    def draw(self, screen):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius,0)

    def change_position(self, width, height):
        self.x = random.randint(30, ((width - 30) * 30) // 30)
        self.y = random.randint(30, ((height - 30)* 30) // 30)