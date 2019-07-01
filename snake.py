import random
from operator import add

import pygame

import child_element


class Snake:
    x: int
    change_x: int
    change_y: int
    color = 100, 100, 10
    move = "stop"
    childs = []
    last_x: int
    last_y: int
    size = 30
    movements = {
        "stop": (0, 0),
        "left": (-size, 0),
        "right": (size, 0),
        "up": (0, -size),
        "down": (0, size),
    }

    def __init__(self):
        self.x = 90
        self.y = 90
        self.speed = 0.1

    def draw(self, screen, screen_size):
        self.set_last_position()
        self.x, self.y = tuple(
            map(add, (self.x, self.y), Snake.movements[self.move]))

        if(self.x + Snake.size >= screen_size[0]):
            self.x = self.x - screen_size[0]
        if(self.x < 0):
            self.x += screen_size[0]
        if(self.y + Snake.size >= screen_size[1]):
            self.y -= screen_size[1]
        if(self.y < 0):
            self.y += screen_size[1]
        # check if collision with child
        self.collision_child()
        self.move_childs()

        pygame.draw.rect(screen, self.color,
                         (self.x, self.y, Snake.size, Snake.size))
        for child in self.childs:
            child.draw(screen)

    def move_snake(self, key):
        if (key == pygame.K_d):
            self.move = "right"
        elif (key == pygame.K_a):
            self.move = "left"
        elif (key == pygame.K_w):
            self.move = "up"
        elif (key == pygame.K_s):
            self.move = "down"

    def collision_food(self, element):
        if(self.x + Snake.size >= element.x and self.x < element.x + element.radius and self.y + Snake.size >= element.y and self.y < element.y + element.radius):
            if(len(self.childs) == 0):
                self.childs.append(child_element.Child(
                    self.last_x, self.last_y, Snake.size))
            else:
                self.childs.append(child_element.Child(
                    self.childs[-1].last_x, self.childs[-1].last_y, Snake.size))
            self.color_change()
            return 1

    def collision_child(self):
        for child in self.childs:
            if(self.x == child.x and self.y == child.y):
                self.move = "stop"

    def set_last_position(self):
        self.last_x = self.x
        self.last_y = self.y

    def move_childs(self):
        if(self.move != "stop"):
            for i in range((len(self.childs) - 1), -1, -1):
                if (i == 0):
                    self.childs[i].x = self.last_x
                    self.childs[i].y = self.last_y
                else:
                    self.childs[i].x = self.childs[i-1].last_x
                    self.childs[i].y = self.childs[i-1].last_y

    def color_change(self):
        color = random.randint(0, 255), random.randint(
            0, 255), random.randint(0, 255)
        for child in self.childs:
            child.color = color
