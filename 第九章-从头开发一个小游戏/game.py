import pygame
pygame.init()
screen = pygame.display.set_mode([800,600])
keep_going = True
pic = pygame.image.load("smile.png")
picx = 0
picy = 0
BLACK = (0,0,0)
WHITE = (255,255,255)
paddlew = 200
paddleh = 25
paddlex = 300
paddley = 550
points = 0
picw = 90
pich = 90
lives = 5
font = pygame.font.SysFont("Times", 24)
timer = pygame.time.Clock()
speedx = 10
speedy = 10
while keep_going:
    timer.tick(100)
    if lives == 0:
        pygame.quit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
    picx = picx + speedx
    picy += speedy
    if picx <= 0 or picx + pic.get_width() >= 800:
        speedx = -speedx
    if picy <= 0:
        speedy = -speedy
    if picy >= 500:
        lives -= 1
        speedy = -speedy
    screen.fill(BLACK)
    screen.blit(pic, (picx, picy))
    paddlex = pygame.mouse.get_pos()[0]
    paddlex -= paddlew/2
    pygame.draw.rect(screen, WHITE, (paddlex, paddley, paddlew, paddleh))
    # Check for paddle bounce
    if picy + pich >= paddley and picy + pich <= paddley + paddleh and speedy > 0:
        if picx + picw / 2 >= paddlex and picx + picw / 2 <= paddlex +  paddlew:
            points += 1
            speedy = -speedy
    draw_string = "Lives: " + str(lives) + " Points: " + str(points)
    text = font.render(draw_string, True, WHITE)
    text_rect = text.get_rect()
    text_rect.centerx = screen.get_rect().centerx
    text_rect.y = 10
    screen.blit(text, text_rect)
    pygame.display.update()
    timer.tick(60)
pygame.quit()