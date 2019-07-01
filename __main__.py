import sys

import pygame
from pygame import gfxdraw

import food
import snake

pygame.init()
pygame.display.set_caption('Snake')

size = width, height = 810, 600
speed = [0, 0]
red = 0
blue = 0
green = 0
black = red, blue, green
color_snake = 100, 100, 10
color_text = 200, 200, 200
score = 0

snake = snake.Snake()
food = food.Food(width, height)

screen = pygame.display.set_mode(size)

while True:
    basicfont = pygame.font.SysFont(None, 48)

    input = "Score:  %d" %  score
    text = basicfont.render(input, True, color_text, black)
    textrect = text.get_rect()
    textrect.centerx = screen.get_rect().centerx + 310
    textrect.centery = screen.get_rect().centery - 270
    if (snake.collision_food(food)):
        food.set_position(width, height)
        score += 1
        print(score)

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            # snake move
            snake.move_snake(event.key)

    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)
    # screen.blit()
    # pygame.display.flip()
    food.draw(screen)
    snake.draw(screen, size)
    screen.blit(text, textrect)
    pygame.display.update()
    screen.blit(text, textrect)
    pygame.time.wait(100)
