import random
import pygame

pygame.init()
window_width=800
window_height = 600

window = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("Snake Game")

white = (255, 255, 255)
black=(0,0,0)
red = (255,0,0)
game_over = False
Score = 0

x1=window_width / 2
y1= window_height/2

x1_change = 0
y1_change = 0

snake_body=[]
lenght_of_snake=1

foodx = round(random.randrange(0,window_width - 10) / 10)*10.0
foody = round(random.randrange(0,window_height-10)/10)*10.0

clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over= True
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change=-10
                y1_change=0
            elif event.key == pygame.K_RIGHT:
                x1_change=10
                y1_change= 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10
            
    x1 = x1+x1_change
    y1 = y1+y1_change

    if x1>=window_width or x1<0 or y1>=window_height or y1<0:
        game_over = True
    
    window.fill(black)
    snake_head = []
    snake_head.append(x1)
    snake_head.append(y1)

    snake_body.append(snake_head)
    if len(snake_body)> lenght_of_snake :
        del snake_body[0]

    for segment in snake_body[:-1]:
        if segment == snake_head :
            game_over = True

    font_style = pygame.font.SysFont(None, 50)
    Score_text = font_style.render("Score : "+str(Score),True,white)
    window.blit(Score_text,(10, 10))

    if x1 == foodx and y1 == foody :
        foodx = round(random.randrange(0, window_width-10)/10)*10.0
        foody = round(random.randrange(0, window_height-10)/10)*10.0
        lenght_of_snake += 1
        Score+=1

    pygame.draw.rect(window,red,[foodx,foody, 10,10])

    for segment in snake_body:
        pygame.draw.rect(window, white,[segment[0],segment[1], 10, 10])

    print(snake_body)
    pygame.display.update()
    clock.tick(20)
