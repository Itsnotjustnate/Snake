# This is the file for the snake game

import pygame
import time
import random

from pygame import display

class Snek_Game:

    def __init__(self):

        #initializes imported Pygame modules
        pygame.init()

        #display width and height variables
        dis_width = 800
        dis_height = 800

        #color palette variables (R,G,B)
        white = (255, 255, 255)
        black = (0, 0, 0)
        red = (255, 0, 0)
        blue = (0, 0, 255)

        #setting up the screen
        display = pygame.display.set_mode((dis_width, dis_height))

        pygame.display.set_caption('Snek Game')

        clock = pygame.time.Clock()

        #snake's attributes
        snek_size = 10
        snek_speed = 30 

    
    def game_loop(dis_width, dis_height, white, snek_size, blue):

        game_over = False 
        game_close = False

        x = dis_width / 2
        y = dis_height / 2
    
        _x = 0
        _y = 0

        while not game_over:

            while game_close == True:
                display.fill(white)
                pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        _x = -snek_size
                        _y = 0
                    elif event.key == pygame.K_RIGHT:
                        _x = snek_size
                        _y = 0
                    elif event.key == pygame.K_UP:
                        _x = 0
                        _y = -snek_size
                    elif event.key == pygame.K_DOWN:
                        _x = 0
                        _y = snek_size
                if x >= dis_width or x < 0 or y >= dis_height or y < 0:
                    game_close = True
                x += _x
                y += _y
                display.fill(white)
                pygame.draw.rect(display, blue, [x, y, snek_size, snek_size])
                pygame.display.update()
        
        pygame.quit()
        quit()



                