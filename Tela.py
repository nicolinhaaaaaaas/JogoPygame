import pygame
from sys import exit

def display_score():
    current_time = pygame.time.get_ticks()
    score_surface = test_font.render(f'{current_time}', False, (64,64,64))
    score_rect = score_surface.get_rect(center = (400, 50))
    screen.blit(score_surface, score_rect)

pygame.init() #inicia o programa do pygame
screen =  pygame.display.set_mode((800,400)) #largura e altura do display, da tela
pygame.display.set_caption('Tela')

Clock = pygame.time.Clock()

test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

game_active = True

sky_surface = pygame.image.load('graphics/sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

#score_surface = test_font.render('Meu Jogo', False, (64,64,64))
#score_rect = score_surface.get_rect(center = (400, 50))

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomright = (600, 300))

player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80, 300))

player_gravity = 0

while True: # tem que colocar no while true que vai durar pra sempre, pra tela n sumir
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #fechando
            exit()
        
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_gravity = -20
            
            if event.type == pygame.MOUSEMOTION:
                if player_rect.collidepoint(event.pos): print ('collision')

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800
        


    if game_active == True:
        screen.blit(sky_surface, (0,0)) #isso ta colocando uma surface dentro da display surface
        screen.blit(ground_surface, (0, 300))

        #pygame.draw.rect(screen, '#c0e8ec', score_rect)
        #pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
        
        #screen.blit(score_surface, score_rect)
        display_score()

        snail_rect.x -= 4
        if snail_rect.right <= 0: snail_rect.left = 800
        screen.blit(snail_surface, snail_rect)

        # PLAYER #
        player_gravity += 1
        player_rect.y += player_gravity
        player_rect.left += 1
        if player_rect.bottom >= 300: player_rect.bottom = 300
        screen.blit(player_surface, player_rect)

        # COLLISION #

        if snail_rect.colliderect(player_rect):
            game_active = False

    else:
        screen.fill('Black')

    # desenhar todos os elementos
    #atualizar tudo
    pygame.display.update()

    Clock.tick(60) #limitando o jogo a 60 fps