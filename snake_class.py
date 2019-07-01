import pygame, random
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

    def __init__(self):
        self.x = 90
        self.y = 90
        self.size = 30
        self.speed = 0.1

    def draw(self, screen, size):
        self.set_last_position()
        if (self.move == "stop"):
            self.x = self.x
            self.y = self.y
        elif (self.move == "right"):
            self.x += self.size
            self.y = self.y
        elif (self.move == "left"):
            self.x -=  self.size
            self.y = self.y
        elif (self.move == "up"):
            self.x = self.x
            self.y -= self.size
        elif (self.move == "down"):
            self.x = self.x
            self.y +=  self.size

        if(self.x + self.size >= size[0]):
            print("true")
            self.x = self.x - size[0]
            print()
        if(self.x < 0):
            self.x += size[0]
        if(self.y + self. size >= size[1]):
            self.y -= size[1]
        if(self.y < 0):
            self.y += size[1]
        #check if collision with child
        self.collision_child()
        self.move_childs()

        
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.size,self.size))
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
        if(self.x + self.size >= element.x and self.x < element.x + element.radius and self.y + self.size >= element.y and self.y < element.y + element.radius ):
            if(len(self.childs) == 0):
                self.childs.append(child_element.Child(self.last_x, self.last_y, self.size))
            else:
                self.childs.append(child_element.Child(self.childs[-1].last_x, self.childs[-1].last_y, self.size))
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
            for i in range((len(self.childs) -1), -1, -1):
                if (i == 0):
                    self.childs[i].x = self.last_x
                    self.childs[i].y = self.last_y
                else:
                    self.childs[i].x = self.childs[i-1].last_x
                    self.childs[i].y = self.childs[i-1].last_y

    def color_change(self):
        color = random.randint(0, 256), random.randint(0, 256), random.randint(0, 256)
        for child in self.childs:
            child.color = color
