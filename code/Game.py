#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()  # initialize pygame
        self.window = pygame.display.set_mode(size=(600, 480))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()

            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         pygame.quit()
            #         quit()  # fechar pygame
