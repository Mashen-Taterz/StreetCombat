import pygame
import random

pygame.init()


#Main Window
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 960

#Game states
STATE_MENU = 0
STATE_CHARACTER_SELECT = 1
STATE_STAGE_SELECT = 2
STATE_GAME = 3

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Street Combat')

#Set up clock to track fps
clock = pygame.time.Clock()

#Visuals

#  Background
#bg_image = pygame.img.load('images/bg1.png')
#def draw_bg():
  #  scaled_bg = pygame.transform.scale(bg_image,(SCREEN_WIDTH, SCREEN_HEIGHT))
  #   screen.blit(scaled_bg, (0, 0))

#SoundFX
#pygame.img.load('')

#Character Class
class Character:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damgage = damage
        self.rect = pygame.Rect(0, 0, 100, 180) #initialize Character rectangle position and size.

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)

    def move(self, dx, dy, obstacles):
        old_rect = self.rect.copy() #Save position of old rectangle
        self.rect.move_ip(dx, dy) #Move characters rectangle
        for obstacle in obstacles:
            if self.rect.colliderect(obstacle):
                self.rect = old_rect #If character collides with obstacle revert to old position.

#Player Class & Controls
class Player(Character):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.name = "Player 1"
    
    def move_input(self, keys, obstacles):
        dx = 0
        dy = 0
        #Movements
        if keys[pygame.K_LEFT]:
            dx -= 5
        if keys[pygame.K_RIGHT]:
            dx += 5
        if keys[pygame.K_UP]:
            dy -= 5
        if keys[pygame.K_DOWN]:
            dy += 5
        self.move(dx, dy, obstacles)
        #Abilities
        if keys[pygame.K_q]: #Block
            pass
        if keys[pygame.K_w]: #Punch
            pass
        if keys[pygame.K_e]: #Kick
            pass
        if keys[pygame.K_SPACE]: #Special
            pass
        
    
    
#AI Class & Controls
class Npc(Character):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.name = "NPC"
        
    #npc_moves = [punch, kick, jump, foward, back]:
    #npc_action = random.choice(npc_moves)
        #return npc_action

#Main Menu

#Character Select

#Stage Select


#Initialize Player and NPC    
player = Player("Player", 100, 5)
player.rect.center = (200, 300)
npc = Npc ("NPC", 100, 5)
npc.rect.center = (400, 300)

#Initialize game state
game_state = STATE_MENU

#Main game loop
while True:

    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_state == STATE_MENU:
                game_state = STATE_CHARACTER_SELECT


    #Handle input
    keys = pygame.key.get_pressed()
    if game_state == STATE_GAME:
        player.handle_input(keys, [npc.rect])
    
    #Update game state
    if game_state == STATE_GAME:
        #update state for game loop
        pass
     

    #Draw on window
    screen.fill((100, 100, 100)) 
    if game_state == STATE_MENU:
        #Draw main menu
        pass
    elif game_state == STATE_GAME:
        player.draw(screen)
        npc.draw(screen)
    

    pygame.display.flip()

    #Limit 60 fps
    clock.tick(60)

        
            

