import pygame

class Child:

    last_x: int
    last_y: int
    change_x: int
    change_y: int
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.color = 100, 255, 10

    def draw(self, screen):
        self.last_x = self.x
        self.last_y = self.y
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.size,self.size))

    # def move_child(self):
    #     if (key == pygame.K_d):
    #         self.move = "right"
    #         self.change_x = self.x
    #         self.change_y = self.y
    #     elif (key == pygame.K_a):
    #         self.move = "left"
    #         self.change_x = self.x
    #         self.change_y = self.y
    #     elif (key == pygame.K_w):
    #         self.move = "up"
    #         self.change_x = self.x
    #         self.change_y = self.y
    #     elif (key == pygame.K_s):
    #         self.move = "down"
    #         self.change_x = self.x
    #         self.change_y = self.y