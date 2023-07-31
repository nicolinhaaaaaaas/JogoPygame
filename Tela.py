import pygame
from sys import exit
from random import randint, choice



class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
        player_walk_2 = pygame.image.load('graphics/player/player_walk_2.png').convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load('graphics/player/jump.png').convert_alpha()

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80,300))
        self.gravity = 0

        self.jump_sound = pygame.mixer.Sound('audio/jump.mp3')
        self.jump_sound.set_volume(0.3)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk): self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()



class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == 'fly':
            fly_1 = pygame.image.load('graphics/fly/fly1.png').convert_alpha()
            fly_2 = pygame.image.load('graphics/fly/fly2.png').convert_alpha()
            self.frames = [fly_1, fly_2]
            y_pos = 210
        else:
            snail_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
            snail_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
            self.frames = [snail_1, snail_2]
            y_pos = 300

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900, 1100), y_pos))

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames): self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy

    def destroy(self):
        if self.rect.x <= -100:
            self.kill


def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = test_font.render(f'Score: {current_time}', False, (64,64,64))
    score_rect = score_surface.get_rect(center = (400, 50))
    screen.blit(score_surface, score_rect)
    return current_time

def obstacle_movement(obstacle_list):

    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 300:
                screen.blit(snail_surface, obstacle_rect)
            else:
                screen.blit(fly_surface, obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100] #isso garante que os obstaculos q saem da tela, somem
            
        return obstacle_list
    else: return []

def collisions(player,obstacles):
	if obstacles:
		for obstacle_rect in obstacles:
			if player.colliderect(obstacle_rect): return False
	return True

def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group , False):
        obstacle_group.empty( )
        return False
    else: return True

def player_animation():
    # animação de andar do personagem

    global player_surface, player_index

    if player_rect.bottom <300:
        player_surface = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk): player_index = 0
        player_surface = player_walk[int(player_index)]



pygame.init() #inicia o programa do pygame
screen =  pygame.display.set_mode((800,400)) #largura e altura do display, da tela
pygame.display.set_caption('Tela')

Clock = pygame.time.Clock()

test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

game_active = False

start_time = 0

score = 0

# MUSICA #
bg_music = pygame.mixer.Sound('audio/music.wav')
bg_music.play(loops = -1) # isso faz dar loop pra sempre
bg_music.set_volume(0.3)

player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()

sky_surface = pygame.image.load('graphics/sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

#score_surface = test_font.render('Meu Jogo', False, (64,64,64))
#score_rect = score_surface.get_rect(center = (400, 50))

# TUDO ISSO AQUI ABAIXO PODIA SER DELETADO, PQ TA SENDO FEITO A MSM COISA NAS CLASSES

#SNAIL
snail_frame_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_frame_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
snail_frames = [snail_frame_1, snail_frame_2]
snail_frame_index = 0
snail_surface = snail_frames[snail_frame_index]

#FLY
fly_frame_1 = pygame.image.load('graphics/fly/fly1.png').convert_alpha()
fly_frame_2 = pygame.image.load('graphics/fly/fly2.png').convert_alpha()
fly_frames = [fly_frame_1, fly_frame_2]
fly_frame_index = 0
fly_surface = fly_frames[fly_frame_index]

obstacle_rect_list = []

#PLAYER
player_walk_1 = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load('graphics/player/player_walk_2.png').convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_jump = pygame.image.load('graphics/player/jump.png').convert_alpha()

player_surface = player_walk[player_index]
player_rect = player_surface.get_rect(midbottom = (80, 300))
player_gravity = 0

# DAQUI PRA CIMA É INUTIL

#INTRO SCREEN
player_stand = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400, 200))

title_surface = test_font.render('Joguinho', False, (111, 196, 169))
title_rect = title_surface.get_rect(center = (400, 80))

game_message = test_font.render('Aperte ESPACO para comecar', False, (111, 196, 169))
game_message_rect = game_message.get_rect(center = (400, 350))

# TIMER
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT +3
pygame.time.set_timer(fly_animation_timer, 200)


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
                start_time = int(pygame.time.get_ticks() / 1000)

        if game_active:
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(['fly', 'snail', 'snail', 'snail']))) # isso faz com que o programa escolha aleatoriamente oq spawnar
                #if randint(0,2):
                #    obstacle_rect_list.append(snail_surface.get_rect(bottomright = (randint(900, 1100), 300)))
                #else: 
                #    obstacle_rect_list.append(fly_surface.get_rect(bottomright = (randint(900, 1100), 200)))

            if event.type == snail_animation_timer:
                if snail_frame_index == 0: snail_frame_index = 1
                else: snail_frame_index = 0
                snail_surface = snail_frames[snail_frame_index]

            if event.type == fly_animation_timer:
                if fly_frame_index == 0: fly_frame_index = 1
                else: fly_frame_index = 0
                fly_surface = fly_frames[fly_frame_index]


    if game_active == True:
        screen.blit(sky_surface, (0,0)) #isso ta colocando uma surface dentro da display surface
        screen.blit(ground_surface, (0, 300))

        #pygame.draw.rect(screen, '#c0e8ec', score_rect)
        #pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
        
        #screen.blit(score_surface, score_rect)
        score = display_score()

        #snail_rect.x -= 4
        #if snail_rect.right <= 0: snail_rect.left = 800
        #screen.blit(snail_surface, snail_rect)

        # PLAYER #
        #player_gravity += 1
        #player_rect.y += player_gravity
        #player_rect.left += 1
        #if player_rect.bottom >= 300: player_rect.bottom = 300
        #player_animation()
        #screen.blit(player_surface, player_rect)
        player.draw(screen)
        player.update()

        obstacle_group.draw(screen)
        obstacle_group.update()

        #OBSTACLE MOVEMENT#
        #obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # COLLISION #
        game_active = collision_sprite()
        #game_active = collisions(player_rect, obstacle_rect_list)

    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (80, 300)
        player_gravity = 0

        score_message = test_font.render(f'Sua pontuacao: {score}', False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center = (400, 350))

        screen.blit(title_surface, title_rect)

        #mostrando a pontução
        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)

    # desenhar todos os elementos
    #atualizar tudo
    pygame.display.update()

    Clock.tick(60) #limitando o jogo a 60 fps