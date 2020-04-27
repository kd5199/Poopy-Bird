import pygame,sys

fly_up = False
fly_down = False
ground = True





pygame.init()
clock = pygame.time.Clock()


screen_width = 500
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jump")


bg_color = pygame.Color("grey12")
light_grey = (200,200,200)

birdimg = pygame.image.load("bird.png")
screen.blit(birdimg, (screen_width/2 - 15, screen_height-50))
ball = pygame.Rect(screen_width/2 - 15, screen_height-50, 30,30)
ball_fly_speed_y = 3
ball_fall_speed_y = 7
ball_jump_height = -100
current_ball_y = 0


base = pygame.Rect(0, screen_height-20, screen_width, 20)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                current_ball_y = ball.y
                print(current_ball_y)
                fly_up = True



        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                pass

    screen.fill(bg_color)



    pygame.draw.rect(screen, light_grey, base)


    if ball.bottom >= base.top:
        #ball.bottom = base.top
        pygame.draw.ellipse(screen, (255, 255, 255), ball)
        ground = True


    if fly_up:
        fly_down = False
        ground = False
        if ball.y > ball_jump_height+current_ball_y:
            screen.blit(birdimg, (screen_width / 2 - 15, screen_height - 50))
            ball.y -= ball_fly_speed_y
            pygame.draw.ellipse(screen, (0,255,0), ball)

        if ball.y <= ball_jump_height+current_ball_y:
            ball.y += ball_fall_speed_y
            fly_up = False
            fly_down = True


    if fly_down:
        if ball.y < base.top:
            ball.y += ball_fall_speed_y
            pygame.draw.ellipse(screen, (255,0, 0), ball)

        if ball.y >= base.top:
            ball.y = base.top
            fly_down = False
            ground = True
            ball.bottom = base.top
            current_ball_y = 0

    pygame.display.flip()
    clock.tick(60)