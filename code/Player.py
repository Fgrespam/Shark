#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

import pygame.key

from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH
from code.Entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.score = 0
        self.health = 3  # Player 1 tem 3 vidas
        self.last_hit_time = 3  # tempo do último dano
        self.invincibility_duration = 3000  # em milissegundos (1 segundo)

    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_UP] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_DOWN] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_RIGHT] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]

    def take_damage(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_hit_time > self.invincibility_duration:
            self.health -= 1
            self.last_hit_time = current_time
            print(f'{self.name} perdeu 1 vida! Vidas restantes: {self.health}')

    def eat(self, fish_list):
        for fish in fish_list:
            if self.rect.colliderect(fish.rect):
                fish.rect.left = WIN_WIDTH  # reposiciona peixe
                fish.rect.top = random.randint(50, WIN_HEIGHT - 50)
                self.score += 2
                if self.score == 20 or self.score == 40 or self.score == 100:
                    self.health += 1

    def eat2(self, lula_list):
        for lula in lula_list:
            if self.rect.colliderect(lula.rect):
                lula.rect.left = WIN_WIDTH  # reposiciona peixe
                lula.rect.top = random.randint(50, WIN_WIDTH - 50)
                self.score += 2
                if self.score == 20 or self.score == 40 or self.score == 100:
                    self.health += 1

        pass
