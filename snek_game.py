# This is the file for the snake game

import pygame
import time
import random

class Snek_Game:

    def __init__(self):
        pygame.init()

        display_width = 800
        display_height = 800

        white = (255,255,255)
        black = (0,0,0)
        red = (255,0,0)
        blue = (0,0,255)

        display = pygame.display.set_mode((display_width, display_height))

        pygame.display.set_caption('Snek Game')

        clock = pygame.time.Clock()

        snek_size = 10
        snek_speed = 30

    def message(text, color):
        msg = font_style.render(text, True, color)

        display.blit(msg, [display_width/3, display_height/3])

    def run():
        



