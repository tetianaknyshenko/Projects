import random
import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT
import os

pygame.init()

FPS = pygame.time.Clock()
height = 800
width = 1200
font = pygame.font.SysFont('Verdana', 40)

main_display = pygame.display.set_mode((width, height))

# Завантаження фону
bg_path = os.path.join(os.getcwd(), "BanderoGusak", "background.png")
bg = pygame.transform.scale(pygame.image.load(bg_path), (width,height))
bg_X1=0
bg_X2=bg.get_width()
bg_move=3

pygame.display.set_caption("Pygame Гусак")

Color_White = (255, 255, 255)
Color_Black = (0, 0, 0)
Color_Blue = (0, 0, 250)
Color_Red = (255, 0, 0)

Player_Size = (25, 25)
#player = pygame.Surface(Player_Size)
bg_player_path = os.path.join(os.getcwd(), "BanderoGusak", "player.png")
IMAGE_PATH="BanderoGusak/goose_animation"
Player_Images=os.listdir(IMAGE_PATH)

player = pygame.image.load(bg_player_path).convert_alpha()
#player.fill(Color_Black)
player_rect = player.get_rect(center=(100, height // 2))
player_move_down = [0, 4]
player_move_up = [0, -4]
player_move_right = [4, 0]
player_move_left = [-4, 0]

bg_enemy_path = os.path.join(os.getcwd(), "BanderoGusak", "enemy.png")
bg_bonus_path = os.path.join(os.getcwd(), "BanderoGusak", "bonus.png")

def create_enemy():
    enemy_size = (30, 30)
    #enemy = pygame.Surface(enemy_size)
    enemy = pygame.image.load(bg_enemy_path).convert_alpha()
    #enemy.fill(Color_Blue)
    enemy_rect = pygame.Rect(width, random.randint(100, height-100), *enemy_size)
    enemy_move = [random.randint(-8, -4), 0]
    return [enemy, enemy_rect, enemy_move]

def create_bonus():
    bonus_size = (20, 20)
    #bonus = pygame.Surface(bonus_size)
    bonus = pygame.image.load(bg_bonus_path).convert_alpha()
    #bonus.fill(Color_Red)
    bonus_rect = pygame.Rect(random.randint(150, width-150), -bonus_size[1], *bonus_size)
    bonus_move = [0, random.randint(4, 8)]
    return [bonus, bonus_rect, bonus_move]

CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 2500)

CREATE_BONUS = pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_BONUS, 3000)

Change_Image=pygame.USEREVENT+3
pygame.time.set_timer(Change_Image,250)
enemies = []
bonuses = []
score = 0
image_index=0
playing = True

while playing:
    FPS.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False
            #pygame.quit()
            break  # Завершення циклу після завершення роботи Pygame

        if event.type == CREATE_ENEMY:
            enemies.append(create_enemy())

        if event.type == CREATE_BONUS:
            bonuses.append(create_bonus())
        
        if event.type == Change_Image:
            player=pygame.image.load(os.path.join(IMAGE_PATH, Player_Images[image_index]))
            image_index+=1
            if image_index>=len(Player_Images):
                image_index=0


    
    bg_X1-= bg_move
    bg_X2-= bg_move

    if bg_X1<-bg.get_width():
        bg_X1=bg.get_width()
    
    if bg_X2<-bg.get_width():
        bg_X2=bg.get_width()
    main_display.blit(bg,(bg_X1, 0))
    main_display.blit(bg, (bg_X2, 0))


    keys = pygame.key.get_pressed()

    if keys[K_DOWN] and player_rect.bottom < height:
        player_rect = player_rect.move(player_move_down)
    if keys[K_UP] and player_rect.top > 0:
        player_rect = player_rect.move(player_move_up)
    if keys[K_RIGHT] and player_rect.right < width:
        player_rect = player_rect.move(player_move_right)
    if keys[K_LEFT] and player_rect.left > 0:
        player_rect = player_rect.move(player_move_left)

    for enemy in enemies:
        enemy[1] = enemy[1].move(enemy[2])
        main_display.blit(enemy[0], enemy[1])    

    for bonus in bonuses:
        bonus[1] = bonus[1].move(bonus[2])
        main_display.blit(bonus[0], bonus[1])

    main_display.blit(font.render(str(score), True, Color_Black), (width - 50, 20))
    main_display.blit(player, player_rect)
    pygame.display.flip()

    for enemy in enemies:
        if enemy[1].left < 0:
            enemies.pop(enemies.index(enemy))
        
        if player_rect.colliderect(enemy[1]):
            print('Boom')
            playing = False
            pygame.quit()
            break

    for bonus in bonuses:
        if bonus[1].top > height:
            bonuses.pop(bonuses.index(bonus))
        
        if player_rect.colliderect(bonus[1]):
            score += 10
            bonuses.pop(bonuses.index(bonus))

# Повне завершення програми
pygame.quit()
