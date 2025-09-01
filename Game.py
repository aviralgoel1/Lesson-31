import math
import random
import pygame


screen_width = 800
screen_height = 500
player_start_x =  370
player_start_y=380
enemy_start_y_min=50
enemy_start_y_max=150
enemy_speed_x=4
enemy_speed_y=40
bullet_seped_y=10
collision_distance=27


pygame.init()
screen=pygame.display.set_mode((screen_width,screen_height))
background=pygame.image.load('background.png')
pygame.display.set_caption("Space invader")
icon=pygame.image.lead('ufo.png')
pygame.display.set_icon(icon)

playerImg=pygame.image.load('player.png')
player_x= player_start_x
player_y=player_start_y

playerx_change=0

enemyImg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enemies = 6

for _i in range (num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0,screen_width-64))
    enemyY.append(random.randint(enemy_start_y_min,enemy_start_y_max))
    enemyX_change.append(enemy_speed_x)
    enemyY_change.append(enemy_speed_y)

bulletImg=pygame.image.load('bullet.png')
bulletX=0
bulletY=player_start_y
bullet_state="ready"

score_value=0
font=pygame.font.Font('freesansbolt.ttf',32)
textX=10
textY=10

over_font=pygame.font.Font('freesansbold.ttf',64)

def show_score(x,y):
    score = font.render("Score: "+str(score_value), True, (255,255,255))
    screen.blit(score,(x,y))
def game_over_text():
    over_text=over_font.render("GAME OVER",True,(255,255,255))
    screen.blit(over_text, (200,250))
def player (x,y):
    screen.blit(playerImg,(x,y))
def Enemy (x,y,i):
    screen.blit(enemyImg[i],(x,y))
def fire_bullet(x,y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x+16,y+10))
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance=math.sqrt((enemyX-bulletX)**2+(enemyY-bulletY)**2)
    return distance < collision_distance


running = True
while running:
    screen.fill((0,0,0))
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            