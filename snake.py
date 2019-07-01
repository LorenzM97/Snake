import random
from operator import add

import pygame

import child_element


class Snake:
    x: int
    change_x: int
    change_y: int
    color = 100, 100, 10
    children = []
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
    key_mapping = {
        pygame.K_d: "right",
        pygame.K_a: "left",
        pygame.K_s: "down",
        pygame.K_w: "up"
    }

    def __init__(self):
        self.x = 90
        self.y = 90
        self.move = "stop"

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
        self.move_children()

        pygame.draw.rect(screen, self.color,
                         (self.x, self.y, Snake.size, Snake.size))
        for child in self.children:
            child.draw(screen)

    def move_snake(self, key):

        self.move = Snake.key_mapping[key] if key in Snake.key_mapping.keys(
        ) else self.move

    def collision_food(self, element):
        if(self.x + Snake.size >= element.x and self.x < element.x + element.radius and self.y + Snake.size >= element.y and self.y < element.y + element.radius):
            if(len(self.children) == 0):
                self.children.append(child_element.Child(
                    self.last_x, self.last_y, Snake.size))
            else:
                self.children.append(child_element.Child(
                    self.children[-1].last_x, self.children[-1].last_y, Snake.size))
            self.color_change()
            return True

    def collision_child(self):
        for child in self.children:
            if(self.x == child.x and self.y == child.y):
                self.move = "stop"

    def set_last_position(self):
        self.last_x = self.x
        self.last_y = self.y

    def move_children(self):
        if(self.move != "stop"):
            for i in range((len(self.children) - 1), -1, -1):
                if (i == 0):
                    self.children[i].x = self.last_x
                    self.children[i].y = self.last_y
                else:
                    self.children[i].x = self.children[i-1].last_x
                    self.children[i].y = self.children[i-1].last_y

    def color_change(self):
        color = random.randint(0, 255), random.randint(
            0, 255), random.randint(0, 255)
        for child in self.children:
            child.color = color
