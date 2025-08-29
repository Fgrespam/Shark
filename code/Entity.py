#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.score = None
        self.health = None
        self.name = name
        self.surf = pygame.image.load('./Asset/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0

    @abstractmethod
    def move(self):
        pass

    def eat(self, fish_list):
        pass

    def take_damage(self):
        pass

    def eat2(self, lula_list):
        pass
