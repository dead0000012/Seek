import pygame
import random
import math

class NPC:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def move_towards(npc, target, speed):
        if npc.x < target.x:
            npc.x += speed
        elif npc.x > target.x:
            npc.x -= speed

        if npc.y < target.y:
            npc.y += speed
        elif npc.y > target.y:
            npc.y -= speed


pygame.init()
screen_width, screen_height = 800, 600
pygame.display.set_caption("NPC Movement Example")
screen = pygame.display.set_mode((screen_width, screen_height))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
run = True
take = 0
clock = pygame.time.Clock()
Player_width, Player_height = 10, 10
Player = pygame.Rect(random.randint(0, screen_width - 90), random.randint(0, screen_height - 90), Player_width, Player_height)
Player_2 = pygame.Rect(random.randint(0, screen_width- 90), random.randint(1, screen_height - 90), Player_width, Player_height)
Player_3 = pygame.Rect(random.randint(0, screen_width - 90), random.randint(0, screen_height - 90), Player_width, Player_height)
Player_4 = pygame.Rect(random.randint(0, screen_width - 90), random.randint(0, screen_height - 90), Player_width, Player_height)
Player_5 = pygame.Rect(random.randint(0, screen_width - 90), random.randint(0, screen_height - 90), Player_width, Player_height)
Player_6 = pygame.Rect(random.randint(0, screen_width - 90), random.randint(0, screen_height - 90), Player_width, Player_height)
Player_7 = pygame.Rect(random.randint(0, screen_width - 90), random.randint(0, screen_height - 90), Player_width, Player_height)
Player_8 = pygame.Rect(random.randint(0, screen_width - 90), random.randint(0, screen_height - 90), Player_width, Player_height)
Player_9 = pygame.Rect(random.randint(0, screen_width - 90), random.randint(0, screen_height - 90), Player_width, Player_height)
Player_10 = pygame.Rect(random.randint(0, screen_width - 90), random.randint(0, screen_height - 90), Player_width, Player_height)
speed = 7
npc = pygame.Rect(screen_width // 2, screen_height // 2, 20 ,20)
npc_2 = pygame.Rect(screen_width // 2, screen_height // 2, 20, 20)
npc_3 = pygame.Rect(screen_width // 2, screen_height // 2, 20, 20)
npc_4 = pygame.Rect(screen_width // 2, screen_height // 2, 20, 20)
npc_5 = pygame.Rect(screen_width // 2, screen_height // 2, 20, 20)
npc_6 = pygame.Rect(screen_width // 2, screen_height // 2, 20, 20)
npc_7 = pygame.Rect(screen_width // 2, screen_height // 2, 20, 20)
npc_8 = pygame.Rect(screen_width // 2, screen_height // 2, 20, 20)
npc_9 = pygame.Rect(screen_width // 2, screen_height // 2, 20, 20)
npc_10 = pygame.Rect(screen_width // 2, screen_height // 2, 20, 20)
time = 0

while run:
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, Player)
    pygame.draw.rect(screen, BLACK, Player_2)
    pygame.draw.rect(screen, BLACK, Player_3)
    pygame.draw.rect(screen, BLACK, Player_4)
    pygame.draw.rect(screen, BLACK, Player_5)
    pygame.draw.rect(screen, BLACK, Player_6)
    pygame.draw.rect(screen, BLACK, Player_7)
    pygame.draw.rect(screen, BLACK, Player_8)
    pygame.draw.rect(screen, BLACK, Player_9)
    pygame.draw.rect(screen, BLACK, Player_10)

    pygame.draw.rect(screen, (255, 0, 0), npc)
    pygame.draw.rect(screen, (255, 0, 0), npc_2)
    pygame.draw.rect(screen, (255, 0, 0), npc_3)
    pygame.draw.rect(screen, (255, 0, 0), npc_4)
    pygame.draw.rect(screen, (255, 0, 0), npc_5)
    pygame.draw.rect(screen, (255, 0, 0), npc_6)
    pygame.draw.rect(screen, (255, 0, 0), npc_7)
    pygame.draw.rect(screen, (255, 0, 0), npc_8)
    pygame.draw.rect(screen, (255, 0, 0), npc_9)
    pygame.draw.rect(screen, (255, 0, 0), npc_10)


    NPC.move_towards( npc, Player, speed)
    NPC.move_towards(npc_2, Player_2, speed)
    NPC.move_towards(npc_3, Player_3, speed)
    NPC.move_towards(npc_4, Player_4, speed)
    NPC.move_towards(npc_5, Player_5, speed)
    NPC.move_towards(npc_6, Player_6, speed)
    NPC.move_towards(npc_7, Player_7, speed)
    NPC.move_towards(npc_8, Player_8, speed)
    NPC.move_towards(npc_9, Player_9, speed)
    NPC.move_towards(npc_10, Player_10, speed)
    
    

    if npc.colliderect(Player):
        random_x = random.randint(0, screen_width - 90)
        random_y = random.randint(0, screen_height - 90)
        Player = pygame.Rect(random_x, random_y, Player_width, Player_height)
        take += 1
        print(f"Collision count: {take}")
    elif npc_2.colliderect(Player_2):
        random.randint(0, screen_width - 90)
        random.randint(0, screen_height - 90)
        Player_2 = pygame.Rect(random.randint(0, screen_width - 200), random.randint(0, screen_height - 200), Player_width, Player_height)
        take += 1
        print(f"Collision count: {take}")
    elif npc_3.colliderect(Player_3):
        random.randint(0, screen_width - 90)
        random.randint(0, screen_height - 90)
        Player_3 = pygame.Rect(random.randint(0, screen_height - 200), random.randint(0, screen_width - 200), Player_width, Player_height)
        take += 1
        print(f"Collision count: {take}")
    elif npc_4.colliderect(Player_4):
        random.randint(0, screen_width - 90)
        random.randint(0, screen_height - 90)
        Player_4 = pygame.Rect(random.randint(0, screen_height - 200), random.randint(0, screen_width - 200), Player_width, Player_height)
        take += 1
        print(f"Collision count: {take}")
    elif npc_5.colliderect(Player_5):
        random.randint(0, screen_width - 90)
        random.randint(0, screen_height - 90)
        Player_5 = pygame.Rect(random.randint(0, screen_height - 200), random.randint(0, screen_width - 200), Player_width, Player_height)
        take += 1
        print(f"Collision count: {take}")
    elif npc_6.colliderect(Player_6):
        random.randint(0, screen_width - 90)
        random.randint(0, screen_height - 90)
        Player_6 = pygame.Rect(random.randint(0, screen_height - 200), random.randint(0, screen_width - 200), Player_width, Player_height)
        take += 1
        print(f"Collision count: {take}")
    elif npc_7.colliderect(Player_7):
        random.randint(0, screen_width - 90)
        random.randint(0, screen_height - 90)
        Player_7 = pygame.Rect(random.randint(0, screen_height - 200), random.randint(0, screen_width - 200), Player_width, Player_height)
        take += 1
        print(f"Collision count: {take}")
    elif npc_8.colliderect(Player_8):
        random.randint(0, screen_width - 90)
        random.randint(0, screen_height - 90)
        Player_8 = pygame.Rect(random.randint(0, screen_width - 200), random.randint(0, screen_height - 200), Player_width, Player_height)
        take += 1
        print(f"Collision count: {take}")
    elif npc_9.colliderect(Player_9):
        random.randint(0, screen_width - 90)
        random.randint(0, screen_height - 90)
        Player_9 = pygame.Rect(random.randint(0, screen_width - 200), random.randint(0, screen_height - 200), Player_width, Player_height)
        take += 1
        print(f"Collision count: {take}")
    elif npc_10.colliderect(Player_10):
        random.randint(0, screen_width - 90)
        random.randint(0, screen_height - 90)
        Player_10 = pygame.Rect(random.randint(0, screen_width - 200), random.randint(0, screen_height - 200), Player_width, Player_height)
        take += 1
        print(f"Collision count: {take}")

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            run = False

    npc.clamp_ip(screen.get_rect())
    npc_2.clamp_ip(screen.get_rect())
    npc_3.clamp_ip(screen.get_rect())
    npc_4.clamp_ip(screen.get_rect())
    npc_5.clamp_ip(screen.get_rect())
    npc_6.clamp_ip(screen.get_rect())
    npc_7.clamp_ip(screen.get_rect())
    npc_8.clamp_ip(screen.get_rect())
    npc_9.clamp_ip(screen.get_rect())
    npc_10.clamp_ip(screen.get_rect())


    clock.get_fps()
    pygame.display.set_caption(f"FPS: {int(clock.get_fps())}")

    pygame.display.update()
    clock.tick(60)
pygame.quit()


