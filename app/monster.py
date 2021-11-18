# app/monster.py

import random

import pygame

from app import animation

from math import copysign


class Monster(animation.AnimateSprite):
    def __init__(self, game, name, monster_size, offset=0, side="right"):
        super(Monster, self).__init__(name, monster_size) 
        self.game = game
        self.attack = 0.3
        self.monster_health = 100
        self.monster_max_health = 100
        self.rect = self.image.get_rect()
        if side == "right":
            self.rect.x = 1000 + random.randint(0, 300)
            self.direction = "right"
        elif side == "left":
            self.rect.x = 0 + random.randint(0, 30)
            self.direction = "left"

        self.rect.y = 540 - offset
        self.loop_attack = 10
        self.start_animate_sprite()

    def set_speed(self, speed):
        self.default_speed = speed
        self.velocity = random.randint(1, speed)

    def set_loop_attack(self, attack):
        self.loop_attack = attack

    def monster_dommage_attack(self, attack):
        self.monster_health -= attack
        if self.monster_health <= 0:
            self.rect.x = random.randint(0,1)*1200 + random.randint(0, 100)
            self.velocity = random.randint(1, self.default_speed)
            self.monster_health = self.monster_max_health
            self.game.add_score(self.loop_attack)

            if self.game.comet_event.is_full_loaded():
                self.game.monsters.remove(self)
                self.game.comet_event.attempt_fail()

    def animate_monster(self):
        self.animate_sprite(loop=True)

    def monster_update_health_bar(self, surface):
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.monster_max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.monster_health, 5])

    def forward(self):
        if not self.game.check_collision(self, self.game.players):
            if (self.rect.x - self.game.player.rect.x) >= 0:
                self.rect.x -= self.velocity
                self.direction = "right"
            else:
                self.rect.x += self.velocity
                self.direction = "left"
        else:
            self.game.player.player_dommage_attack(self.attack)


class Mummy(Monster):
    def __init__(self, game, side="right"):
        super(Mummy, self).__init__(game, "mummy", (130, 130), side=side)
        self.set_speed(3)
        self.set_loop_attack(5)

class Alien(Monster):
    def __init__(self, game, side="right"):
        super(Alien, self).__init__(game, "alien", (250, 250), offset=100, side=side)
        self.monster_health = 250
        self.monster_max_health = 250
        self.attack = 0.8
        self.set_speed(1)
        self.set_loop_attack(10)