import pygame
import random
import math

pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("NPC Movement Example")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PLAYER_SIZE = (10, 10)
NPC_SIZE    = (20, 20)
SPEED       = 7
COUNT       = 10  

def spawn(size):
    w, h = size
    x = random.randint(0, screen_width  - w)
    y = random.randint(0, screen_height - h)
    return pygame.Rect(x, y, w, h)

def move_towards(npc, target, speed):
    if npc.x < target.x:
        npc.x += speed
    elif npc.x > target.x:
        npc.x -= speed
    if npc.y < target.y:
        npc.y += speed
    elif npc.y > target.y:
        npc.y -= speed
    npc.clamp_ip(screen.get_rect())

npcs    = [spawn(NPC_SIZE)    for _ in range(COUNT)]
players = [spawn(PLAYER_SIZE) for _ in range(COUNT)]

take = 0
clock = pygame.time.Clock()
run = True

def dist2(a, b):
    dx = a.x - b.x
    dy = a.y - b.y
    return dx*dx + dy*dy

while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
            run = False

    screen.fill(WHITE)

    for npc in npcs:
        nearest = min(players, key=lambda p: dist2(npc, p))

        move_towards(npc, nearest, SPEED)

        pygame.draw.rect(screen, (255, 0, 0), npc)
    for player in players:
        pygame.draw.rect(screen, BLACK, player)

    for i, player in enumerate(players):
        for npc in npcs:
            if npc.colliderect(player):
                players[i] = spawn(PLAYER_SIZE)
                take += 1
                print(f"Collision count: {take}")
                break 

    pygame.display.set_caption(f"NPC Movement Example — FPS: {int(clock.get_fps())}")
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
