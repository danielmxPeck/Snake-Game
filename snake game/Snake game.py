import time
from numpy import blackman
import pygame
import random

pygame.init() #initialize
pygame.display.set_caption("SNAKE GAME")

game_over =False
display_w = 800
display_h = 600
display = pygame.display.set_mode((display_w,display_h))



black = (0, 0, 0)  
white = (255,255,255)
blue = (0,0,255)
red = (255,0,0)  
green = (0, 255, 0)
blue = (50, 153, 213)

snake_block = 10
snake_speed = 15

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None,30,bold=True)
score_font = pygame.font.SysFont(None, 20, bold=True)

def play_score(score,color):
    value = score_font.render(str(score),True,black)
    display.blit(value,(0,0))

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display,black,[x[0],x[1],snake_block,snake_block])

def message(msg,color):
    message = font_style.render(msg, True, color)
    display.blit(message,(display_w/4,display_h/2)) # Display in the middle

def gameLoop():
    game_over=False
    game_close = False

    x1 = display_w/2
    y1 = display_h /2 
    
    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1
    score = 0

    foodx = round(random.randrange(0, display_w - snake_block) / 10.0) *10.0
    foody = round(random.randrange(0, display_h - snake_block )/ 10.0 )*10.

    while not game_over:

        while game_close == True:
            display.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.key == pygame.K_q:
                    game_over = True
                    game_close = False
                elif event.key == pygame.K_c: ## chaganed to else if 
                    gameLoop()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0  
            
        if x1 >= display_w or x1 < 0 or y1 >= display_h or y1 < 0:
            game_close = True
    


        for x in snake_list[:-1]:
            if x == snake_Head:
                game_close = True
                
        
        our_snake(snake_block,snake_list)

        play_score(score,black)     
        pygame.display.update()
        
        if x1==foodx and y1 == foody:
            print('Yummy')
            foodx = round(random.randrange(0, display_w - snake_block) / 10.0) *10.0
            foody = round(random.randrange(0, display_h - snake_block )/ 10.0 )*10.0
            length_of_snake+=1
            score+=1
        

        x1 += x1_change
        y1 += y1_change
        display.fill(blue)
        pygame.draw.rect(display,green,[foodx,foody, snake_block,snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_list.append(snake_Head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]
            
        play_score(score,black)      
        
        clock.tick(snake_speed)
        # print(snake_Head)
        print(snake_list)
        # message("YOU LOST", red)
        # pygame.display.update()
        # time.sleep(2)
    
    pygame.quit()
    quit()

gameLoop()

