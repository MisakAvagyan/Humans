import pygame
import random

pygame.init()

width = 1920
height = 1080

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

window = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
pygame.display.set_caption("Space shooter")

player_speed = 5
bullet_speed = 10
enemy_speed = 2
score = 0
bullet_cooldown = 30
player_img = pygame.image.load('player.png')
player_x = width // 2 - player_img.get_width() // 2
player_y = height - player_img.get_height()
bullets = []
bullet_timer = 0
enemies = []
enemy_img = pygame.image.load('enemy.png')


def draw_player(x, y):
    window.blit(player_img, (x, y))


def draw_enemy(x, y):
    window.blit(enemy_img, (x, y))


running = True
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    for bullet in bullets:
        bullet.y -= bullet_speed
        if bullet.y < 0:
            bullets.remove(bullet)
    if bullet_timer > 0:
        bullet_timer -= 0.5

    if keys[pygame.K_SPACE] and bullet_timer == 0:
        bullet = pygame.Rect(player_x + player_img.get_width() // 2 - 2, player_y, 4, 10)
        bullets.append(bullet)
        bullet_timer = bullet_cooldown
    if random.randint(1, 100) == 1:
        enemy_x = random.randint(0, width - enemy_img.get_width())
        enemy = pygame.Rect(enemy_x, 0, enemy_img.get_width(), enemy_img.get_height())
        enemies.append(enemy)

    for enemy in enemies:
        enemy.y += enemy_speed
        if enemy.y > height:
            enemies.remove(enemy)

    for bullet in bullets:
        for enemy in enemies:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 1

    for enemy in enemies:
        if enemy.colliderect(player_x, player_y, player_img.get_width(), player_img.get_height()):
            game_over = True

    if game_over:
        window.fill(BLACK)
        font = pygame.font.Font(None, 72)
        text = font.render("Game Over", True, WHITE)
        window.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height()))
        text = font.render("Score: " + str(score), True, WHITE)
        window.blit(text, (width // 2 - text.get_width() // 2, height // 2))
        try_again_text = font.render("Try Again", True, WHITE)
        try_again_button = pygame.Rect(width // 2 - try_again_text.get_width() // 2,
                                       height // 2 + 2 * try_again_text.get_height(),
                                       try_again_text.get_width(), try_again_text.get_height())
        pygame.draw.rect(window, BLACK, try_again_button)
        window.blit(try_again_text, (try_again_button.x, try_again_button.y))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and try_again_button.collidepoint(event.pos):
                    game_over = False
                    player_x = width // 2 - player_img.get_width() // 2
                    player_y = height - player_img.get_height()
                    bullets = []
                    enemies = []
                    score = 0

    else:
        window.fill(BLACK)
        draw_player(player_x, player_y)
        for bullet in bullets:
            pygame.draw.rect(window, WHITE, bullet)
        for enemy in enemies:
            draw_enemy(enemy.x, enemy.y)

        font = pygame.font.Font(None, 36)
        text = font.render("Score: " + str(score), True, WHITE)
        window.blit(text, (10, 10))

        pygame.display.update()

pygame.quit()
