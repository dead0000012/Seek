import pygame
import random

# ————— Настройки —————
pygame.init()
screen_width, screen_height = 900, 600
screen = pygame.display.set_mode((screen_width, screen_height))


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PLAYER_SIZE = (10, 10)
NPC_SIZE = (20, 20)
SPEED = 10
COUNT = 1000  # сколько пар игрок+NPC

# ————— Вспомогательные функции —————
def spawn(rect_size):
    w, h = rect_size
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
    npc.clamp_ip(screen.get_rect())  # чтобы npc не вылезал из экрана

# ————— Создаём списки игроков и NPC —————
players = [spawn(PLAYER_SIZE) for _ in range(COUNT)]
npcs    = [spawn(NPC_SIZE)    for _ in range(COUNT)]

take = 0
clock = pygame.time.Clock()
run = True

# ————— Главный цикл —————
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
            run = False

    screen.fill(WHITE)

    # двигаем NPC к своим игрокам и отрисовываем
    for player, npc in zip(players, npcs):
        move_towards(npc, player, SPEED)
        pygame.draw.rect(screen, BLACK, player)
        pygame.draw.rect(screen, (255, 0, 0), npc)

        # проверка столкновения и респавн
        if npc.colliderect(player):
            players[players.index(player)] = spawn(PLAYER_SIZE)
            take += 1
            print(f"Collision count: {take}")
    fps = int(clock.get_fps())
    pygame.display.set_caption(f"NPC Movement Example — FPS: {fps}")
    pygame.display.flip()
    clock.tick(60)

pygame.quit()