import pygame
import sys
from spritesheet import SpriteSheet

FPSCLOCK = 10
pygame.init()
fps_clock = pygame.time.Clock()
print(fps_clock)

H_window = 200
L_window = 400


canvas = pygame.Surface((L_window,H_window))
window = pygame.display.set_mode((L_window,H_window))
screen = window
running =True
background = canvas.fill((0,0,0))
background_position = canvas.get_rect()

filename = 'C:\\Users\\utili\\Pictures\\Adam_anim\\sprite_sheet_street_fighter_red_blond_guy.png'
my_spritesheet = SpriteSheet(filename)
L_sprite = 101
H_sprite = 120
offset=2
red_guy = my_spritesheet.get_sprite(0,H_sprite,L_sprite,H_sprite)
index = 0
while running:
    #screen.blit(pygame.Surface((L_window,H_window)), background_position)

    #pygame.display.flip()
    index = (index+1) % 10
    red_guy = my_spritesheet.get_sprite(L_sprite*index+offset,H_sprite,L_sprite,H_sprite)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
            running = False

    canvas.fill((255,255,255))
    canvas.blit(red_guy,(0,H_window-148))
    window.blit(canvas,(0,0))
    fps_clock.tick(FPSCLOCK)
    pygame.display.update()