import pygame,sys,random

fly_up = False
fly_down = False
ground = True

pygame.init()
clock = pygame.time.Clock()


screen_width = 700
screen_height = 500
BG_x = 0
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jump")
BGImg = pygame.image.load("BG.png")
screen_speed = 7

top_pipe_img = pygame.image.load("down.png")
bottom_pipe_img = pygame.image.load("up.png")
pipe_x =  screen_width/2
pipe_y =  random.randrange(screen_height/2 ,screen_height/2 + 100 )
screen.blit(top_pipe_img, (screen_width/2, screen_height/2 - 20))


bg_color = pygame.Color("grey12")
light_grey = (200,200,200)

birdimg = pygame.image.load("bird.png")

bird = pygame.Rect(screen_width/2, screen_height, 30,30)
bird_fly_speed_y = 3
bird_fall_speed_y = 3
bird_jump_height = -75
current_bird_y = 0
bird_y = screen_height-50
bird_x = screen_width/2 - 200


screen.blit(birdimg, (bird_x, bird_y))

base = pygame.Rect(0, screen_height-20, screen_width, 20)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                current_bird_y = bird_y
                print(current_bird_y)
                fly_up = True



        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                pass


    rel_x = BG_x % BGImg.get_rect().width
    screen.blit(BGImg, (rel_x - BGImg.get_rect().width, 0))
    if rel_x < screen_width:
        screen.blit(BGImg, (rel_x, 0))
    BG_x -= screen_speed

    """if BG_x <= 1600:
        screen.blit(BGImg,(BG_x, 0))
        BG_x -= 1
    elif BG_x >= 1600:
        BG_x = 0
        screen.blit(BGImg,(BG_x, 0))"""


    pygame.draw.rect(screen, light_grey, base)


    if ground == True:
        screen.blit(birdimg, (bird_x, bird_y))
        #bird.bottom = base.top
        



    if fly_up:
        fly_down = False
        ground = False
        if bird_y > bird_jump_height+current_bird_y:
            bird_y -= bird_fly_speed_y
            screen.blit(pygame.transform.rotate(birdimg, 30), (bird_x, bird_y))

        if bird_y <= bird_jump_height+current_bird_y:
            bird_y += bird_fall_speed_y
            fly_up = False
            fly_down = True


    if fly_down:
        if bird_y < base.top:
            bird_y += bird_fall_speed_y

            screen.blit(pygame.transform.rotate(birdimg, -80), (bird_x, bird_y))

        if bird_y >= base.top:
            bird_y = base.top - 20

            screen.blit(birdimg, (bird_x, bird_y))
            fly_down = False
            ground = True
            bird.bottom = base.top
            current_bird_y = 0




    pipe_x -= screen_speed
    screen.blit(pygame.transform.rotozoom(top_pipe_img, 0, 1.5), (pipe_x, pipe_y))
    screen.blit(pygame.transform.rotozoom(bottom_pipe_img, 0, 1.5), (pipe_x, pipe_y-450))
    if pipe_x < -screen_width/2:
        pipe_x = screen_width
        pipe_y = random.randrange(screen_height/2 - 100 ,screen_height/2 + 100)

    hitbox1 = (pipe_x+30 , pipe_y+40 , 95, 350)
    pygame.draw.rect(screen, (255, 0, 0), hitbox1, 2)

    hitbox2 = (pipe_x + 30, pipe_y-400 + 40, 95, 270)
    pygame.draw.rect(screen, (255, 0, 0), hitbox2, 2)

    birdbox = (bird_x, bird_y, 30, 30)
    pygame.draw.rect(screen, (255, 0, 0), birdbox, 2)

    if birdbox[0]+birdbox[2] >= hitbox1[0] and birdbox[0] <= hitbox1[0]+hitbox1[2]:
        if birdbox[1] + birdbox[3]  >= hitbox1[1] and birdbox[1] + birdbox[3] <= hitbox1[1] + hitbox1[3] or \
                birdbox[1] <= hitbox2[1]+ hitbox2[3]:
            print("HIT")
    """if birdbox.colliderect(hitbox1) or birdbox.colliderect(hitbox2):
        print("HIT")"""

    pygame.display.flip()
    clock.tick(60)