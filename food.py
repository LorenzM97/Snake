import random
import pygame


class Food:

    def __init__(self, screen_width, screen_height):
        self.radius = 15
        self.color = 0, 50, 110
        self.set_position(screen_width, screen_height)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color,
                           (self.x, self.y), self.radius, 0)

    def set_position(self, screen_width, screen_height):
        # subtract radius because draw.circle takes middle point x and y coordinates as parameters 
        self.x = random.randint(
            1, screen_width // 30)*30 - self.radius
        self.y = random.randint(
            1, screen_height//30)*30 - self.radius
