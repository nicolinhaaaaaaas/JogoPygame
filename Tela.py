import pygame
from sys import exit

pygame.init() #inicia o programa do pygame
screen =  pygame.display.set_mode((800,400)) #largura e altura do display, da tela
pygame.display.set_caption('Tela')

Clock = pygame.time.Clock()

test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics/sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = test_font.render('Meu Jogo', False, 'Black')

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomright = (600, 300))

player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80, 300))

while True: # tem que colocar no while true que vai durar pra sempre, pra tela n sumir
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #fechando
            exit()


    screen.blit(sky_surface, (0,0)) #isso ta colocando uma surface dentro da display surface
    screen.blit(ground_surface, (0, 300))
    screen.blit( text_surface, (300, 50))

    snail_rect.x -= 4
    if snail_rect.right <= 0: snail_rect.left = 800
    screen.blit(snail_surface, snail_rect)

    player_rect.left += 1
    screen.blit(player_surface, player_rect)
    
    # desenhar todos os elementos
    #atualizar tudo
    pygame.display.update()

    Clock.tick(60) #limitando o jogo a 60 fps