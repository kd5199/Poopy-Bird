import pygame, sys, random

fly_up = False
fly_down = True
ground = True
throw_poop = False
scale = 1.5
angle = 0

pygame.init()
clock = pygame.time.Clock()

screen_width = 700
screen_height = 500
BG_x = 0
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_icon(pygame.image.load("twitter.png"))
pygame.display.set_caption("Poopy BIRD")
BGImg = pygame.image.load("BGG.png")
screen_speed = 7

top_pipe_img = pygame.image.load("down.png")
bottom_pipe_img = pygame.image.load("up.png")
pipe_x = screen_width / 2
pipe_y_top = random.randrange(screen_height / 2, screen_height / 2 + 100)
pipe_y_bottom = random.randrange(screen_height / 2, screen_height / 2 + 100) - 400
screen.blit(top_pipe_img, (screen_width / 2, screen_height / 2 - 20))

bg_color = pygame.Color("grey12")
light_grey = (200, 200, 200)

birdimg = pygame.image.load("bird.png")

bird = pygame.Rect(screen_width / 2, screen_height, 30, 30)
bird_fly_speed_y = 3
bird_fall_speed_y = 3
bird_jump_height = -75
current_bird_y = 0
bird_y = screen_height / 2
bird_x = screen_width / 2 - 200


poop_x = bird_x
poop_y = bird_y
poopbox = (poop_x, poop_y, 30, 30)
poopimg = pygame.image.load("poop.png")


screen.blit(birdimg, (bird_x, bird_y))

base = pygame.Rect(0, screen_height - 20, screen_width, 20)

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
            if event.key == pygame.K_SPACE:
                poop_x = bird_x
                poop_y = bird_y
                throw_poop = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                pass
            if event.key == pygame.K_SPACE:
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
        # bird.bottom = base.top

    if fly_up:
        fly_down = False
        ground = False
        if bird_y > bird_jump_height + current_bird_y:
            bird_y -= bird_fly_speed_y
            angle = 30

        if bird_y <= bird_jump_height + current_bird_y:
            bird_y += bird_fall_speed_y
            fly_up = False
            fly_down = True

    if fly_down:
        if bird_y < base.top:
            bird_y += bird_fall_speed_y
            angle = -80


        if bird_y >= base.top:
            bird_y = base.top - 20

            screen.blit(birdimg, (bird_x, bird_y))
            fly_down = False
            ground = True
            bird.bottom = base.top
            current_bird_y = 0

    pipe_x -= screen_speed
    screen.blit(pygame.transform.rotozoom(top_pipe_img, 0, scale), (pipe_x, pipe_y_top))
    screen.blit(pygame.transform.rotozoom(bottom_pipe_img, 0, scale), (pipe_x, pipe_y_bottom))
    if pipe_x < -screen_width / 2:
        pipe_x = screen_width
        pipe_y_top = random.randrange(screen_height / 2, screen_height / 2 + 100)
        pipe_y_bottom = pipe_y_top - 400

    hitbox1 = (pipe_x + 30, pipe_y_top + 40, 95, 350)
    #pygame.draw.rect(screen, (255, 0, 0), hitbox1, 2)

    hitbox2 = (pipe_x + 30, pipe_y_bottom+ 40, 95, 320)
    #pygame.draw.rect(screen, (255, 0, 0), hitbox2, 2)

    birdbox = (bird_x, bird_y, 30, 30)
    #pygame.draw.rect(screen, (255, 0, 0), birdbox, 2)



    if birdbox[0] + birdbox[2] >= hitbox1[0] and birdbox[0] <= hitbox1[0] + hitbox1[2]:
        if birdbox[1] + birdbox[3] >= hitbox1[1] and birdbox[1] + birdbox[3] <= hitbox1[1] + hitbox1[3] or \
                birdbox[1] <= hitbox2[1] + hitbox2[3]:
            print("HIT")
    """if birdbox.colliderect(hitbox1) or birdbox.colliderect(hitbox2):
        print("HIT")"""
    if throw_poop:
        poopbox = (poop_x, poop_y, 30, 30)
        angle = 120
        #pygame.draw.rect(screen, (255, 0, 0), poopbox, 2)

        #poop = pygame.Rect(poop_x, poop_y, 30, 30)
        screen.blit(pygame.transform.rotate(poopimg, 30), (poop_x, poop_y))
        #pygame.draw.ellipse(screen, light_grey, poop)
        poop_x += 10
        poop_y += 4
        if poop_y >= screen_height:
            throw_poop = False

        if poopbox[0] + poopbox[2] >= hitbox1[0] and poopbox[0] <= hitbox1[0] + hitbox1[2]:
            if poopbox[1] + poopbox[3] >= hitbox1[1] and poopbox[1] + poopbox[3] <= hitbox1[1] + hitbox1[3]:
                pipe_y_top+=40
                throw_poop = False
            if poopbox[1] <= hitbox2[1] + hitbox2[3]:
                pipe_y_bottom -= 40
                throw_poop = False

    screen.blit(pygame.transform.rotate(birdimg, angle), (bird_x, bird_y))
    pygame.display.flip()
    clock.tick(60)