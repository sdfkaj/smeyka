import pygame
import random

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pong")


    paddle_1 = pygame.Rect(30, SCREEN_HEIGHT // 2 - 50, 7, 100)
    paddle_2 = pygame.Rect(SCREEN_WIDTH - 50, SCREEN_HEIGHT // 2 - 50, 7, 100)
    ball = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 25, 25)

    paddle_1_move = 0
    paddle_2_move = 0

    ball_speed_x = random.choice([-0.2, 0.2])
    ball_speed_y = random.choice([-0.2, 0.2])

    clock = pygame.time.Clock()
    started = False

    font = pygame.font.SysFont('Consolas', 30)

    while True:
        delta_time = clock.tick(60)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    paddle_1_move = -0.5
                if event.key == pygame.K_s:
                    paddle_1_move = 0.5
                if event.key == pygame.K_UP:
                    paddle_2_move = -0.5
                if event.key == pygame.K_DOWN:
                    paddle_2_move = 0.5
                if event.key == pygame.K_SPACE:
                    started = True

            if event.type == pygame.KEYUP:
                if event.key in (pygame.K_w, pygame.K_s):
                    paddle_1_move = 0
                if event.key in (pygame.K_UP, pygame.K_DOWN):
                    paddle_2_move = 0
        paddle_1.top += paddle_1_move * delta_time
        paddle_2.top += paddle_2_move * delta_time
        paddle_1.clamp_ip(screen.get_rect())
        paddle_2.clamp_ip(screen.get_rect())

        if started:
            ball.left += ball_speed_x * delta_time
            ball.top += ball_speed_y * delta_time

            if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
                ball_speed_y *= -1
            if ball.colliderect(paddle_1) and ball_speed_x < 0:
                ball_speed_x *= -1
                ball.left = paddle_1.right
            if ball.colliderect(paddle_2) and ball_speed_x > 0:
                ball_speed_x *= -1
                ball.right = paddle_2.left

            if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
                started = False
                ball.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
                ball_speed_x = random.choice([-0.4, 0.4])
                ball_speed_y = random.choice([-0.4, 0.4])


        screen.fill(COLOR_BLACK)
        pygame.draw.rect(screen, COLOR_WHITE, paddle_1)
        pygame.draw.rect(screen, COLOR_WHITE, paddle_2)
        pygame.draw.ellipse(screen, COLOR_WHITE, ball)

        if not started:
            text = font.render('Press SPACE to Start', True, COLOR_WHITE)
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            screen.blit(text, text_rect)

        pygame.display.flip()


if __name__ == "__main__":
    main()
