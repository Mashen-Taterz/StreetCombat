import pygame
import random

pygame.init()


#Main Window
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 960

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Street Combat')

#Visuals
bg_image = pygame.img.get('')
#  Background
##BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))

#SoundFX
pygame.img.Sound()

#Character Class
class Character:
    def __init__(self, x, y, health = 100):
        self.x = x
        self.y = y 
        self.health = health


#Player Class & Controls
class Player(Character):
    def __init__(self, x, y, health = 100):
        super().__init__(x, y, health)
        self.name = "Player 1"
       
        
    
    
#AI Class & Controls
class Npc(Character):
    def __init__(self, x, y, health = 100):
        super().__init__(x, y, health)
        self.name = "NPC"
        

#Main Menu
def main_menu():
    run = True

    while run:

        for event in pygame.event.get():
            #quit game
            if event.type == pygame.QUIT:
                run = False

#Main game loop
def main():
    run = True
    FPS = 60
    player = Player(10, 950)
    npc = Npc (1270, 950)

    while run:

        for event in pygame.event.get():
            #quit game
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_vel > 0: # Left
            player.x -= player_vel
        if keys[pygame.K_d] and player.x + player_vel + player.get_width() < WIDTH:  # Right
            player.x += player_vel
        if keys[pygame.K_w] and player.y - player_vel > 0:  # Up
            player.y -= player_vel
        if keys[pygame.K_s] and player.y + player_vel + player.get_height() < HEIGHT:  # Down
            player.y += player_vel
        if keys[pygame.K_SPACE]:
            player.shoot()

pygame.quit()
            

