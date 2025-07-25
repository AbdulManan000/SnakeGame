

import pygame
import random



pygame.init()
pygame.display.set_caption("Snake")
icon=pygame.image.load("snake.png")
pygame.display.set_icon(icon)
screen_width=1600
screen_height=900
screen=pygame.display.set_mode((screen_width,screen_height))

player_pos = pygame.Vector2((screen.get_width() / 2)+5, (screen.get_height() / 2)+13)
player = pygame.Rect(player_pos[0],player_pos[1],25,25)
vel=10
clock=pygame.time.Clock()

cordfruit1=random.choice([i+1 for i in range (30,screen_width - 40)])
cordfruit2=random.choice([i+1 for i in range (30,screen_height - 40)])


xlocation=0
ylocation=0

lenofsnake=0
snakelist=[]
score=0
font = pygame.font.SysFont(None,36,bold=True,italic=True,)

wblockkey=False
sblockkey=False
ablockkey=False
dblockkey=False

image = pygame.image.load("88072056.jpg")

def backgroundimage(image):
    size=pygame.transform.scale(image,(screen_width-1,screen_height-1)).convert_alpha()
    screen.blit(size,(1,1))

ratimage=pygame.image.load("rat.png")
ratimagescaled=pygame.transform.scale(ratimage,(50,55))

run = True
def gameending(run):
    screenrun=True
    while screenrun == True and run == True:
        screen.fill("red")
        Text1 = font.render(f"You lose,Try again", True, "white")
        screen.blit(Text1, (screen_width / 2 - (Text1.get_width() / 2), screen_height / 2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
    pygame.quit()

backgroundgreen=(32,33,37)



try:
 while run:


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False





    #movement

    button=pygame.key.get_pressed()


    if button[pygame.K_w]==True and wblockkey==False:

        xlocation = 0
        ylocation = (-vel)
        player_pos.y = player_pos.y + ylocation

        if lenofsnake>0:
         wblockkey=False
         sblockkey=True
         ablockkey=False
         dblockkey=False



    elif button[pygame.K_s]==True and sblockkey==False:
         xlocation = 0
         ylocation = vel
         player_pos.y = player_pos.y + ylocation

         if lenofsnake > 0:
          wblockkey=True
          sblockkey=False
          ablockkey=False
          dblockkey=False

    elif button[pygame.K_d]==True and dblockkey==False:
        xlocation = vel
        ylocation = 0
        player_pos.x = player_pos.x + xlocation

        if lenofsnake>0:
         wblockkey=False
         sblockkey=False
         ablockkey= True
         dblockkey= False



    elif button[pygame.K_a]==True and ablockkey==False:
         xlocation=(-vel)
         ylocation=0
         player_pos.x = player_pos.x + xlocation

         if lenofsnake>0:
          wblockkey= False
          sblockkey= False
          ablockkey= False
          dblockkey= True

    else:
        player_pos.x=player_pos.x + xlocation
        player_pos.y = player_pos.y + ylocation
     #movement ends



    # screen.fill(backgroundgreen)
    screen.fill(backgroundgreen)
    backgroundimage(image)



    # Snake
    if len(snakelist)>lenofsnake:
        del snakelist[0]
    head=[]
    head.append(player_pos.x)
    head.append(player_pos.y)
    snakelist.append(head)
    for x,y in snakelist:
     player = pygame.Rect(x,y,25,25)
     pygame.draw.rect(screen,(172,172,172),player)
    snakelist2=snakelist[1:-1]
    for i in snakelist2:
        collider=i
        if player_pos.x==collider[0] and  player_pos.y==collider[1]:
            gameending(run)
     #snake ends



    #border
    border1=pygame.Rect(-1,-1,screen_width,1)
    border2 = pygame.Rect(-1, -1,1,screen_height)
    border3 = pygame.Rect(-1, screen_height, screen_width,1)
    border4 = pygame.Rect(screen_width,-1,1,screen_height)
    borderlist=[border1,border2,border3,border4]
    pygame.draw.rect(screen, backgroundgreen, border1)
    pygame.draw.rect(screen, backgroundgreen, border2)
    pygame.draw.rect(screen, backgroundgreen, border3)
    pygame.draw.rect(screen, backgroundgreen, border4)
    for border in borderlist:
     if player.colliderect(border):
        gameending(run)
     #borderends



    #fruit
    fruit = pygame.Rect(cordfruit1, cordfruit2, 30, 30)
    screen.blit(ratimagescaled, fruit)
    if player.colliderect(fruit):
        score=score+1
        cordfruit1 = random.choice([i + 1 for i in range(40,(screen_width - 40))])
        cordfruit2 = random.choice([i + 1 for i in range(40,(screen_height - 40))])
        lenofsnake=lenofsnake+3
    #fruitends



   #score
    Text = font.render(f"Score:{score}", True, "white")
    screen.blit(Text, (1,1))
   #score ends




    clock.tick(60)

    pygame.display.update()

 pygame.quit()

except:
 pygame.quit()

