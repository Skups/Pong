import pygame
from pygame import Rect
from random import randint


# COLORS
white = (255,255,255)
gray = (211,211,211)
blue = (100,100,255)
red = (255,100,100)


class Entity():
    def __init__(self, x, y, width, height, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour     


def text_display(text, color,x,y):
    font = pygame.font.SysFont(None, 24)
    font_render = font.render(text, True, color)
    window.blit(font_render,(x,y))

def main_loop(win_height, win_width):
    running = True

    player_1 = Entity(10, 225, 10, 50, blue)
    player_2 = Entity(win_width - 20, 225, 10, 50, red)
    ball = Entity(win_height//2, win_width//2, 10, 10, white)

    player_speed = 15
    if randint(1,3) == 1:
        ball_x_speed = -10
    else:
        ball_x_speed  = 10
    ball_y_speed = 0

    hit_sound = pygame.mixer.Sound('hit.wav')
    score_counter = 0

    while running:
        pygame.time.delay(100)
        keys = pygame.key.get_pressed()

        # QUIT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if keys[pygame.K_ESCAPE]:
            running = False

        # PLAYER ONE CONTROLS
        if keys[pygame.K_w] and player_1.y > 0:
            player_1.y -= player_speed
        elif keys[pygame.K_s] and player_1.y < win_height - player_1.height:
            player_1.y += player_speed
        
        # PLAYER TWO CONTROLS
        if keys[pygame.K_UP] and player_2.y > 0:
            player_2.y -= player_speed
        elif keys[pygame.K_DOWN] and player_2.y < win_height - player_2.height:
            player_2.y += player_speed

        # RETRY
        if keys[pygame.K_r]:
            player_1 = Entity(10, 225, 10, 50, blue)
            player_2 = Entity(win_width - 20, 225, 10, 50, red)
            ball = Entity(win_height//2, win_width//2, 10, 10, white)
            score_counter = 0
            if randint(1,3) == 1:
                ball_x_speed = -10
            else:
                ball_x_speed  = 10
            ball_y_speed = 0

        # DISPLAY THE ENTITIES
        player_1_rect = Rect(player_1.x, player_1.y, player_1.width, player_1.height)
        player_2_rect = Rect(player_2.x, player_2.y, player_2.width, player_2.height)
        ball_rect = Rect(ball.x, ball.y, ball.width, ball.height)

        window.fill((0,0,0))

        pygame.draw.rect(window, player_1.colour, player_1_rect)
        pygame.draw.rect(window, player_2.colour, player_2_rect)
        pygame.draw.rect(window, ball.colour, ball_rect)

        # BALL MOVEMENT
        ball.x += ball_x_speed
        ball.y += ball_y_speed

        pl_1_pos = (ball.x == player_1.x + 10 and (ball.y >= player_1.y - 5 and ball.y <= (player_1.y + player_1.height)))
        pl_2_pos = (ball.x == player_2.x - 10 and (ball.y >= player_2.y - 5 and ball.y <= (player_2.y + player_2.height)))
        
        if pl_1_pos or pl_2_pos:
            ball_x_speed = - ball_x_speed
            ball_y_speed = randint(1,10)

            if randint(1,3) == 1:
                ball_y_speed = - ball_y_speed

            score_counter += 1
            hit_sound.play()

        if ball.y > 489 or ball.y < 0 + 10:
            ball_y_speed = - ball_y_speed


        pl_1_win = ball.x > player_2.x + 10
        pl_2_win = ball.x < player_1.x - 10
        # VICTORY SCREEN
        if pl_1_win or pl_2_win :
            if pl_2_win:
                text_display('Player 2 Wins', red, 200,230)
            elif pl_1_win:
                text_display('Player 1 Wins', blue, 200,230)
            text_display('Press "R" to play again', gray, 160, 250)
            ball_x_speed = 0
            ball_y_speed = 0

        # SCORE COUNTER
        text_display(f'Score: {score_counter}',white,225,10)
        pygame.display.update()

    pygame.quit()


pygame.init()
pygame.mixer.init()

win_width = 500
win_height = 500
icon = pygame.image.load('icon.ico')

window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption('Pong by Skups')
pygame.display.set_icon(icon)

main_loop(win_height, win_width)