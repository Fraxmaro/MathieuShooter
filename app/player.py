# app/player.py

import pygame

from app import animation
from app.weapon import Weapon


RESTART_BY_SCD = 60
PLAYER_ATTACK = 20
POSITION_IMG_X, POSITION_IMG_Y = 450, 500
PLAYER_HEALTH = PLAYER_MAX_HEALTH = 100
VITESSE_DEPLACEMENT_JOUEUR = 2.5
print("Vitesse deplacement joueur =",VITESSE_DEPLACEMENT_JOUEUR)


class Player(animation.AnimateSprite):

    def __init__(self, game):
        super(Player, self).__init__("player")
        self.game = game
        self.player_health = PLAYER_HEALTH
        self.player_max_health = PLAYER_MAX_HEALTH
        self.attack = PLAYER_ATTACK
        self.weapon = pygame.sprite.Group()
        self.velocity = VITESSE_DEPLACEMENT_JOUEUR
        self.jump_speed = 20
        self.jump_speed_max = 20
        self.rect = self.image.get_rect()
        self.rect.x = POSITION_IMG_X
        self.rect.y = POSITION_IMG_Y
        self.direction = "right"

    def player_dommage_attack(self, attack):
        if self.player_health - attack > attack:
            self.player_health = self.player_health - attack
        else:
            self.game.game_over()

    def animate_player(self):
        self.animate_sprite()

    def update_player_health_bar(self, surface):        
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 50, self.rect.y + 20, self.player_max_health, 7])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 50, self.rect.y + 20, self.player_health, 7])

    def launch_weapon(self):
        self.weapon.add(Weapon(self))
        self.start_animate_sprite()
        self.game.sound_manager.play('tir')

    def move_right(self):
        if not self.game.check_collision(self, self.game.monsters):
            self.rect.x += self.velocity

        self.direction = "right"

    def move_left(self):
        self.rect.x -= self.velocity
        self.direction = "left"

    def jump(self):
        if self.rect.y == 500:
            self.jump_speed = self.jump_speed_max

        self.rect.y = min(self.rect.y - self.jump_speed, 500)
        self.jump_speed -= 1
