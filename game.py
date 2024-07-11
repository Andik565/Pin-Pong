import pygame
import random

pygame.init()
pygame.mixer.init()

sound = pygame.mixer.Sound("Balloon.wav")
sound2 = pygame.mixer.Sound("Ring.waw")

screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("pin-pong")
font = pygame.font.Font(None, 36)

color1 = (173, 190, 255)
color2 = (202, 234, 129)
color3 = (253, 252, 0)
color4 = (255, 255, 255)
color5 = (0, 0, 0)
color6 = (50, 50, 50)


platform_w, platform_h = 160, 20
player_platform = pygame.Rect(screen_width // 2 - platform_w // 2,
                              screen_height - platform_h - 10,
                              platform_w, platform_h)

ball = pygame.Rect(screen_width // 2, screen_height // 2, 30, 30)

def menu():
    while True:
        for event2 in pygame.event.get():
            if event2.type == pygame.QUIT:
                pygame.quit()
                quit()


        slow_btn = pygame.Rect(screen_width // 2 - 100, 140, 200, 50)
        normal_btn = pygame.Rect(screen_width // 2 - 100, 200, 200, 50)
        fast_btn = pygame.Rect(screen_width // 2 - 100, 260, 200, 50)
        exit_btn = pygame.Rect(screen_width // 2 - 100, 450, 200, 50)
        fast_text = font.render("Сложно", True, color4)
        normal_text = font.render("Нормально", True, color4)
        slow_text = font.render("Просто", True, color4)
        exit_text = font.render("Выход", True, color4)

        screen.fill(color4)

        mouse_pos = pygame.mouse.get_pos()



        pygame.draw.rect(screen, color5, slow_btn)
        pygame.draw.rect(screen, color5, normal_btn)
        pygame.draw.rect(screen, color5, fast_btn)
        pygame.draw.rect(screen, color5, exit_btn)

        if exit_btn.collidepoint(mouse_pos):
            pygame.draw.rect(screen, color6, exit_btn)
        else:
            pygame.draw.rect(screen, color5, exit_btn)

        if slow_btn.collidepoint(mouse_pos):
            pygame.draw.rect(screen, color6, slow_btn)
        else:
            pygame.draw.rect(screen, color5, slow_btn)

        if normal_btn.collidepoint(mouse_pos):
            pygame.draw.rect(screen, color6, normal_btn)
        else:
            pygame.draw.rect(screen, color5, normal_btn)

        if fast_btn.collidepoint(mouse_pos):
            pygame.draw.rect(screen, color6, fast_btn)
        else:
            pygame.draw.rect(screen, color5, fast_btn)

        screen.blit(slow_text, (slow_btn.centerx - slow_text.get_width() // 2,
                                slow_btn.centery - slow_text.get_height() // 2))
        screen.blit(normal_text, (normal_btn.centerx - normal_text.get_width() // 2,
                                normal_btn.centery - normal_text.get_height() // 2))
        screen.blit(fast_text, (fast_btn.centerx - fast_text.get_width() // 2,
                                fast_btn.centery - fast_text.get_height() // 2))
        screen.blit(exit_text, (exit_btn.centerx - exit_text.get_width() // 2,
                                exit_btn.centery - exit_text.get_height() // 2))


        click = pygame.mouse.get_pressed()

        if exit_btn.collidepoint(mouse_pos) and click[0]:
            pygame.quit()
            quit()

        if slow_btn.collidepoint(mouse_pos) and click[0]:
            return 2

        if normal_btn.collidepoint(mouse_pos) and click[0]:
            return 4

        if fast_btn.collidepoint(mouse_pos) and click[0]:
            return 8


        pygame.display.update()

speed = menu()

ball_speed = [random.choice((-speed, speed)), -speed]

ball_is = False
running = True
clock = pygame.time.Clock()
score = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        if player_platform.left > 0:
            player_platform.x -= 6
    elif key[pygame.K_d]:
        if player_platform.right < screen_width:
            player_platform.x += 6


    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    if ball.top <= 0:
        ball_speed[1] = -ball_speed[1]
        sound2.play()
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed[0] = -ball_speed[0]
        sound2.play()

    if ball.colliderect(player_platform):
        if not ball_is:
            ball_speed[1] = -ball_speed[1]
            ball_is = True
            sound.play()
            score += 1
        else:
            ball_is = False




    screen.fill(color1)

    pygame.draw.rect(screen, color2, player_platform)
    pygame.draw.ellipse(screen, color3, ball)
    score_text = f"Score: {score}"
    s = font.render(score_text, True, color3)
    screen.blit(s, (20, 20))
    pygame.display.update()
    clock.tick(75)

pygame.quit()
