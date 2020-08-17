import pygame
from pygame import Rect
from random import randint
from time import sleep

white = (255,255,255)
blue = (100,100,255)
red = (255,100,100)


class Entity():
    def __init__(self, x, y, width, height, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        
        
    def rects(self, obj):
        self.rect = obj

def text_display(text, color,x,y):
    font = pygame.font.SysFont(None, 24)
    font_render = font.render(text, True, color)
    window.blit(font_render,(x,y))



def main_loop(win_height, win_width):
    running = True

    player_1 = Entity(10, 0, 10, 50, blue)
    player_2 = Entity(win_width - 20, 0, 10, 50, red)
    ball = Entity(win_height/2, win_width/2, 10, 10, white)

    player_speed = 25
    ball_x_speed = 10
    ball_y_speed = 0

    score_counter = 0

    clock = pygame.time.Clock()
    
    

    while running:
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

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


        player_1_rect = Rect(player_1.x, player_1.y, player_1.width, player_1.height)
        player_2_rect = Rect(player_2.x, player_2.y, player_2.width, player_2.height)
        ball_rect = Rect(ball.x, ball.y, ball.width, ball.height)

        window.fill((0,0,0))

        player_1_obj = pygame.draw.rect(window, player_1.colour, player_1_rect)
        player_2_obj = pygame.draw.rect(window, player_2.colour, player_2_rect)
        ball_obj = pygame.draw.rect(window, ball.colour, ball_rect)

        # player_1.rects(player_1_obj)
        # player_2.rects(player_2_obj)
        # ball.rects(ball_obj)

        # BALL MOVEMENT

        

        ball.x += ball_x_speed
        ball.y += ball_y_speed

        pl_1_pos = (ball.x == player_1.x + 10 and (ball.y >= player_1.y and ball.y <= (player_1.y + player_1.height)))
        pl_2_pos = (ball.x == player_2.x - 10 and (ball.y >= player_2.y and ball.y <= (player_2.y + player_2.height)))
        
        if pl_1_pos or pl_2_pos:
            ball_x_speed = - ball_x_speed
            ball_y_speed = randint(1,10)
            if randint(1,3) == 1:
                ball_y_speed = - ball_y_speed

            score_counter += 1

        if ball.y > win_height - 10 or ball.y < 0 + 10:
            ball_y_speed = - ball_y_speed



        # VICTORY SCREEN
        if ball.x < player_1.x - 10:
            text_display('Player 2 Wins', red, 230,230)
            ball_x_speed = 0
            ball_y_speed = 0
            # text_display('Do you wanna play again ? y/n', white, 220, 325)

            # while True:
            #     if keys[pygame.K_y]:
            #         player_1 = Entity(10, 0, 10, 50, blue)
            #         player_2 = Entity(win_width - 20, 0, 10, 50, red)
            #         ball = Entity(win_height/2, win_width/2, 10, 10, white)

            #         player_speed = 25
            #         ball_x_speed = 10
            #         ball_y_speed = 0

            #         score_counter = 0
            #         break
            #     elif keys[pygame.K_n]:
            #         running = False
            #         break
            sleep(2)
        elif ball.x > player_2.x + 10:
            text_display('Player 1 Wins', blue, 230,230)
            ball_x_speed = 0
            ball_y_speed = 0
            # text_display('Do you wanna play again ? y/n', white, 220, 325)
        
            # if keys[pygame.K_y]:
            #     player_1 = Entity(10, 0, 10, 50, blue)
            #     player_2 = Entity(win_width - 20, 0, 10, 50, red)
            #     ball = Entity(win_height/2, win_width/2, 10, 10, white)

            #     player_speed = 25
            #     ball_x_speed = 10
            #     ball_y_speed = 0

            #     score_counter = 0
                
            #     break
            # elif keys[pygame.K_n]:
            #     running = False
            #     break
            sleep(2)

            
        text_display(f'Score: {score_counter}',white,win_width/2,10)
        pygame.display.update()

    pygame.quit()

pygame.init()

win_width = 500
win_height = 500

window = pygame.display.set_mode((win_width, win_height))

main_loop(win_height, win_width)