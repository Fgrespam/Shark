#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

import pygame
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.Const import COLOR_WHITE, WIN_HEIGHT, EVENT_ENEMY, SPAWN_TIME, WIN_WIDTH, EVENT_TIMEOUT, TIMEOUT_STEP, \
    TIMEOUT_LEVEL, ENTITY_SPEED
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.Player import Player


def is_far_enough(new_y, existing_enemies, min_distance=100):
    for enemy in existing_enemies:
        if abs(enemy.rect.top - new_y) < min_distance:
            return False
    return True


class Level:
    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int]):
        self.timeout = TIMEOUT_LEVEL  #### 20 segundos
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))
        player = EntityFactory.get_entity('Player1')
        player.score = player_score[0]  ###
        self.entity_list.append(player)
        self.entity_list.append(EntityFactory.get_entity('Enemy1', position=(WIN_WIDTH + 10, 20)))  #
        # velocidade inicial dos inimigos
        self.enemy_speed = ENTITY_SPEED['Enemy1']  # pega a velocidade inicial do Const
        self.last_increase_time = pygame.time.get_ticks()
        self.increase_interval = 20000  # 20 segundos
        self.fish_list = []
        self.lula_list = []
        for _ in range(4):
            self.fish_list.append(EntityFactory.get_entity('Fish1'))
        self.entity_list.extend(self.fish_list)
        for _ in range(1):
            self.lula_list.append(EntityFactory.get_entity('Lula1'))
        self.entity_list.extend(self.lula_list)
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)  # 100ms

    def run(self, player_score: list[int]):
        # toca a música do nível
        pygame.mixer_music.load(f'./Asset/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)  # FPS
            # verifica se já passou o intervalo para aumentar a dificuldade
            #  Desenha e move todas as entidades
            for ent in self.entity_list:
                self.window.blit(ent.surf, ent.rect)
                ent.move()
            # --- Aumenta a velocidade dos inimigos a cada 10s ---
            current_time = pygame.time.get_ticks()
            if current_time - self.last_increase_time > self.increase_interval:
                self.enemy_speed += 2
                ENTITY_SPEED['Enemy1'] = self.enemy_speed  # <<< Atualiza no Const
                self.last_increase_time = current_time
                print("Velocidade dos inimigos aumentou para:", self.enemy_speed)
            #  Verifica colisão Player x Enemy
            player = next((e for e in self.entity_list if e.name == 'Player1'), None)
            if player:
                for enemy in [e for e in self.entity_list if e.name == 'Enemy1']:
                    if player.rect.colliderect(enemy.rect):
                        player.take_damage()

                if player.health <= 0:
                    pygame.mixer.music.stop()
                    print("Game Over!")
                    return False  # sai do loop do level

            #  Verifica colisão Player x Fish
            if player:
                player.eat(self.fish_list)
                self.level_text(14, f'Pontos: {player.score}', COLOR_WHITE, (10, 25))
                self.level_text(14, f'Vidas: {player.health}', COLOR_WHITE, (10, 45))

            if player:
                player.eat2(self.lula_list)
                self.level_text(14, f'Pontos: {player.score}', COLOR_WHITE, (10, 25))
                self.level_text(14, f'Vidas: {player.health}', COLOR_WHITE, (10, 45))

            # Eventos Pygame
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_TIMEOUT:  ###
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'Player1':
                                player_score[0] = ent.score

                        return True

                # Gerar inimigos
                if event.type == EVENT_ENEMY:
                    existing_enemies = [e for e in self.entity_list if e.name == 'Enemy1']
                    max_attempts = 10  # tenta até 10 vezes encontrar posição segura
                    for _ in range(max_attempts):
                        new_y = random.randint(40, WIN_HEIGHT - 40)
                        if is_far_enough(new_y, existing_enemies):
                            self.entity_list.append(
                                EntityFactory.get_entity(entity_name='Enemy1', position=(WIN_WIDTH + 50, new_y))
                            )
                            break  # encontrou posição segura, sai do loop

            # Exibe informações do nível
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', COLOR_WHITE, (10, 5))
            # self.level_text(14, f'fps: {clock.get_fps():.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            # self.level_text(14, f'entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 20))

            # Atualiza a tela
            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
